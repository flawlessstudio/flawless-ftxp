# Discovery Pass 5 — Navigation Occurrences, Actions, States and Routes

**Execution:** `GHFS-2026-09-06-001`  
**Status:** COMPLETE — NOT SATURATED  
**Material novelty:** MEDIUM-HIGH

## Outputs

- `registries/navigation-occurrence-registry.yaml`
- `registries/action-registry.yaml`
- `registries/state-registry.yaml`
- `registries/route-registry.yaml`

## Core modeling result

The requested menu/submenu/control granularity is now represented without contaminating the canonical taxonomy:

```text
CANONICAL CAPABILITY
   ├─ web occurrence
   ├─ settings occurrence
   ├─ mobile occurrence
   ├─ CLI occurrence
   ├─ REST occurrence
   └─ event/notification occurrence
```

The recursive discovery contract is:

```text
SURFACE
→ SECTION
→ SUBSECTION
→ COMPONENT
→ CONTROL
→ OPTION
→ ACTION
→ STATE TRANSITION
→ RESULTING SURFACE
```

A repeated action in several locations remains one canonical action with multiple occurrences.

## Current repository Settings seed

Official current documentation confirms repository configuration families for customization, feature enablement, Actions policy, access, visibility, forking, PR reviews, default branch/commit signoff/push policies, archive/LFS handling, push email notifications, autolinks, automatic issue closing, environments, advanced security and destructive operations.

The seed does not yet claim every exact sidebar label or responsive/menu variant. Those require live-context observation and are tracked as occurrence-level evidence rather than conceptual gaps.

## Route integrity

Routes are explicitly namespaced. A web route, REST endpoint, GraphQL operation, Git transport URL and webhook callback are different objects. Exact web URLs are marked `UNVERIFIED/VERIFY` when only the navigation path rather than URL pattern is confirmed by official documentation.

## State modeling result

Primary state and orthogonal condition are separated. For example, a pull request may be `open_ready` while simultaneously `checks_pending` and `review_requested`; these are not mutually exclusive lifecycle states.

## Remaining material work

Pass 6 should perform target-specific applicability/conformance mapping for `flawless-ftxp`, including a minimum-sufficient target architecture, lifecycle test plan and remediation dependency graph. After that, independent/adversarial rediscovery can begin.

```text
SAT-MAX PASS 1 = NOT READY
```
