# Zero-Novelty Attempt 2 — FAILED / SAT-MAX Reset

**Execution:** `GHFS-2026-09-06-001`  
**Independent axis:** deployment model, self-managed lifecycle and compute topology  
**Result:** MATERIAL NOVELTY FOUND

## Material classes found

- GHE.com/data residency is a separate managed-cloud deployment context with dedicated hostnames, API endpoints, managed-user constraints and regional data placement.
- GitHub Enterprise Server adds a self-managed **instance lifecycle**: backup/restore, HA, upgrades, support-version lifecycle and administrator-operated infrastructure.
- GitHub Connect introduces a hybrid GHES↔cloud integration boundary.
- Actions execution is not one runner type. GitHub-hosted, larger hosted, persistent self-hosted, ephemeral self-hosted and runner-scale-set/ARC models have different ownership, networking, state and risk semantics.
- GHES has a deployment-specific Actions runner constraint: documented workflows use self-hosted runners rather than GitHub-hosted runners.

## Why this matters to the architecture

The context model must now explicitly include:

```text
DEPLOYMENT_MODEL
× PLATFORM_VERSION
× HOST/API_NAMESPACE
× IDENTITY_MODEL
× COMPUTE_OWNERSHIP
× DATA_LOCATION
```

Without those dimensions, claims about menus, APIs, Actions, permissions or features could be true on GitHub.com but false on GHE.com or GHES.

## Target impact

`flawless-ftxp` remains on ordinary GitHub.com using GitHub-hosted Actions. None of the new deployment/compute systems should be implemented in the repository; they are reference-architecture context dimensions.

## Saturation status

```text
zero-material-novelty: FAIL
consecutive zero passes: 0
SAT-MAX: RESET
```

## Next attempt

Traverse residual **hosting/account deployment variants and service-specific planes**, including government/data-residency variants, GitHub-hosted editors/dev environments, Pages/Packages/Gists remaining context, notification/search/accessibility and recent changelog deltas. If no new material class emerges, start zero-novelty counting; otherwise integrate and repeat.
