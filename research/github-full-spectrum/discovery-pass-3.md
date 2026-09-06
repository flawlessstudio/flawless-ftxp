# Discovery Pass 3 — Access, Actions Security, Trust Boundaries and Security Controls

**Execution:** `GHFS-2026-09-06-001`  
**Status:** COMPLETE — NOT SATURATED  
**Material novelty:** HIGH

## Outputs

- `registries/access-role-permission-registry.yaml`
- `registries/actions-security-trust-registry.yaml`
- `registries/security-control-registry.yaml`
- `registries/policy-inheritance-registry.yaml`

## Material conclusions

### 1. The target is a personal-account repository

`flawlessstudio/flawless-ftxp` is owned by a GitHub `User`, not an organization. Organization roles such as Triage/Write/Maintain/Admin, security manager, CI/CD admin, teams and organization-level policy are essential to the **reference architecture** but must not be blindly assumed to govern this target repository.

This materially constrains the future governance design: the minimum sufficient protection for `main` should use controls actually available to a public personal-account repository rather than an organization-centric template.

### 2. Role, permission, policy and app authorization are independent dimensions

GitHub Apps separate installation from authorization. Installation grants repository/organization resource access and repository selection; authorization grants requested account permissions and allows acting on behalf of the user. User access tokens are additionally bounded by the user's own permissions.

### 3. Actions security is already partially strong

The existing FTXP validation workflow explicitly grants only `contents: read`, uses no repository secret, and pins `actions/checkout` to a full commit SHA. These match current GitHub secure-use guidance.

This does **not** prove repository-wide Actions policy because the effective repository setting, organization inheritance (not applicable as current owner), and other future workflows remain separate concerns.

### 4. Current security conformance cannot be declared yet

Official GitHub guidance for public repositories identifies Dependabot alerts, secret scanning, push protection and code scanning as a minimum security baseline. The connected repository capability does not expose enough effective security configuration to confirm each control. They remain `UNKNOWN/INACCESSIBLE`, not `OFF`.

### 5. Push protection is cross-surface

It is not merely a Git push feature. Current GitHub documentation describes enforcement across command-line pushes, GitHub web commits, file uploads, REST requests and public-repository GitHub MCP interactions. This validates the full-spectrum model's interaction-channel facet.

### 6. Repository governance is an authorization boundary

A future `main` ruleset must model bypass explicitly. Adding a rule without defining who can bypass it would not close RQ17.

## New target-specific candidate

The low-level research commits created through the connected Git-data API are currently unsigned, while the GitHub-created squash merge commits on `main` are verified. This is **not yet classified as a defect**: requiring signed commits may interact with the chosen automation/write path. It must be tested before becoming a required control.

## Next discovery pass

Pass 4 should map programmatic interfaces, event/webhook/notification architecture and client parity, then tie these to actions/state transitions. This is required before surface/navigation saturation can be attempted.

```text
SAT-MAX PASS 1 = NOT READY
```
