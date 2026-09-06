# Discovery Pass 2 — Repository Lifecycle, Settings, Surfaces and Governance

**Execution:** `GHFS-2026-09-06-001`  
**Status:** COMPLETE — NOT SATURATED  
**Material novelty:** HIGH

## Focus

Pass 2 decomposed the repository-scoped control plane because it directly determines whether `flawless-ftxp` can satisfy repository lifecycle, governance, release and reconstructability gates.

Primary official evidence established that current repository configuration spans repository customization/feature enablement, access, general repository settings, branch/merge configuration, branch protection/rulesets, Actions policy, environments/deployments, security and analysis, releases and destructive lifecycle operations.

## Artifacts

- `registries/repository-setting-registry.yaml`
- `registries/repository-lifecycle-registry.yaml`
- `registries/governance-control-registry.yaml`
- `registries/repository-surface-registry.yaml`

## Material findings

### 1. Governance is a layered effective configuration

Repository behavior is not determined by one Settings page. Effective behavior may combine repository merge settings, branch protection/rulesets, organization/enterprise policy, Actions policy, CODEOWNERS and environment protections.

### 2. CODEOWNERS is not an enforcement mechanism by itself

It provides ownership/review routing. Requiring code-owner approval is a separate branch/ruleset governance decision.

### 3. Existing CI is not currently a required merge gate

`flawless-ftxp` has a validation workflow, but `main` is unprotected and no ruleset exists. Therefore a passing workflow is evidence, not yet an enforced precondition for modifying `main`.

### 4. Release identity is multi-object

The following remain distinct:

```text
semantic/repository version
≠ Git tag
≠ commit SHA
≠ GitHub Release
```

GitHub Releases are tag-based. Current GitHub also supports immutable releases, which lock the associated tag and assets after publication and generate a release attestation. Whether this repository should enable immutability is an applicability decision, not an automatic requirement.

### 5. Destructive settings are lifecycle transitions

Visibility changes, transfer and deletion can change feature availability, permissions, forks and recoverability. They belong in lifecycle/failure/recovery modeling rather than a miscellaneous Settings appendix.

### 6. Environment protection is separate from branch merge protection

Environments can require reviewers, timers, branch/tag restrictions and GitHub-App protection rules before jobs proceed and secrets become available. This does not replace branch/ruleset governance.

## `flawless-ftxp` implications — still non-mutating

The pass reinforces the initial blocker-for-freeze findings:

- protect/enforce the `main` integration path using the minimum sufficient ruleset or equivalent control;
- make the existing validation check a required condition if that mechanism is chosen;
- establish exact version → tag → release → commit reconstructability;
- decide whether merged branch auto-deletion is appropriate;
- expand repository validation only after its invariants are specified;
- verify security settings separately before claiming security conformance.

No remediation is performed in this pass.

## Remaining material discovery

Pass 3 should focus on identity/access/policy inheritance plus Actions/security/trust boundaries, because those dimensions constrain the safe governance configuration that could later be applied to `flawless-ftxp`.

```text
SAT-MAX PASS 1 = NOT READY
```
