# FTXP Architecture

FTXP is intentionally protocol-first and implementation-light.

## Core

```text
FTXP v1.0
├── C1 Normative Specification
├── C2 Canonical Execution Kernel
├── C3 Execution Profile
├── C4 Canonical Data Model
└── C5 Validation & Saturation System
```

## Derived template layer

```text
Canonical Template Set
├── T1 Canonical Execution Template
├── T2 Canonical Record Template
└── T3 Canonical Run Package Template
```

The template layer is derived from the core and does not constitute a sixth core component.

## Profiles

FT-L, FT-S and FT-X are presets of C3. They MUST NOT evolve into incompatible protocol forks.

## SSOT boundaries

- `spec/` owns normative protocol truth.
- `kernel/` owns executable instruction behavior.
- `profiles/` owns execution presets.
- `templates/` owns reusable input/output interfaces.
- `registries/` owns controlled vocabularies.
- `schemas/` owns logical data shape.
- `validation/` owns saturation and regression assurance.
- `docs/` explains but does not redefine normative truth.

## Complexity budget

FTXP does not require an application, database, API, graph database, RDF/OWL model, vector store, agent runtime, or MCP server. Such components may be introduced only when a demonstrated operational requirement exceeds the capability of the existing baseline.
