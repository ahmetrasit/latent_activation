#!/usr/bin/env python3
"""Dependency-free validator for the JSON Schema keywords used by GSLS 2.1."""

from __future__ import annotations

import json
import re
from datetime import datetime
from pathlib import Path
from typing import Any

from common import PACKAGE_ROOT, ContractError, load_json


SCHEMA_ROOT = PACKAGE_ROOT / "schemas"


def _json_type_matches(value: Any, expected: str) -> bool:
    if expected == "null":
        return value is None
    if expected == "boolean":
        return isinstance(value, bool)
    if expected == "integer":
        return isinstance(value, int) and not isinstance(value, bool)
    if expected == "number":
        return isinstance(value, (int, float)) and not isinstance(value, bool)
    if expected == "string":
        return isinstance(value, str)
    if expected == "array":
        return isinstance(value, list)
    if expected == "object":
        return isinstance(value, dict)
    raise ContractError(f"Unsupported JSON Schema type: {expected}")


def _pointer(document: Any, fragment: str) -> Any:
    if not fragment or fragment == "#":
        return document
    if not fragment.startswith("#/"):
        raise ContractError(f"Unsupported JSON Schema fragment: {fragment}")
    value = document
    for token in fragment[2:].split("/"):
        token = token.replace("~1", "/").replace("~0", "~")
        if not isinstance(value, dict) or token not in value:
            raise ContractError(f"Unresolved JSON Schema pointer: {fragment}")
        value = value[token]
    return value


def _resolve_ref(ref: str, root_document: dict[str, Any], base_path: Path) -> tuple[Any, dict[str, Any], Path]:
    file_part, separator, fragment_part = ref.partition("#")
    fragment = f"#{fragment_part}" if separator else ""
    if file_part:
        target_path = (base_path.parent / file_part).resolve()
        try:
            target_path.relative_to(SCHEMA_ROOT.resolve())
        except ValueError as error:
            raise ContractError(f"Schema reference escapes schema root: {ref}") from error
        target_document = load_json(target_path)
        if not isinstance(target_document, dict):
            raise ContractError(f"Referenced schema is not an object: {target_path}")
        return _pointer(target_document, fragment), target_document, target_path
    return _pointer(root_document, fragment), root_document, base_path


def _format_ok(value: str, format_name: str) -> bool:
    if format_name != "date-time":
        return True
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return False
    return parsed.tzinfo is not None


def _validate(
    value: Any,
    schema: Any,
    root_document: dict[str, Any],
    base_path: Path,
    instance_path: str,
    errors: list[str],
) -> None:
    if schema is True:
        return
    if schema is False:
        errors.append(f"{instance_path}: rejected by false schema")
        return
    if not isinstance(schema, dict):
        raise ContractError(f"Schema node is not an object or boolean at {instance_path}")

    ref = schema.get("$ref")
    if isinstance(ref, str):
        resolved, target_root, target_path = _resolve_ref(ref, root_document, base_path)
        _validate(value, resolved, target_root, target_path, instance_path, errors)

    for child in schema.get("allOf", []):
        _validate(value, child, root_document, base_path, instance_path, errors)

    condition = schema.get("if")
    if condition is not None:
        condition_errors: list[str] = []
        _validate(value, condition, root_document, base_path, instance_path, condition_errors)
        if not condition_errors and "then" in schema:
            _validate(value, schema["then"], root_document, base_path, instance_path, errors)

    expected_type = schema.get("type")
    if expected_type is not None:
        allowed = [expected_type] if isinstance(expected_type, str) else expected_type
        if not isinstance(allowed, list) or not all(isinstance(item, str) for item in allowed):
            raise ContractError(f"Invalid type declaration in {base_path}")
        if not any(_json_type_matches(value, item) for item in allowed):
            errors.append(f"{instance_path}: expected type {' or '.join(allowed)}")
            return

    if "const" in schema and value != schema["const"]:
        errors.append(f"{instance_path}: must equal {schema['const']!r}")
    if "enum" in schema and value not in schema["enum"]:
        errors.append(f"{instance_path}: value {value!r} is not in the allowed enum")

    if isinstance(value, dict):
        required = schema.get("required", [])
        for field in required:
            if field not in value:
                errors.append(f"{instance_path}: missing required property {field!r}")
        properties = schema.get("properties", {})
        if not isinstance(properties, dict):
            raise ContractError(f"Invalid properties declaration in {base_path}")
        for field, child_schema in properties.items():
            if field in value:
                _validate(
                    value[field],
                    child_schema,
                    root_document,
                    base_path,
                    f"{instance_path}.{field}",
                    errors,
                )
        additional = schema.get("additionalProperties", True)
        for field in value.keys() - properties.keys():
            if additional is False:
                errors.append(f"{instance_path}: unexpected property {field!r}")
            elif isinstance(additional, dict):
                _validate(
                    value[field],
                    additional,
                    root_document,
                    base_path,
                    f"{instance_path}.{field}",
                    errors,
                )
        property_names = schema.get("propertyNames")
        if property_names is not None:
            for field in value:
                _validate(field, property_names, root_document, base_path, f"{instance_path}.<key>", errors)
        minimum_properties = schema.get("minProperties")
        if isinstance(minimum_properties, int) and len(value) < minimum_properties:
            errors.append(f"{instance_path}: requires at least {minimum_properties} properties")

    if isinstance(value, list):
        items = schema.get("items")
        if items is not None:
            for index, item in enumerate(value):
                _validate(item, items, root_document, base_path, f"{instance_path}[{index}]", errors)
        minimum_items = schema.get("minItems")
        if isinstance(minimum_items, int) and len(value) < minimum_items:
            errors.append(f"{instance_path}: requires at least {minimum_items} items")
        maximum_items = schema.get("maxItems")
        if isinstance(maximum_items, int) and len(value) > maximum_items:
            errors.append(f"{instance_path}: permits at most {maximum_items} items")
        if schema.get("uniqueItems") is True:
            encoded = [json.dumps(item, ensure_ascii=False, sort_keys=True) for item in value]
            if len(encoded) != len(set(encoded)):
                errors.append(f"{instance_path}: array items must be unique")

    if isinstance(value, str):
        minimum_length = schema.get("minLength")
        if isinstance(minimum_length, int) and len(value) < minimum_length:
            errors.append(f"{instance_path}: string is shorter than {minimum_length}")
        pattern = schema.get("pattern")
        if isinstance(pattern, str) and re.search(pattern, value) is None:
            errors.append(f"{instance_path}: string does not match {pattern!r}")
        format_name = schema.get("format")
        if isinstance(format_name, str) and not _format_ok(value, format_name):
            errors.append(f"{instance_path}: invalid {format_name} value")

    if isinstance(value, (int, float)) and not isinstance(value, bool):
        minimum = schema.get("minimum")
        maximum = schema.get("maximum")
        if isinstance(minimum, (int, float)) and value < minimum:
            errors.append(f"{instance_path}: value is below minimum {minimum}")
        if isinstance(maximum, (int, float)) and value > maximum:
            errors.append(f"{instance_path}: value is above maximum {maximum}")


def validate_instance(value: Any, schema_name: str, instance_path: str = "$") -> list[str]:
    schema_path = SCHEMA_ROOT / f"{schema_name}.schema.json"
    document = load_json(schema_path)
    if not isinstance(document, dict):
        raise ContractError(f"Schema document is not an object: {schema_path}")
    errors: list[str] = []
    _validate(value, document, document, schema_path, instance_path, errors)
    return errors
