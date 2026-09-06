# FTXP — Faceted Taxonomy Execution Protocol

`flawless-ftxp` is the canonical, versioned Single Source of Truth (SSOT) for **FTXP — Faceted Taxonomy Execution Protocol**.

FTXP is a protocol for producing faceted taxonomies that are explicit in scope, terminologically normalized, semantically deduplicated, structurally coherent, evidence-aware, materially saturated, validated, and versionable.

## Current baseline

- Protocol: **FTXP v1.0.0**
- Repository baseline: **v1.0.0**
- Status: **Frozen baseline**
- Default execution profile: **FT-S**

## Core architecture

1. Normative Specification
2. Canonical Execution Kernel
3. Execution Profile
4. Canonical Data Model
5. Validation & Saturation System

## Canonical Template Set

- T1 — Canonical Execution Template
- T2 — Canonical Record Template
- T3 — Canonical Run Package Template

FT-L, FT-S and FT-X are presets of one execution model, not independent implementations.

## Repository map

- [`spec/`](spec/) — normative protocol definition
- [`kernel/`](kernel/) — canonical executable instruction kernel
- [`profiles/`](profiles/) — FT-L / FT-S / FT-X presets
- [`templates/`](templates/) — canonical reusable templates
- [`registries/`](registries/) — controlled vocabularies and protocol registries
- [`validation/`](validation/) — quality gates, SAT-MAX and regression
- [`docs/`](docs/) — explanatory architecture, lifecycle and derived execution/reference documentation
- [`.github/`](.github/) — repository-native contribution and validation controls

## Derived execution references

Derived execution/reference artifacts apply FTXP without redefining the normative protocol. The canonical Git + GitHub full-spectrum FT-X instruction is [`docs/github-full-spectrum-master-prompt.md`](docs/github-full-spectrum-master-prompt.md).

## Canonical lifecycle

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

## Saturation

FTXP does **not** claim universal ontological completeness. SAT-MAX means material saturation inside an explicit scope and evidence horizon.

FTXP v1.0 requires two consecutive passes with no material novelty, including at least one adversarial or independent pass.

## Change policy

A frozen baseline is reopened only by a material trigger: new material evidence, material domain change, canonical terminology/standard change, discovered contradiction, demonstrated material gap, scope change, or use-case requirement change.

See [`spec/FTXP-v1.0.md`](spec/FTXP-v1.0.md) for the normative definition and [`CHANGELOG.md`](CHANGELOG.md) for version history.
