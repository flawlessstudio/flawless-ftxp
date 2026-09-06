# Adversarial Rediscovery Pass 5

**Execution:** `GHFS-2026-09-06-001`  
**Mode:** repository metadata, deployment, observability and temporal-correction rediscovery  
**Result:** **MATERIAL NOVELTY FOUND**

## Search axis

This pass avoided the agentic/client axis and instead traversed repository graphs/insights, deployments/environments, ruleset observability, community products, notification lifecycle and the late-August/early-September 2026 GitHub Changelog.

## Findings

### Material temporal corrections

1. **GitHub Classroom is decommissioned/deprecated as of 2026-08-28.** Its website, APIs and related services are decommissioned. Any earlier representation of Classroom as a current education product must be corrected to a retired/deprecated temporal state while preserving remaining user/repository/organization artifacts separately.
2. **Actions retention semantics are scheduled to expand on 2026-10-01** so the Actions retention setting governs checks, workflow runs and statuses in addition to artifacts/logs. This is announced future state and must not be applied to the 2026-09-06 current-state model, but it materially extends the temporal/retention relationship graph.
3. **Custom thread subscription deprecation was paused on 2026-08-14.** The `Customize` option remains available. A source that only reads the original 2026-08-10 deprecation announcement would produce a false current-state classification.

### Structural additions that fit existing classes

- **Rule insights dashboard** is now generally available at repository and organization levels. It exposes allowed/failed/bypassed ruleset evaluations, bypass actors, filters, drill-down and CSV export. This is an observability occurrence over the existing ruleset/governance model, not a new governance primitive.
- **Deployment environments** have a distinct state/gate lifecycle: branch/tag eligibility, wait timers, required reviewers, optional prevention of self-review, admin bypass policy, environment secrets/variables and GitHub-App-based custom deployment protection rules. These fit the existing environment/deployment/policy/trust-boundary classes and make their state machine more explicit.
- Repository **graphs/insights** expose traffic, contributors, commits, dependency/network/fork information and belong in the observability surface registry.
- The new privacy-safe **star history REST API** exposes historical star-count data without stargazer identities. It is an API/observability occurrence over an existing star/repository-social concept rather than a new entity family.

## Canonicalization consequence

The temporal registry must distinguish at least:

```text
CURRENT
ANNOUNCED_FUTURE
PUBLIC_PREVIEW
DEPRECATED
DECOMMISSIONED
RETIRED
DEPRECATION_PAUSED
```

and evidence precedence must allow a later changelog update to override an earlier deprecation announcement.

Deployment modeling should explicitly connect:

```text
environment
→ protection rules
→ approval/bypass state
→ secrets availability
→ workflow job dispatch
→ deployment status/history
```

without turning deployment infrastructure into an FTXP repository requirement.

## Target impact on `flawless-ftxp`

No deployment environment is justified for this spec-first repository because it currently deploys no application/service. Rule insights becomes relevant only after a ruleset is actually applied. Repository graphs and star-history APIs are informational, not conformance requirements.

The material impact is primarily on **reference accuracy and temporal evidence discipline**, not target implementation.

## Saturation status

```text
material novelty: LOW-MEDIUM (temporal corrections + lifecycle refinement)
zero-material pass: NOT ACHIEVED
consecutive zero passes: 0 / 2
SAT-MAX: NOT READY
```

## Evidence

- GitHub Changelog: GitHub Classroom deprecated (2026-08-27; effective 2026-08-28)
- GitHub Changelog: Actions retention will cover checks, workflow runs, and statuses (2026-08-27; future effective date 2026-10-01)
- GitHub Changelog: Custom thread subscriptions are being deprecated — updated 2026-08-14 to pause the deprecation
- GitHub Changelog: Rule insights dashboard generally available (2026-08-25)
- GitHub Docs: Deployments and environments / Managing environments / Reviewing deployments
- GitHub Docs: About repository graphs
- GitHub Changelog: privacy-safe star history REST endpoint (2026-09-04)

## Next stage

Integrate the temporal corrections. The next independent pass should focus on package/release/supply-chain and API/schema change boundaries, while applying a stricter materiality rule: subfeatures that fit existing entity/facet/state/relationship classes do **not** reset SAT-MAX unless they invalidate a current classification or require a new architecture dimension.