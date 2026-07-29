# S100 Reader_M Baseline

Status: comparison target established; Hermetic Focus Trace reader outputs are
not present yet.

## Source Files

| role | file | notes |
| --- | --- | --- |
| reader_m baseline | `../quran-data/data/analysis/ayah-activation/v12-tr/s100/full_context_control/reader_m_ayah_walk.md` | strongest observed S100 reader effect; covers 100:1-11 and includes Turkish prose synthesis |
| regular whole-surah reader | `../quran-data/data/analysis/ayah-activation/v12-tr/s100/full_context_control/reader_s100_b_ayah_walk.md` | full-context S100 control; includes basmalah plus 100:1-11 |
| 11-ayah reader | `../quran-data/data/analysis/ayah-activation/v12-tr-11ayah/s100/full_context_control/reader_s100_a_ayah_walk.md` | plus/minus-5 / 11-ayah control; includes basmalah plus 100:1-11 |

## Structural Baseline

| reader | analysis sections | activated readings | Turkish synthesis |
| --- | ---: | ---: | --- |
| `reader_m` | 11 | 48 | yes |
| regular v12 | 12 including basmalah; 11 ayat = 32 readings | 35 including basmalah | no |
| v12 11-ayah | 12 including basmalah; 11 ayat = 33 readings | 36 including basmalah | no |

The important difference is not only volume. `reader_m` keeps more alternative
readings alive per ayah, writes frequent changed-reading language, and preserves
odd branch activations long enough for prose synthesis to render them. The
regular and 11-ayah readers often find the main structural lines but more often
compress them into a coherent surah-wide account.

## Reader_M Qualities To Recover

Hermetic Focus Trace should be judged against `reader_m` on these qualities:

- surprise: later ayat should make earlier ayat read differently, not merely
  confirm a theme;
- latent activation: branch-distant images should enter when the local sequence
  makes them active;
- changed reading: the response should explicitly say what the ayah changes
  from and what it changes into;
- abductive moves: the reader should show the inferred bridge from source
  phrase to later activation;
- multiple coexistence: literal, moral, bodily, ecological, forensic, and
  exploratory readings can coexist when anchored;
- prose usefulness: the output should give Layer 2 material that can become
  reader-facing commentary without flattening the surprise.

## Motif Targets From Reader_M

The new focus run should be able to recover several of these S100-specific
surprises:

- 100:1: panting/running becomes an inward chest symptom; crossed ground later
  becomes overturned ground.
- 100:2: spark becomes disclosure prototype; internal disease/decay and
  planning-risk remain live.
- 100:3: dawn raid becomes moral alteration; protective jealousy is inverted
  into possessive attachment.
- 100:4: dust becomes resurrection rehearsal; thirst/satisfaction is inverted
  into dry exposure.
- 100:5: entering the middle becomes judicial center; gathered force reverses
  into future restraint or collection.
- 100:6: ingratitude becomes severed nurture; barren land and caretaker/foster
  relation sharpen the accusation.
- 100:7: witness becomes embodied evidence; honey-in-comb becomes an
  extraction image.
- 100:8: love of good becomes a kernel in the chest; `khayr` can become a
  burrow-flushing mechanism.
- 100:9: grave-opening becomes forced knowledge; belongings scatter into moral
  inventory; predator/den imagery remains exploratory.
- 100:10: chest extraction becomes kernel assay; residue, source/front, and
  departure from watering-place remain live.
- 100:11: Lordly knowledge becomes cultivator/expert report; cloud, water,
  field-yield, covenant, and bundle readings converge.

## Comparison Method After HFT Reader Output Exists

Once `focus_trace/runs/s100/readers/reader_hft_a/*.focus_trace.json` exists,
compare each ayah against this baseline:

1. Count whether the response has a focus-only baseline, at least two
   context-triggered deltas, and at least one surprising outlier when the packet
   supports one.
2. Check whether each delta contains a genuine changed reading rather than
   generic restatement.
3. Check whether split-root branch citations include `mapped_root_id` with
   `branch_id`, especially for `ع د و`, `ث و ر`, and `ر ب ب`.
4. Score reader-facing usefulness separately from prose elegance. Hermetic
   Focus Trace may be behind `reader_m` as prose and still be production-useful
   if it supplies strong latent readings for Layer 2.

This is a baseline for the pending quality comparison, not a completed
comparison. Reader outputs are absent because the coordinator was instructed not
to spawn agents yet.
