"""Smoke test: every example script under examples/ runs to completion."""

import subprocess
import sys
from pathlib import Path

import pytest

EXAMPLES = sorted(Path(__file__).resolve().parents[2].joinpath("examples").glob("*.py"))


@pytest.fixture(params=EXAMPLES, ids=lambda p: p.name)
def example_run_result(request, tmp_path):
    # Arrange
    ex = request.param
    # Act
    result = subprocess.run(
        [sys.executable, str(ex)],
        cwd=tmp_path,
        capture_output=True,
        text=True,
        timeout=120,
    )
    return ex, result


def test_examples_directory_is_non_empty():
    # Arrange
    # Act
    found = list(EXAMPLES)
    # Assert
    assert found, "No example scripts found under examples/"


def test_example_script_exits_successfully(example_run_result):
    # Arrange
    ex, r = example_run_result
    # Act
    rc = r.returncode
    # Assert
    assert rc == 0, f"{ex.name} failed:\nSTDOUT:\n{r.stdout}\nSTDERR:\n{r.stderr}"
