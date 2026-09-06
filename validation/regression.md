# FTXP Regression Protocol

Regression validation ensures that late-stage corrections or extensions do not reintroduce previously resolved defects.

## Required checks

Before freeze, verify that changes have not:

- reintroduced exact, lexical, referential, semantic, functional, or structural duplicates;
- broken parent/child consistency;
- introduced hierarchy cycles;
- converted aliases into canonical concepts;
- merged materially distinct concepts;
- invalidated facet orthogonality;
- broken typed relationships;
- removed required provenance;
- contradicted registries;
- created unresolved BLOCKER or MAJOR findings;
- invalidated SAT-MAX evidence;
- produced version mismatches between root metadata and normative documents.

## Trigger

Regression MUST run:

1. after every material integration during SAT-MAX;
2. after adversarial corrections;
3. immediately before baseline freeze.

## Result

Regression status is one of:

- PASS
- PASS_WITH_MINOR_FINDINGS
- FAIL

A FAIL blocks freeze.
