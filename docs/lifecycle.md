# FTXP Lifecycle

The canonical lifecycle is sequential but adaptive. A material discovery may return execution to an earlier stage, followed by regression.

```text
TARGET
→ Intent Reconstruction
→ Normalization
→ Disambiguation
→ Scope Definition
→ Scope Lock
→ Candidate Discovery
→ Candidate Registry
→ Terminology Resolution
→ Canonicalization
→ Deduplication
→ Concept Typing
→ Primary Hierarchy
→ Facet Activation
→ Facet Assignment
→ Relationship Modeling
→ Granular Expansion
→ Cross-Cutting Analysis
→ Gap Analysis
→ Adversarial Review
→ Evidence Resolution
→ Material-Novelty Analysis
→ SAT-MAX Loop
→ Regression
→ Consolidation
→ Run Package
→ Validation
→ Baseline
→ Freeze
```

## Loop rule

If material novelty appears after scope lock:

```text
material novelty
→ validate
→ integrate
→ deduplicate
→ structural regression
→ continue discovery/challenge
```

## Stop rule

Stop when all applicable gates pass, SAT-MAX passes, regression passes, BLOCKERS = 0, and unresolved MAJOR = 0.

Further expansion after freeze requires a valid reopening trigger.
