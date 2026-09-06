# Discovery Pass 1 — Domain, Product/Interface, Entity and Feature-Family Seed

**Execution:** `GHFS-2026-09-06-001`  
**Status:** COMPLETE — NOT SATURATED  
**Material novelty:** HIGH

## Method

Pass 1 used two independent primary-source families:

1. current Git documentation (`git`, `gitglossary`, `gitworkflows`), and
2. the current GitHub Docs information architecture plus selected official product/reference pages.

The GitHub Docs root currently exposes top-level documentation groups covering onboarding/account concerns, collaborative coding, Copilot, CI/CD, security/code quality, client apps, project management, enterprise/teams, developer interfaces and community surfaces. These are treated as **discovery evidence**, not blindly as a product taxonomy.

## Output

Pass 1 produced four explicit seed registries:

- `domain-registry.yaml`
- `product-interface-registry.yaml`
- `entity-registry.yaml`
- `feature-family-registry.yaml`

The split is deliberate:

```text
DOCUMENTATION DOMAIN
≠ PRODUCT
≠ INTERFACE
≠ ENTITY
≠ FEATURE FAMILY
```

## Important distinctions established

- Git and GitHub remain separate systems; GitHub CLI is not Git.
- GitHub App installation and GitHub App authorization are separate entities/processes.
- REST, GraphQL, Webhooks, Git transport and CLI are separate interaction models.
- Roles, permissions, policies, plans and account scopes are separate context dimensions.
- Actions workflow definitions, runs, jobs, steps, actions and runners are separate entities.
- Release, tag and repository baseline are separate concepts.
- UI/client occurrences will later map to canonical concepts rather than creating duplicate concepts.

## First-pass candidate families

The seed now covers repository lifecycle, collaboration, planning, automation, releases, packages, Pages, Codespaces, identity/access, governance, Apps/integrations, REST/GraphQL/webhooks/CLI, security, notifications, audit/observability, billing, clients, Copilot/agentic capabilities, failure/recovery and temporal variation.

## Why SAT-MAX cannot run yet

This pass intentionally remains high level. It does not yet exhaust:

- repository settings and nested controls,
- every role/permission and policy interaction,
- route/action/state registries,
- notification reasons and event catalog,
- Actions trigger/context matrix,
- REST endpoint families and GraphQL schema categories,
- webhook event catalog,
- security feature availability matrix,
- client parity,
- menu/surface/navigation occurrences,
- failure/recovery mappings,
- applicability to `flawless-ftxp`.

Therefore:

```text
SAT-MAX PASS 1 = NOT READY
```

## Next pass

Discovery Pass 2 MUST decompose the current GitHub repository lifecycle and repository settings/governance surface, because those dimensions directly control the correctness and freeze-readiness of `flawless-ftxp`.
