# Contributing to FTXP

FTXP is a frozen protocol baseline. Contributions should preserve the Single Source of Truth and must not reopen settled architecture without a material reason.

## Change classes

- **Editorial** — wording, formatting, links, examples; no semantic change.
- **Patch** — compatible correction of a defect or inconsistency.
- **Minor** — compatible addition of capability.
- **Major** — incompatible protocol, schema, lifecycle, or semantic change.

## Normative changes

A change affecting `spec/`, `kernel/`, `profiles/`, `templates/`, `registries/`, `schemas/`, or `validation/` must identify:

1. the problem being solved;
2. affected SSOT artifacts;
3. the applicable reopening trigger, if the frozen baseline is reopened;
4. expected compatibility impact;
5. validation performed;
6. regression impact;
7. required version change.

## Reopening triggers

Only R1–R7 in [`registries/reopening-triggers.yaml`](registries/reopening-triggers.yaml) justify reopening a frozen baseline.

## Pull requests

Keep changes minimal and cohesive. Do not combine unrelated normative and cosmetic changes when they can be reviewed independently.

Before proposing a normative change, run:

```bash
python3 validation/validate_repository.py
```

A change must not introduce BLOCKER or unresolved MAJOR findings.
