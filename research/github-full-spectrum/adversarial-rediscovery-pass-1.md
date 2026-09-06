# Adversarial Rediscovery Pass 1

**Execution:** `GHFS-2026-09-06-001`  
**Mode:** independent omission-seeking  
**Result:** **MATERIAL NOVELTY FOUND**

## Search strategy

Instead of following the existing domain tree, this pass searched for GitHub capabilities that frequently sit outside ordinary repository documentation: organization metadata/governance, supply-chain provenance, account-wide settings, Gists, vulnerability intake, new agentic surfaces, and products in transition or retirement.

## Material omissions discovered

1. **Repository custom properties** — structured organization metadata with ruleset targeting implications.
2. **Security configurations** — organization-scale collections of security enablement settings with managed repository relationships.
3. **Artifact attestations** — cryptographic build provenance and integrity claims, with CLI/API verification.
4. **Gists** — a separate Git-backed GitHub content subsystem, not merely a code snippet UI.
5. **Private vulnerability reporting** — public-repository structured private disclosure flow, distinct from `SECURITY.md`.
6. **Personal account surfaces** — settings/accessibility/account lifecycle belong in the full platform model even when not repository configuration.
7. **GitHub Models** — must be represented as **retired**, not current; fully retired July 30, 2026.
8. **GitHub Spark** — must be represented as **sunsetting**; no new users/apps from August 4, 2026.
9. **Agent management/session surfaces** — current Agents UI, session logs, steering, history and enterprise AI Controls.
10. **Third-party coding agents** — current public-preview GitHub workflow for agents including Claude and OpenAI Codex.
11. **Agent apps** — public-preview GitHub App specialization that exposes partner agents via issues, PRs, Agents UI and Mobile.
12. **Copilot automations** — scheduled/event-driven cloud-agent tasks with repository/event security constraints.
13. **GitHub Agentic Workflows** — public-preview natural-language workflows compiled to hardened GitHub Actions.
14. **Copilot plugins/hooks/skills/custom instruction hierarchy** — distinct repository/personal/organization extension artifacts and lifecycle hooks.
15. **Copilot sandboxes, OpenTelemetry and usage metrics** — trust, observability and governance dimensions absent from the initial seed.

## Target-specific impact

Most organization- and enterprise-scale discoveries are not directly applicable to `flawless-ftxp` because it is a personal-account repository. They remain mandatory in the **reference architecture** but must be filtered out of the target implementation.

Two discoveries are directly relevant to the target audit:

- private vulnerability reporting should be evaluated alongside a future `SECURITY.md`;
- release/provenance architecture should explicitly distinguish release immutability from artifact attestations, which are currently not justified because FTXP does not build a distributable binary/container artifact.

The agentic discoveries do **not** justify adding Copilot files, plugins, skills or agentic workflows to FTXP. They demonstrate why GitHub's current platform architecture needs a richer agentic domain and client/policy model.

## Saturation consequence

Because this independent pass discovered multiple new material classes:

```text
SAT-MAX PASS 1 = FAIL / RESET
material_novelty = HIGH
```

The candidates must be normalized, deduplicated and regressed into the reference architecture before a new zero-material-novelty pass can begin.

## Next step

Run a second adversarial pass focused on **platform subsystems and edge lifecycle classes not centered on repositories**: Packages/registries, Pages/custom domains, Sponsors/Education/Support, migrations/import/export, Git LFS/large-file limits, search/command palette, audit/status/service availability, account/org/enterprise deletion/transfer, and API/runtime quota boundaries.
