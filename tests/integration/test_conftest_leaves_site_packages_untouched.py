"""Regression: importing tests/conftest.py must not touch site-packages or env."""

from __future__ import annotations

import subprocess
import sys
import textwrap
from pathlib import Path


def test_conftest_leaves_site_packages_and_coverage_env_untouched(tmp_path):
    # Arrange
    conftest = Path(__file__).resolve().parents[1] / "conftest.py"
    child = textwrap.dedent(
        f"""\
        import runpy
        import site

        def snapshot():
            names = set()
            for d in site.getsitepackages() + [site.getusersitepackages()]:
                try:
                    import os
                    names.update((d, n) for n in os.listdir(d))
                except OSError:
                    continue
            return names

        before = snapshot()
        import os
        os.environ["COVERAGE_PROCESS_START"] = "sentinel-start"
        os.environ["COVERAGE_FILE"] = "sentinel-file"
        runpy.run_path({str(conftest)!r})
        after = snapshot()
        assert before == after, sorted(after - before)
        assert os.environ["COVERAGE_PROCESS_START"] == "sentinel-start"
        assert os.environ["COVERAGE_FILE"] == "sentinel-file"
        """
    )
    # Act
    proc = subprocess.run(
        [sys.executable, "-c", child],
        capture_output=True,
        text=True,
        cwd=tmp_path,
    )
    # Assert
    assert proc.returncode == 0, proc.stderr + proc.stdout
