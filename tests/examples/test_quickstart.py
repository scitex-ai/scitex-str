#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""End-to-end execution test for examples/quickstart.py.

Per scitex-dev PS303 every example must have a matching test under
`tests/examples/`. The meaningful contract: the example **runs**
without raising. Tests that only check `Path.exists()` or `py_compile`
are theater — they pass even when the example imports a removed
symbol or asserts on stale behaviour. We invoke the example in a
real subprocess against the installed `scitex_str`.
"""

import subprocess
import sys
from pathlib import Path

EXAMPLE = Path(__file__).resolve().parents[2] / "examples" / "quickstart.py"


def test_quickstart_runs_end_to_end_without_raising():
    # Arrange
    cmd = [sys.executable, str(EXAMPLE)]
    # Act
    result = subprocess.run(cmd, check=False, capture_output=True, timeout=30)
    # Assert
    assert result.returncode == 0, (
        f"example exited {result.returncode}\n"
        f"stdout:\n{result.stdout.decode(errors='replace')}\n"
        f"stderr:\n{result.stderr.decode(errors='replace')}"
    )


def test_quickstart_prints_readable_bytes_marker():
    """The example's print statements are part of its public contract —
    they exercise the documented API. Asserting on the marker catches
    accidental rename / removal of `readable_bytes`."""
    # Arrange
    cmd = [sys.executable, str(EXAMPLE)]
    # Act
    result = subprocess.run(cmd, check=False, capture_output=True, timeout=30)
    stdout = result.stdout.decode(errors="replace")
    # Assert
    assert "readable_bytes(1500):" in stdout


def test_quickstart_prints_squeeze_spaces_marker():
    # Arrange
    cmd = [sys.executable, str(EXAMPLE)]
    # Act
    result = subprocess.run(cmd, check=False, capture_output=True, timeout=30)
    stdout = result.stdout.decode(errors="replace")
    # Assert
    assert "squeeze_spaces:" in stdout


def test_quickstart_prints_title_case_marker():
    # Arrange
    cmd = [sys.executable, str(EXAMPLE)]
    # Act
    result = subprocess.run(cmd, check=False, capture_output=True, timeout=30)
    stdout = result.stdout.decode(errors="replace")
    # Assert
    assert "title_case:" in stdout


def test_quickstart_prints_clean_path_marker():
    # Arrange
    cmd = [sys.executable, str(EXAMPLE)]
    # Act
    result = subprocess.run(cmd, check=False, capture_output=True, timeout=30)
    stdout = result.stdout.decode(errors="replace")
    # Assert
    assert "clean_path:" in stdout


# EOF
