# Adversarial Rediscovery Pass 3

**Execution:** `GHFS-2026-09-06-001`  
**Mode:** residual topology, retention, provenance and delivery-semantics rediscovery  
**Result:** **MATERIAL NOVELTY FOUND**

## Findings

The remaining novelty is becoming narrower, but it is still architectural:

- **Stacked pull requests** add a dependent-PR topology and base/trunk governance semantics not represented by a flat PR lifecycle.
- **Copilot Memory** adds repository/user memory classes, validation against current repository state and explicit retention semantics.
- **SBOM export/dependency submission** adds a supply-chain inventory/export path that links dependency graph, Actions and APIs.
- **Webhook delivery** has its own asynchronous failure/recovery lifecycle: no automatic retry, bounded recent-delivery view, manual/API redelivery, possible throttling and non-guaranteed order.
- **Audit streaming** introduces external observability with at-least-once delivery semantics.
- **Codespaces** are ephemeral stateful development environments with retention/deletion policy.
- **Custom repository roles** have their own create/edit/delete lifecycle and inherited-permission consequences.

## Target impact

These findings do not materially change the minimum target architecture for `flawless-ftxp` today. They strengthen the global reference model and validate the `retention`, `topology`, `delivery semantics`, and `scope` facets.

The only target-adjacent supply-chain addition is SBOM export, which remains conditional and low-value while the repository has negligible software dependency surface.

## Saturation status

```text
material novelty: MEDIUM
zero-material pass: NOT ACHIEVED
SAT-MAX: NOT READY
```

## Regression implication

The reference architecture must now allow:

1. graph topologies, not only independent PRs;
2. data objects with retention/expiry and revalidation behavior;
3. asynchronous delivery semantics with duplicate/out-of-order/retry properties;
4. provenance exports such as SBOMs in addition to signed attestations.

## Next stage

Run **Zero-Novelty Attempt 1** using a source-independent traversal of current GitHub Docs/changelog categories, explicitly searching for a missing macro-domain, lifecycle class, security/trust boundary, data-retention class or programmatic interface. Cosmetic labels, new examples and minor product subfeatures do not count as material novelty.
