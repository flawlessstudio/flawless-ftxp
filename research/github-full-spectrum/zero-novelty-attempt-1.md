# Zero-Novelty Attempt 1 — FAILED / SAT-MAX Reset

**Execution:** `GHFS-2026-09-06-001`  
**Independent axis:** enterprise IAM, enterprise policy and network boundaries  
**Result:** MATERIAL NOVELTY FOUND

## Why this counts as a real failure rather than over-expansion

The pass did not merely find more settings. It exposed previously under-modeled system boundaries:

- Enterprise Managed Users is a distinct account/identity lifecycle controlled by an IdP.
- SAML/OIDC/SCIM form an enterprise authentication/provisioning plane, not just alternative login buttons.
- Repository policies in current Enterprise Cloud govern repository **container lifecycle** (creation/deletion/transfer/naming/visibility) and are semantically distinct from code rulesets.
- IP allow lists and hosted-compute private networking add a network trust/policy axis that constrains Actions and resource access.
- SSH certificate authorities add a Git transport authentication lifecycle beyond static SSH keys.

These affect the universal GitHub architecture even though they are not applicable to the current personal-account `flawless-ftxp` repository.

## SAT-MAX

```text
zero-material-novelty pass 1: FAIL
consecutive zero passes: 0
SAT-MAX: RESET
```

## Next attempt

Regress these candidates into the access/policy/trust model, then run another independent traversal focused on deployment models and hosted-vs-self-managed boundaries: GitHub.com, Enterprise Cloud data residency/GHE.com, Enterprise Server, GitHub Connect, Actions runner ownership, API host differences, backup/restore and upgrade lifecycle.
