# Git + GitHub E2E Lifecycle Test Plan for `flawless-ftxp`

The lifecycle test is a **post-remediation verification** exercise. It must not be run against an unenforced baseline and then mistaken for proof of governance.

## Test L1 — Happy-path governed change

```text
issue/change rationale
→ short-lived branch
→ valid change
→ commit
→ pull request
→ `validate` required check PASS
→ review/conversation state acceptable
→ squash merge
→ main push validation PASS
→ branch cleanup
```

Evidence to retain: branch SHA, PR number, check run, merge SHA, main validation run, cleanup state.

## Test L2 — Validation failure blocks integration

Create a temporary branch that intentionally violates a harmless validator invariant (for example a deliberately inconsistent test fixture or temporary VERSION mismatch on the branch), open a PR, and prove:

1. `validate` fails;
2. GitHub reports the required check as failed;
3. normal merge is blocked by the main ruleset;
4. fix the branch;
5. validation passes;
6. merge becomes eligible.

The invalid test change MUST NOT be merged.

## Test L3 — Direct-main mutation protection

Attempt a safe no-op/test direct update path to `main` through an interface that would otherwise have write permission. Expected result: blocked by the effective rule unless an explicitly documented bypass is invoked.

Do not use destructive force-push testing on the real frozen baseline.

## Test L4 — Force-push/deletion policy inspection

Verify through ruleset effective state/API/UI that force pushes and deletion of `main` are blocked. Prefer configuration evidence over destructive live testing.

## Test L5 — Post-merge regression

After a successful test PR merge, verify the `push` workflow on `main` passes against the exact integrated commit.

## Test L6 — Version/tag/release/reconstructability

For the final release candidate:

```text
validated main SHA
→ VERSION/CHANGELOG consistency
→ v1.0.0 tag points exactly to SHA
→ GitHub Release uses v1.0.0
→ release metadata records SHA and validation state
→ freeze manifest records all identifiers
→ clean checkout/tag reconstruction reproduces canonical baseline
```

If release immutability is adopted, enable it before publishing the release and verify the release is marked immutable afterwards.

## Test L7 — Recovery without destructive history rewriting

Create a reversible test change after baseline (or use a dedicated test branch), then demonstrate `git revert` / PR-based rollback semantics and validation of the restored logical state. The canonical test MUST prefer revert over rewriting published main history.

## Test L8 — Branch recovery/hygiene

Verify merged branch deletion policy. If a deleted branch must be recoverable for a documented short window/context, verify the platform-supported restoration path on a disposable branch rather than on baseline branches.

## Test L9 — Security configuration evidence

Record observed effective state of Dependabot alerts, secret scanning, push protection, code scanning and dependency graph. Do not intentionally commit a real secret or vulnerability. If testing push protection, use GitHub-approved harmless test patterns only when official guidance supports a safe test path.

## Test L10 — Workflow supply-chain policy

Attempt a PR containing a temporary workflow fixture/reference that violates the chosen action pinning policy only if it can be safely isolated. Expected: policy/check prevents use or merge. Remove fixture before final integration.

## Exit criteria

- all applicable tests PASS;
- no invalid/destructive fixture merged;
- exact final main SHA identified;
- release/tag/freeze identifiers consistent;
- RQ14–RQ17 pass;
- blockers=0 and unresolved majors=0.
