# FTXP v1.0 — Normative Specification

Status: Frozen baseline  
Version: 1.0.0

## 1. Purpose

FTXP defines a reusable, evidence-aware protocol for constructing faceted taxonomies that are bounded by explicit scope, terminologically normalized, semantically deduplicated, structurally coherent, materially saturated, validated, and versionable.

FTXP optimizes for functional completeness inside a defined scope. It MUST NOT claim universal completeness merely because no further candidates were found.

## 2. Normative language

- **MUST / MUST NOT**: mandatory/prohibited.
- **SHOULD / SHOULD NOT**: recommended unless a documented reason justifies deviation.
- **MAY**: optional.

## 3. Core components

FTXP v1.0 contains exactly five core components:

1. Normative Specification.
2. Canonical Execution Kernel.
3. Execution Profile.
4. Canonical Data Model.
5. Validation & Saturation System.

The Canonical Template Set is a derived interface layer, not a sixth core component.

## 4. Execution profiles

- **FT-L**: light, bounded execution for narrow targets.
- **FT-S**: standard execution and default profile.
- **FT-X**: exhaustive execution for broad, polysemous, high-criticality, cross-domain, historical, emerging, or evidence-intensive targets.

FT-L, FT-S and FT-X MUST remain presets of one execution model.

## 5. Invariants

### I1 — Scope integrity
Every included concept MUST be inside the declared scope or explicitly justified as boundary context.

### I2 — Concept/term separation
A lexical form MUST NOT be treated automatically as a distinct concept.

### I3 — Primary classification consistency
Sibling nodes SHOULD share one recognizable primary classification basis.

### I4 — Facet orthogonality
Independent dimensions SHOULD be represented as facets rather than mixed arbitrarily into the primary hierarchy.

### I5 — Semantic deduplication
Distinct labels referring to the same concept MUST NOT survive as independent canonical concepts.

### I6 — Traceability
Material merges, splits, exclusions, deprecations, and unresolved decisions MUST remain traceable.

### I7 — Explicit uncertainty
Irreducible uncertainty MUST be recorded instead of hidden behind false precision.

### I8 — Material saturation
Execution MUST terminate by material-saturation criteria, not by arbitrary length or token exhaustion.

### I9 — Stable canonical identity
Canonical concepts SHOULD preserve stable identifiers across compatible revisions.

### I10 — Complexity control
A new layer, tool, template, or implementation MUST solve a demonstrated problem before entering the baseline.

## 6. Canonical lifecycle

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

## 7. Candidate lifecycle

Discovered candidates are provisional. The following states are not equivalent:

```text
DISCOVERED ≠ VALIDATED ≠ CANONICAL ≠ INCLUDED
```

Every material candidate MUST resolve to one of:

- KEEP
- MERGE
- ALIAS
- RELATE
- SPLIT
- EXCLUDE
- UNRESOLVED
- REJECT

## 8. Deduplication

FTXP defines six deduplication levels:

- D1 Exact.
- D2 Lexical.
- D3 Referential.
- D4 Semantic.
- D5 Functional.
- D6 Structural.

A difference in wording alone is not evidence of conceptual distinctness.

## 9. Granularity

The target depth is **maximal useful granularity**, not maximal theoretically possible granularity.

Expansion SHOULD stop when additional subdivision produces only examples, aliases, microvariants, irrelevant distinctions, or categories with no material discriminative value.

## 10. Discovery dimensions

FT-S and FT-X SHOULD consider, where applicable:

- upward discovery;
- downward discovery;
- vertical discovery;
- horizontal discovery;
- lateral discovery;
- lexical discovery;
- temporal discovery;
- cross-domain discovery.

Discovery produces candidates; it does not authorize inclusion.

## 11. Evidence model

When external verification is required, evidence SHOULD prioritize:

1. primary specification;
2. official documentation;
3. official repository;
4. standards organization;
5. authoritative technical publication;
6. research;
7. high-quality secondary source.

Executions MUST distinguish fact, inference, assumption, and convention when the distinction is material.

## 12. Quality gates

FTXP defines G0–G12:

- G0 Scope
- G1 Terminology
- G2 Candidate Coverage
- G3 Canonicalization
- G4 Deduplication
- G5 Hierarchy
- G6 Facet Orthogonality
- G7 Relationships
- G8 Evidence
- G9 Gap Analysis
- G10 Adversarial Review
- G11 SAT-MAX
- G12 Regression

Gate states are PASS, PASS_WITH_MINOR_FINDINGS, FAIL, or NOT_APPLICABLE.

Finding severities are BLOCKER, MAJOR, MINOR, and INFO.

A baseline MUST NOT freeze while BLOCKER > 0 or unresolved MAJOR > 0.

## 13. SAT-MAX

SAT-MAX is reached when successive independent discovery and challenge passes produce no material novelty within the declared scope.

Material novelty includes:

- a new family;
- a new class;
- a necessary conceptual split;
- a structural relationship that changes interpretation;
- a material coverage gap;
- evidence invalidating an active decision;
- a scope/boundary failure.

Aliases, translations, examples, cosmetic reformulations, and purely confirmatory evidence are not material novelty by themselves.

FTXP v1.0 requires:

- two consecutive zero-material-novelty passes; and
- at least one adversarial or independent pass.

## 14. Freeze condition

An execution is FTXP-Frozen only when:

```text
all applicable gates PASS
AND SAT-MAX PASS
AND regression PASS
AND BLOCKERS = 0
AND unresolved MAJOR = 0
```

## 15. Reopening triggers

A frozen baseline may be reopened only by:

- R1 New material evidence.
- R2 Material domain change.
- R3 Canonical terminology or standard change.
- R4 Discovered contradiction.
- R5 Demonstrated material gap.
- R6 Scope change.
- R7 Use-case requirement change.

Cosmetic edits, new examples, aliases, or generic desires for additional breadth do not trigger reopening.

## 16. Non-goals

FTXP is not:

- a universal ontology;
- a guarantee of infinite or universal knowledge completeness;
- a requirement for RDF/OWL;
- a requirement for multi-agent orchestration;
- a requirement for a database, API, GUI, MCP server, or vector store.

Those MAY be implemented later only if an operational need justifies them.
