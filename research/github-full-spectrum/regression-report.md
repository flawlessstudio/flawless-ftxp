# GHFS Full Regression Report

**Execution:** `GHFS-2026-09-06-001`  
**Protocol/profile:** FTXP v1.0.0 / FT-X  
**Evidence horizon:** 2026-09-06  
**Result:** **PASS**

## Scope of regression

Regression was run after all discovery, adversarial and late-novelty integrations. It covers the derived Git + GitHub reference model, not a reopening of FTXP v1.0 normative semantics.

The regression checked:

- required execution/discovery/adversarial/SAT-MAX artifacts;
- canonical research registry presence;
- canonical ID uniqueness across research registries;
- feature-family → domain referential integrity;
- registry evidence-ID resolution against the source registry;
- late-discovery promotion of Copilot app, github.dev, Agent Finder, MCP Registry/ARD, Code Quality and temporal corrections;
- temporal distinction between current, preview, announced-future, deprecation-paused, decommissioned, sunsetting and retired states;
- presence and integrity of the two consecutive zero-material-novelty passes;
- preservation of the target repository's non-frozen conformance state;
- preservation of the single-owner review constraint and evidence horizon.

## Executed validation

GitHub Actions run: `34022607305`  
Job: `validate` / `101457809123`  
Conclusion: `success`

Observed validator output:

```text
PASS: FTXP repository structural baseline is internally consistent.
PASS: GHFS research regression is structurally consistent across 36 registries.
PASS: 600 canonical research IDs are unique and referenced domain/evidence IDs resolve.
PASS: two consecutive zero-material-novelty passes are recorded; SAT-MAX discovery condition may proceed to final report.
```

The workflow retained least privilege (`contents: read`) and used `actions/checkout` pinned to a full commit SHA.

## Late-novelty integration

The final integration promoted materially distinct late candidates into canonical derived registries rather than leaving them only in adversarial notes:

- client model: GitHub Copilot app, github.dev;
- agentic model: Agent Finder, MCP Registry, Agentic Resource Discovery;
- product model: GitHub Code Quality and temporal GitHub Classroom state;
- temporal model: announced-future vs current, deprecation pause, decommissioning;
- retention model: browser-local github.dev state, Classroom decommission data, future Actions retention;
- feature families: Code Quality, agentic discovery, modern client parity, stacked PRs, deployment gates, rule insights;
- evidence registry: current official sources for the promoted candidates.

## Regression findings

### No material contradiction introduced

The late promotions are representable by existing top-level dimensions. No new macro-dimension was required after the two zero-material-novelty passes.

### Git/GitHub boundary preserved

Git objects/refs/operations remain separate from GitHub products, surfaces, policies, clients and programmatic interfaces.

### Concept/occurrence boundary preserved

New UI/API/client appearances are treated as occurrences or interfaces unless they introduce a materially distinct capability/product/entity.

### Temporal integrity strengthened

Later evidence can supersede earlier deprecation announcements. Future changes are retained as future evidence and are not projected backward into the 2026-09-06 current-state model.

### Target applicability remains filtered

The global reference universe does not force implementation in `flawless-ftxp`. Paid/enterprise/agentic/deployment capabilities remain NOT_APPLICABLE or OPTIONAL unless a real target requirement exists.

## Residual unknown space

The regression intentionally retains, rather than fabricates answers for:

- repository security-setting state not exposed by the current connector;
- complete GitHub App installation/effective-permission inventory;
- tenant/private/feature-flag contexts outside the evidence horizon;
- future product changes after 2026-09-06;
- the human licensing decision.

These are not taxonomy gaps. They are explicit access, temporal or human-decision boundaries.

## Result

```text
structural regression ........ PASS
ID uniqueness ................ PASS
referential integrity ........ PASS
late novelty integration ..... PASS
Git/GitHub boundary .......... PASS
concept/occurrence boundary .. PASS
temporal classification ...... PASS
SAT-MAX prerequisites ........ PASS
target repository freeze ..... NOT READY
```

The reference-discovery layer may proceed to the SAT-MAX report. Target remediation remains a separate downstream phase.