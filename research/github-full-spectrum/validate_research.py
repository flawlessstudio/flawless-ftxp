#!/usr/bin/env python3
"""Zero-dependency structural regression validator for GHFS research artifacts."""

from __future__ import annotations

import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
WORK = ROOT / "research" / "github-full-spectrum"
REGISTRIES = WORK / "registries"

REQUIRED = [
    "execution-manifest.yaml",
    "source-registry.yaml",
    "gap-register.yaml",
    "pre-execution-readiness.md",
    "discovery-pass-1.md",
    "discovery-pass-2.md",
    "discovery-pass-3.md",
    "discovery-pass-4.md",
    "discovery-pass-5.md",
    "discovery-pass-6.md",
    "adversarial-rediscovery-pass-1.md",
    "adversarial-rediscovery-pass-2.md",
    "adversarial-rediscovery-pass-3.md",
    "adversarial-rediscovery-pass-4.md",
    "adversarial-rediscovery-pass-5.md",
    "zero-material-novelty-pass-1.md",
    "zero-material-novelty-pass-2.md",
    "applicability-matrix.yaml",
    "conformance-matrix.yaml",
    "target-architecture.md",
    "lifecycle-test-plan.md",
    "remediation-dependency-graph.md",
]

CORE_REGISTRIES = [
    "domain-registry.yaml",
    "feature-family-registry.yaml",
    "product-interface-registry.yaml",
    "entity-registry.yaml",
    "access-role-permission-registry.yaml",
    "repository-lifecycle-registry.yaml",
    "repository-surface-registry.yaml",
    "repository-setting-registry.yaml",
    "navigation-occurrence-registry.yaml",
    "action-registry.yaml",
    "state-registry.yaml",
    "route-registry.yaml",
    "programmatic-interface-registry.yaml",
    "event-webhook-registry.yaml",
    "notification-registry.yaml",
    "security-control-registry.yaml",
    "governance-control-registry.yaml",
    "policy-inheritance-registry.yaml",
    "agentic-capability-registry.yaml",
    "client-parity-registry.yaml",
    "temporal-product-registry.yaml",
    "data-retention-delivery-registry.yaml",
    "supply-chain-provenance-registry.yaml",
    "storage-limit-migration-registry.yaml",
    "deployment-model-registry.yaml",
]

ID_LINE = re.compile(r"^\s*-\s+id:\s*([A-Za-z0-9_.-]+)\s*$", re.MULTILINE)
ID_INLINE = re.compile(r"\{id:\s*([A-Za-z0-9_.-]+)")
SOURCE_REF = re.compile(r"\b(?:GIT-S|GH-S|LIVE-R)\d+\b")
DOMAIN_REF = re.compile(r"\bdomain:\s*(GH-D\d+)\b")


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    raise SystemExit(1)


def text(path: pathlib.Path) -> str:
    return path.read_text(encoding="utf-8")


def ids(body: str) -> list[str]:
    return ID_LINE.findall(body) + ID_INLINE.findall(body)


def main() -> int:
    missing = [name for name in REQUIRED if not (WORK / name).is_file()]
    missing += [f"registries/{name}" for name in CORE_REGISTRIES if not (REGISTRIES / name).is_file()]
    if missing:
        fail("missing required GHFS artifacts: " + ", ".join(missing))

    # Canonical-registry identifiers must be unique across the research model.
    seen: dict[str, str] = {}
    for path in sorted(REGISTRIES.glob("*.yaml")):
        body = text(path)
        local = ids(body)
        if len(local) != len(set(local)):
            fail(f"duplicate ID inside {path.name}")
        for item in local:
            if item in seen:
                fail(f"canonical ID {item!r} occurs in both {seen[item]} and {path.name}")
            seen[item] = path.name

    domain_body = text(REGISTRIES / "domain-registry.yaml")
    domain_ids = set(ids(domain_body))
    feature_body = text(REGISTRIES / "feature-family-registry.yaml")
    unresolved_domains = sorted(set(DOMAIN_REF.findall(feature_body)) - domain_ids)
    if unresolved_domains:
        fail("feature-family domain references do not resolve: " + ", ".join(unresolved_domains))

    source_body = text(WORK / "source-registry.yaml")
    source_ids = set(ids(source_body))
    missing_expected_sources = [f"GH-S{i:03d}" for i in range(23, 35) if f"GH-S{i:03d}" not in source_ids]
    if missing_expected_sources:
        fail("late-discovery evidence sources were not integrated: " + ", ".join(missing_expected_sources))

    unresolved_source_refs: dict[str, list[str]] = {}
    for path in sorted(REGISTRIES.glob("*.yaml")):
        refs = set(SOURCE_REF.findall(text(path)))
        missing_refs = sorted(refs - source_ids)
        if missing_refs:
            unresolved_source_refs[path.name] = missing_refs
    if unresolved_source_refs:
        fail("unresolved evidence IDs: " + repr(unresolved_source_refs))

    temporal = text(REGISTRIES / "temporal-product-registry.yaml")
    for marker in ["ANNOUNCED_FUTURE", "DEPRECATION_PAUSED", "DECOMMISSIONED", "GitHub Classroom", "GitHub Code Quality", "github.dev"]:
        if marker not in temporal:
            fail(f"temporal registry missing regression marker: {marker}")

    agentic = text(REGISTRIES / "agentic-capability-registry.yaml")
    for marker in ["GitHub Copilot app", "Agent Finder", "MCP Registry", "Agentic Resource Discovery"]:
        if marker not in agentic:
            fail(f"agentic registry missing regression marker: {marker}")

    clients = text(REGISTRIES / "client-parity-registry.yaml")
    for marker in ["GitHub Copilot app", "github.dev", "Codespaces"]:
        if marker not in clients:
            fail(f"client registry missing regression marker: {marker}")

    products = text(REGISTRIES / "product-interface-registry.yaml")
    for marker in ["GitHub Code Quality", "GitHub Classroom", "Agent Finder", "MCP Registry"]:
        if marker not in products:
            fail(f"product/interface registry missing regression marker: {marker}")

    zero1 = text(WORK / "zero-material-novelty-pass-1.md")
    zero2 = text(WORK / "zero-material-novelty-pass-2.md")
    if "ZERO MATERIAL NOVELTY" not in zero1 or "1 / 2" not in zero1:
        fail("first SAT-MAX zero-material pass is not validly recorded")
    if "ZERO MATERIAL NOVELTY" not in zero2 or "2 / 2" not in zero2:
        fail("second SAT-MAX zero-material pass is not validly recorded")

    conformance = text(WORK / "conformance-matrix.yaml")
    if "freeze_ready: false" not in conformance:
        fail("target conformance must remain non-frozen until remediation closes")

    target = text(WORK / "target-architecture.md")
    if "mandatory approval count: 0" not in target:
        fail("single-owner review constraint is missing from target architecture")

    manifest = text(WORK / "execution-manifest.yaml")
    if "evidence_horizon:" not in manifest or "date: 2026-09-06" not in manifest:
        fail("execution evidence horizon is missing or changed unexpectedly")

    print(f"PASS: GHFS research regression is structurally consistent across {len(list(REGISTRIES.glob('*.yaml')))} registries.")
    print(f"PASS: {len(seen)} canonical research IDs are unique and referenced domain/evidence IDs resolve.")
    print("PASS: two consecutive zero-material-novelty passes are recorded; SAT-MAX discovery condition may proceed to final report.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
