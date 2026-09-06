# Git + GitHub Full-Spectrum Execution Workspace

This directory contains **derived research and assurance artifacts** produced by executing `docs/github-full-spectrum-master-prompt.md` with FTXP profile FT-X.

It is not part of the frozen FTXP normative specification. The normative SSOT remains under `spec/`, `kernel/`, `profiles/`, `templates/`, `registries/`, `schemas/`, and `validation/`.

## Execution order

1. `execution-manifest.yaml` — target, baseline snapshot, scope, evidence horizon, access boundaries, and execution state.
2. `source-registry.yaml` — authoritative source inventory used for discovery and evidence resolution.
3. `gap-register.yaml` — observed gaps, uncertainties, external blockers, and remediation eligibility.
4. `pre-execution-readiness.md` — PE0–PE15 readiness gate report.

Subsequent execution artifacts MUST be derived from these controls rather than duplicating them.

## Status semantics

- `DISCOVERED` — candidate found but not yet validated.
- `VALIDATED` — evidence supports the candidate.
- `CANONICAL` — normalized, deduplicated, typed and accepted into the reference architecture.
- `EXCLUDED` — intentionally outside scope or not materially distinct.
- `UNRESOLVED` — material question remains open.
- `INACCESSIBLE` — existence or state cannot be directly verified in the available context.

## Mutation boundary

Research artifacts may be added on the execution branch. Repository remediation MUST wait until a candidate gap has been verified, classified for applicability, justified, and assigned a validation and rollback path.
