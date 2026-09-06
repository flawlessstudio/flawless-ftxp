# FTXP Conformance

FTXP defines four conformance levels.

## FTXP-Conformant

An execution is FTXP-Conformant when it satisfies all applicable MUST requirements in the normative specification.

## FTXP-Validated

An execution is FTXP-Validated when it is FTXP-Conformant and all applicable quality gates G0–G12 pass.

## FTXP-Saturated

An execution is FTXP-Saturated when it is FTXP-Validated and SAT-MAX passes.

## FTXP-Frozen

An execution is FTXP-Frozen when:

```text
FTXP-Validated
AND FTXP-Saturated
AND regression PASS
AND BLOCKERS = 0
AND unresolved MAJOR = 0
```

## Deviations

Any documented deviation from a SHOULD-level rule must include:

- the rule being deviated from;
- the reason;
- the expected impact;
- whether the deviation affects conformance, validation, saturation, or freeze status.

A MUST-level deviation makes the execution non-conformant unless the specification itself explicitly defines an exception path.
