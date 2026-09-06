# Adversarial Rediscovery Pass 2

**Execution:** `GHFS-2026-09-06-001`  
**Mode:** edge lifecycle and non-repository-platform rediscovery  
**Result:** **MATERIAL NOVELTY FOUND**

## Material additions

This pass deliberately avoided the previously dominant repository-governance/security path and searched distribution, storage, migration, service, community and alternative-navigation boundaries.

Material additions:

- GitHub Packages has **two materially different permission models** depending on registry; repository transfer and Actions access therefore cannot be modeled generically.
- Git LFS changes the storage boundary: Git records pointer objects while GitHub-hosted large content is retrieved separately; LFS is also a separate client/program from Git.
- GitHub documents repository/file/branch/directory operational limits that belong in the failure/constraint model.
- GitHub Pages has branch/folder and GitHub Actions publication pipelines with different execution behavior.
- GitHub Enterprise Importer is a first-class migration subsystem that can preserve GitHub metadata beyond raw Git history.
- Organization deletion/archive and personal-to-organization migration add account-scope lifecycle transitions and irreversible boundaries.
- Command Palette is a context-sensitive navigation/search/action surface and is currently public preview; it cannot be reduced to a keyboard shortcut.
- GitHub Support/Status creates an external operational plane with incident subscriptions and a Status API.
- Sponsors, Education/Classroom and Nonprofits are distinct community/program services that belong in the full platform universe even though they are not repository-blueprint requirements.

## Target impact

None of the newly discovered distribution/community programs justify adding implementation to `flawless-ftxp`. The storage/limit model is relevant mainly as a negative applicability result: this text-heavy repository should remain far below large-repository/LFS thresholds.

Command Palette and Support/Status improve full-spectrum surface/operational completeness but do not alter the target repository architecture.

## Saturation consequence

The pass still produced materially distinct classes and lifecycle relations:

```text
SAT-MAX ZERO-NOVELTY PASS = NOT ACHIEVED
```

## Next independent pass

Run a third adversarial pass focused on **residual governance/data planes and current preview/change surfaces**, not broad product categories: custom roles/properties, audit streaming, repository rules/status/checks, attestations/immutable releases, dependency metadata/SBOM, dev-environment lifecycle, Pages/Packages edge state, API/webhook delivery failures, accessibility/localization, and changelog-derived current previews/deprecations.
