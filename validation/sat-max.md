# SAT-MAX v1.0

SAT-MAX is the FTXP material-saturation criterion.

## Definition

SAT-MAX is reached when successive independent rounds of discovery, expansion, falsification, and gap analysis produce no new materially relevant classes, distinctions, relationships, invalidating evidence, or scope failures within the established scope and evidence horizon.

## Material novelty

Material novelty is governed by [`registries/material-novelty.yaml`](../registries/material-novelty.yaml).

## Algorithm

```text
PASS n
↓
DISCOVERY / CHALLENGE
↓
VALIDATE NEW CANDIDATES
↓
MATERIAL NOVELTY?
├─ YES
│  ↓
│  INTEGRATE
│  ↓
│  DEDUPLICATE
│  ↓
│  REGRESSION
│  ↓
│  NEXT PASS
│
└─ NO
   ↓
ADVERSARIAL / INDEPENDENT PASS
   ↓
MATERIAL NOVELTY?
├─ YES → integrate → continue
└─ NO
   ↓
SECOND CONSECUTIVE ZERO-MATERIAL PASS
   ↓
SAT-MAX PASS
```

## Minimum condition

FTXP v1.0 requires:

- at least two consecutive passes with zero material novelty; and
- at least one of those passes to be adversarial or independent.

## Non-claim

SAT-MAX does not prove universal ontological completeness. It proves material saturation only relative to the declared scope, granularity, evidence horizon, and execution conditions.
