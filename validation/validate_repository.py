#!/usr/bin/env python3
"""Zero-dependency structural validator for the FTXP repository baseline."""

from __future__ import annotations

import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
EXPECTED_VERSION = "1.0.0"

REQUIRED_FILES = [
    "README.md",
    "CHANGELOG.md",
    "VERSION",
    "spec/FTXP-v1.0.md",
    "spec/terminology.md",
    "spec/conformance.md",
    "kernel/canonical-execution-kernel.md",
    "profiles/FT-L.yaml",
    "profiles/FT-S.yaml",
    "profiles/FT-X.yaml",
    "templates/T1-execution.yaml",
    "templates/T2-record.yaml",
    "templates/T3-run-package.yaml",
    "registries/concept-types.yaml",
    "registries/facets.yaml",
    "registries/relationships.yaml",
    "registries/statuses.yaml",
    "registries/quality-gates.yaml",
    "registries/material-novelty.yaml",
    "registries/reopening-triggers.yaml",
    "schemas/logical-data-model.yaml",
    "validation/sat-max.md",
    "validation/regression.md",
]

REQUIRED_SPEC_TERMS = [
    "Scope integrity",
    "Semantic deduplication",
    "SAT-MAX",
    "G12 Regression",
    "R7 Use-case requirement change",
]


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    raise SystemExit(1)


def main() -> int:
    missing = [path for path in REQUIRED_FILES if not (ROOT / path).is_file()]
    if missing:
        fail("missing required files: " + ", ".join(missing))

    version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
    if version != EXPECTED_VERSION:
        fail(f"VERSION is {version!r}; expected {EXPECTED_VERSION!r}")

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    if f"FTXP v{EXPECTED_VERSION}" not in readme:
        fail("README does not identify the canonical protocol version")

    spec = (ROOT / "spec/FTXP-v1.0.md").read_text(encoding="utf-8")
    for term in REQUIRED_SPEC_TERMS:
        if term not in spec:
            fail(f"normative specification is missing required term: {term}")

    gates = (ROOT / "registries/quality-gates.yaml").read_text(encoding="utf-8")
    gate_ids = re.findall(r"^\s*- id: (G\d+)\s*$", gates, flags=re.MULTILINE)
    expected_gates = [f"G{i}" for i in range(13)]
    if gate_ids != expected_gates:
        fail(f"quality gate IDs are {gate_ids!r}; expected {expected_gates!r}")

    facets = (ROOT / "registries/facets.yaml").read_text(encoding="utf-8")
    facet_ids = re.findall(r"^\s*- id: (F\d+)\s*$", facets, flags=re.MULTILINE)
    expected_facets = [f"F{i:02d}" for i in range(1, 24)]
    if facet_ids != expected_facets:
        fail("facet registry must contain F01–F23 exactly once and in canonical order")

    reopen = (ROOT / "registries/reopening-triggers.yaml").read_text(encoding="utf-8")
    reopening_ids = re.findall(r"^\s*- id: (R\d+)\s*$", reopen, flags=re.MULTILINE)
    expected_reopening = [f"R{i}" for i in range(1, 8)]
    if reopening_ids != expected_reopening:
        fail("reopening registry must contain R1–R7 exactly once and in canonical order")

    profile_s = (ROOT / "profiles/FT-S.yaml").read_text(encoding="utf-8")
    if "profile: FT-S" not in profile_s or "adversarial_pass: required" not in profile_s:
        fail("FT-S default profile is malformed")

    print("PASS: FTXP repository structural baseline is internally consistent.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
