# `flawless-ftxp` — Minimum Sufficient Target Repository Architecture

**Status:** proposed target derived from Discovery Passes 1–6; remediation remains locked until review of the research package.

## Design rule

```text
DISCOVER EVERYTHING MATERIAL
≠
IMPLEMENT EVERYTHING DISCOVERED
```

The target is a **public, spec-first protocol SSOT**, not a software product. Therefore no application runtime, database, container platform, frontend, backend, deployment environment, package registry, Codespace requirement, MCP server, or project-management system is added without a concrete use case.

## Target layers

### A. Canonical protocol SSOT — keep

- `spec/`
- `kernel/`
- `profiles/`
- `templates/`
- `registries/`
- `schemas/`
- `validation/`

These remain the protocol-defining layers.

### B. Repository gateway/governance — keep and complete

- `README.md`
- `VERSION`
- `CHANGELOG.md`
- `CONTRIBUTING.md`
- `.github/CODEOWNERS`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/ISSUE_TEMPLATE/`
- `.github/workflows/validate.yml`

Add only if validated/applicable:

- `SECURITY.md` — recommended for responsible disclosure.
- `CITATION.cff` — recommended for citation of the protocol/reference artifact.
- `LICENSE` — **human decision**, never inferred.
- `CODE_OF_CONDUCT.md` — only if actual community participation warrants it.

### C. Validation/reference assurance — complete

Target:

```text
validation/
  validate_repository.py
  sat-max.md
  regression.md

tests/
  reference-cases/

examples/
  [only canonical examples]

runs/
  reference/
  [only regression/reference runs worth preserving]
```

No empty directories merely for architectural symmetry.

### D. Derived research/reference artifacts — keep outside normative truth

`research/github-full-spectrum/` contains execution-derived evidence and registries. It MUST NOT become a second normative FTXP specification.

## Target GitHub configuration

### `main`

Minimum enforceable path:

```text
short-lived branch
→ pull request
→ required `validate` check
→ conversations resolved
→ squash merge
→ post-merge validation
```

Rules should also prevent force-push and deletion of `main`.

### Review policy

Do **not** invent a fake two-person governance model. The repository is currently owned by a personal account and has one canonical CODEOWNER. Requiring one independent approval would make the normal owner-authored PR path impossible unless another genuine maintainer is added.

Therefore target now:

- PR required: YES
- validation required: YES
- conversation resolution: YES
- mandatory approval count: 0
- code-owner approval enforcement: CONDITIONAL on a second genuine eligible reviewer

CODEOWNERS remains useful for ownership metadata and future review routing.

### Merge policy

Recommended:

- squash merge: ON
- merge commits: OFF
- rebase merge: OFF
- linear history: ON via rule if compatible
- delete head branches after merge: ON
- auto-merge: optional
- update branch: optional/useful when strict checks need current base
- merge queue: NOT APPLICABLE at current scale

This choice preserves one logical main commit per accepted PR while retaining detailed branch/PR history in GitHub.

### Actions

Current workflow already has two strong properties:

- explicit `contents: read` only;
- `actions/checkout` pinned to a full commit SHA.

Target adds repository-level enforcement of full-SHA action pinning if available without conflicting with necessary reusable workflow semantics, plus future-workflow review against least privilege.

### Security

Before freeze, verify effective state of GitHub's current minimum public-repository security controls:

- Dependabot alerts
- secret scanning
- push protection
- code scanning
- dependency graph

Do not mark `PASS` from documentation defaults alone; observe the target state.

### Release/reconstructability

Target invariant:

```text
FTXP protocol version
↔ repository VERSION
↔ exact main commit SHA
↔ Git tag v1.0.0
↔ GitHub Release v1.0.0
↔ validation evidence
↔ freeze manifest
```

These objects remain distinct but traceably linked.

Recommended: enable release immutability **before** publishing future frozen releases if the final release workflow is compatible, so the associated tag/assets gain stronger integrity guarantees.

## GitHub-native surface minimization

Current `wiki=true` and `projects=true` have no established use case. For this repository the versioned documentation and issue/PR workflow are sufficient. Disable unused surfaces only after the applicability decision is accepted; do not delete or migrate data blindly.

## Explicit non-goals

- no issue tracker replacement;
- no knowledge graph engine;
- no database;
- no CI matrix unrelated to repository invariants;
- no deployment environment merely to exercise GitHub features;
- no package publication unless FTXP acquires a real distributable implementation;
- no artificial community governance objects without participants;
- no action/plugin added for a check that can be implemented more simply and reproducibly.
