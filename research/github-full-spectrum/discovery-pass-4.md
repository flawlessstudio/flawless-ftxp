# Discovery Pass 4 — Programmatic Interfaces, Events, Notifications and Client Parity

**Execution:** `GHFS-2026-09-06-001`  
**Status:** COMPLETE — NOT SATURATED  
**Material novelty:** HIGH

## Outputs

- `registries/programmatic-interface-registry.yaml`
- `registries/event-webhook-registry.yaml`
- `registries/notification-registry.yaml`
- `registries/client-parity-registry.yaml`

## Material conclusions

### 1. Git, `gh`, REST, GraphQL and webhooks are distinct interfaces

GitHub CLI explicitly brings GitHub platform operations such as repositories, issues, pull requests, Actions, releases, Codespaces and API access to the terminal. It does not replace the Git CLI's repository/object/history operations.

### 2. Webhook events are not a lifecycle taxonomy by themselves

Webhook event names are machine-delivery representations of platform events. A single conceptual transition can simultaneously appear as a UI timeline event, Actions trigger, webhook payload, notification reason and audit/activity record. The canonical event model therefore sits above all delivery channels.

### 3. Notification reasons are contextual state

Notification delivery depends on participation, watching, manual subscriptions and custom repository watch settings. Reason values can change for a thread after a later higher-priority interaction such as an explicit mention.

### 4. API coverage adds limits absent from a UI-only map

REST and GraphQL have separate primary and secondary rate-limit models. REST API versioning is date-based and breaking changes move to a new API version. These constraints are part of the programmatic lifecycle, not incidental documentation.

### 5. Client parity is demonstrably non-uniform

GitHub Mobile explicitly supports notification triage, issues/PR collaboration, editing PR files, repository code search and authentication workflows. GitHub Desktop focuses primarily on local Git/GitHub workflows such as clone/fork, branches, commits, sync and PR creation. Therefore `CLIENT` remains an independent facet rather than a presentation detail.

## Remaining uncertainties

The first parity matrix deliberately uses `UNKNOWN`/`PARTIAL_OR_UNKNOWN` rather than inventing equivalence for unverified client capabilities. These cells are targets for later rediscovery, not evidence of absence.

## Next pass

Pass 5 should decompose surface/navigation/settings occurrence structure and build the first action/state/route cross-map. This is required to approach the user's requested menu/submenu/surface granularity without duplicating canonical features.

```text
SAT-MAX PASS 1 = NOT READY
```
