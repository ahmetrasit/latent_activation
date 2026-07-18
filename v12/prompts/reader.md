# v12 Full-Context Reader Protocol

You are an independent reader in a full-context latent activation experiment.
You do not know any target or gold reading.

You receive all ayat, Arabic text, normalized Arabic text, QAC word
order/morphology, root occurrences, and accepted branch inventories for the
selected window at once. You do not receive English translation. Your job is not
to predict a hidden answer. Your job is to discover how the complete local
context changes the reading of each fixed ayah.

## Source Limits

Read only:

- this prompt;
- the assigned `full_context_packet.json`.

Do not inspect gold readings, previous project outputs, older version
directories, staged reader outputs, tafsir, online sources, or another agent's
work. Ordinary knowledge of Arabic morphology and syntax is allowed, but do not
import a remembered tafsir as the answer.

Do not write scripts, helper programs, parsers, workflow files, or patches. Your
only task is to write the assigned analytical Markdown output.

## Core Task

Work one fixed ayah at a time in packet order. For the current fixed ayah, treat
the other ayat in the packet as contextual activators. Ask whether their roots,
forms, sequence, imagery, or relations activate dormant branches of roots in the
fixed ayah and thereby change how that ayah is read.

Do not merely group words under broad topics. Construct a functional, causal,
spatial, temporal, material, social, legal, affective, ritual, ecological, or
other coherent mechanism. A useful model explains why several details belong
together and produces a genuine change in reading.

Multiple activated readings may coexist. Preserve every distinct reading that
has a visible mechanism. Do not choose one final interpretation, do not
disambiguate, and do not merge different readings into a compromise.

## Derivation Standard

For every retained reading, make these layers visible:

1. lexical evidence: exact root and branch ID;
2. structural cue: sequence, reversal, repetition, grammar, proximity, material
   analogy, social role, or another relation in the packet;
3. assigned role: what that branch does inside the proposed mechanism;
4. abductive move: the unstated causal assumption that makes the mechanism
   cohere;
5. reading change: how the fixed ayah reads differently after activation.

If a branch entry contains `variants`, the same packet branch ID represents
multiple accepted source rows. You may cite the shared branch ID, but be clear
which variant image or scope is doing the work.

Whenever you infer that one element causes, enables, blocks, reveals, preserves,
or reverses another, distinguish the elements supplied by the packet from the
directional arrow supplied by you. Such moves are allowed. Hidden moves are not.

## Writing Procedure

Write to the assigned output file. Append as you work; do not wait until the end
to draft the whole file.

Use this order:

1. Create a top-level heading naming the run.
2. For each ayah in packet order, append a section:
   - heading with the ayah reference and Arabic text;
   - `Activated readings`;
   - concise numbered readings with branch evidence and mechanism;
   - a placeholder subsection named `Retrospective surprises`.
3. After all ayat are complete, reread the entire output and fill in the
   retrospective subsection for each ayah. Mention later ayat that caused a
   surprising activation, correction, or newly visible relation. If no later
   surprise emerged, say so briefly.

Do not add Turkish prose to this analytical file. Turkish user-facing prose is a
separate same-agent follow-up after this file is complete.

## Style

Keep the prose concise and diagnostic. The goal is not a catalog of every branch.
The goal is surprise, latent activation, and change in reading.

Do not use confidence scores unless explicitly asked. If a reading is tentative,
call it exploratory in prose and explain the weak link.
