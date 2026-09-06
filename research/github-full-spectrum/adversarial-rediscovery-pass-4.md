# Adversarial Rediscovery Pass 4

**Execution:** `GHFS-2026-09-06-001`  
**Mode:** client/agentic/quality-surface rediscovery  
**Result:** **MATERIAL NOVELTY FOUND**

## Search axis

This pass deliberately changed direction again. It searched recent official GitHub documentation and changelog entries for current client surfaces, agentic discovery mechanisms, developer-environment variants and repository quality products that were not guaranteed to appear in repository-governance or enterprise-deployment documentation.

## Material findings

1. **GitHub Copilot app** is a distinct desktop client for agent-driven development, generally available on macOS, Windows and Linux. It manages parallel agent sessions, branches/worktrees, issues, pull requests, diff review, integrated terminal/browser validation, canvases, cloud sessions/automations, MCP-connected tools and PR handoff.
2. **github.dev** is a distinct browser-sandbox development client, currently public preview. It does not clone the repository, stores uncommitted work in browser local storage, lacks Codespaces compute/terminal, and is not equivalent to GitHub.com file editing or Codespaces.
3. **Agent finder** is a capability-discovery layer for GitHub Copilot that searches a registry and ranks MCP servers, tools, agents, skills and related resources. It implements the open **Agentic Resource Discovery (ARD)** specification and does not silently install discovered resources.
4. **MCP Registry** is a registry/discovery surface rather than a mere MCP configuration file. It must be represented separately from an MCP server, MCP client, tool invocation or repository MCP configuration.
5. **GitHub Code Quality** is now a generally available standalone paid product on GitHub Team and Enterprise Cloud. It combines deterministic CodeQL-based quality analysis, pull-request findings, default-branch findings, coverage metrics, Copilot-powered remediation and ruleset-enforced quality/coverage thresholds.
6. Code Quality has its own organization targeting/inheritance controls, repository enablement API, audit events, dedicated Actions actor/path and billing model. Those surfaces make it a product/domain rather than a subsetting label under generic code scanning.
7. GitHub has announced a future Copilot policy convergence no earlier than 2026-09-28 for Copilot on github.com, GitHub Mobile and the cloud agent. This is **temporal policy evidence**, not a current-state replacement as of this execution horizon.

## Canonicalization consequences

The reference architecture must distinguish:

```text
client ≠ feature ≠ agent runtime ≠ registry ≠ discovery protocol ≠ integration
```

and:

```text
code scanning/security analysis ≠ code quality product
```

The client model must contain at least:

- GitHub.com web;
- responsive web;
- GitHub Mobile;
- GitHub Desktop;
- GitHub CLI;
- GitHub Copilot app;
- github.dev;
- Codespaces;
- IDE integrations;
- REST/GraphQL/Git transport clients.

The agentic model must allow:

```text
agent/client
→ registry
→ discovery mechanism
→ ranked capability
→ user/admin policy check
→ explicit connection/installation
→ tool/resource use
```

## Target impact on `flawless-ftxp`

These findings **do not justify adding** the Copilot app, MCP configuration, Agent Finder, Code Quality, Codespaces or github.dev as dependencies of FTXP.

For the current public, personal-account, spec-first repository:

- GitHub Code Quality is not an applicable baseline requirement because the documented product requires GitHub Team or Enterprise Cloud and would add paid/runtime overhead disproportionate to this repository.
- The Copilot app and Agent Finder remain reference-architecture/client discoveries, not repository requirements.
- github.dev is a valid optional authoring client but not a governance or conformance dependency.

## Saturation status

```text
material novelty: MEDIUM
zero-material pass: NOT ACHIEVED
consecutive zero passes: 0 / 2
SAT-MAX: NOT READY
```

## Evidence

Primary/current evidence used in this pass:

- GitHub Docs: About the GitHub Copilot app
- GitHub Changelog: GitHub Copilot app generally available (2026-06-17)
- GitHub Docs: The github.dev web-based editor
- GitHub Changelog: Agent finder for GitHub Copilot now available (2026-06-17)
- GitHub Docs/Changelog: GitHub Code Quality, generally available 2026-07-20
- GitHub Changelog: Code Quality audit events and separate Actions path (2026-08-20)
- GitHub Changelog: upcoming Copilot policy/billing changes (2026-08-28)

## Next stage

Integrate the candidates into the canonical novelty registry, regress the client/product/agentic/temporal models, then run a new independent zero-novelty attempt from a different axis. The next pass should focus on repository metadata/community/release/distribution and account-level surfaces rather than AI/client documentation.