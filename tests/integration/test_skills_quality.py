"""Enforces SciTeX skills quality checklist §1–§4."""
from pathlib import Path
from scitex_dev._skills_quality_pytest import make_skill_quality_tests

# PS-206b: import-smoke-allowed — the assertions live inside the generated
# test function; this module only wires the package root into the factory.
test_skills_quality = make_skill_quality_tests(
    package_root=Path(__file__).resolve().parents[1]
)
