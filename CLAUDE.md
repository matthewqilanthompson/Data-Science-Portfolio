# Data-Science-Portfolio — Claude Code Instructions

## Every claim (numbers, techniques, course codes) must match what the code/data actually shows

This is the single most repeated fix pattern in the repo's history — a dozen+ commits correcting
overclaims after the fact: `7e3d9d8` (fix the 10.13% observation story to match the data), `4d7d156`
(correct coding systems to SNOMED-CT/LOINC), `60a8d14` (correct README claims the code doesn't
support), `edb591e` (fix course number INFO 521 → INFO 511), `f320e25` (fix SQL technique: window
functions → correlated subqueries), `3115579` (replace an ETL claim with data wrangling for accuracy),
`61a5b25` (correct a ROC AUC overclaim), `bddd4f0` (fix a metric mislabel). Before writing or editing
any README/project-description text, verify the specific number/technique/course-code against the
actual code or data it describes — don't restate a plausible-sounding claim from memory.

## Never commit secrets or hardcoded local paths

`8fdfb29` had to strip a leaked Codabench `secret_key` plus hardcoded local paths; `cab757d` was a
separate instance of stripping a hardcoded user path. Grep for secrets/absolute-paths before
committing, especially in notebook outputs and config files.

## `.github/copilot-instructions.md` references a `WARP.md` that doesn't exist

Stale cross-reference — same class of issue as a dead link. If cleaning up `copilot-instructions.md`,
either restore the missing content or remove the reference.
