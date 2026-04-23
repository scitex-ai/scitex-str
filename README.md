# SciTeX Str (`scitex-str`)

<p align="center"><b>Text processing utilities for scientific workflows</b></p>

<p align="center">
  <a href="https://badge.fury.io/py/scitex-str"><img src="https://badge.fury.io/py/scitex-str.svg" alt="PyPI version"></a>
  <a href="https://github.com/ywatanabe1989/scitex-str/actions/workflows/test.yml"><img src="https://github.com/ywatanabe1989/scitex-str/actions/workflows/test.yml/badge.svg" alt="Tests"></a>
  <a href="https://www.gnu.org/licenses/agpl-3.0"><img src="https://img.shields.io/badge/License-AGPL--3.0-blue.svg" alt="License: AGPL-3.0"></a>
</p>

<p align="center">
  <code>pip install scitex-str</code>
</p>

---

## Problem and Solution


| # | Problem | Solution |
|---|---------|----------|
| 1 | **LaTeX labels crash matplotlib when TeX isn't installed** -- CI runners, laptops without MacTeX, Colab without `!apt install texlive` all fail | **`safe_latex_render(s)`** -- auto-detects LaTeX; falls back to mathtext then unicode silently |
| 2 | **ANSI color codes + grep/parse sprinkled as ad-hoc `re` patterns** -- each script reinvents the wheel | **Grab-bag of helpers** -- `printc`, `color_text`, `grep`, `parse`, `replace`, `mask_api`, `readable_bytes` — boring but consistent across 33 packages |

## Problem

Scientific Python code frequently needs LaTeX-style formatting for axis labels, colored terminal output for debugging, and structured string parsing for file paths and templates. These are scattered across ad-hoc helper functions in every project.

## Solution

scitex-str provides a single package for text utilities commonly needed in scientific workflows:

- **LaTeX formatting** -- convert variable names to LaTeX style, with automatic fallback when LaTeX is unavailable
- **Colored terminal output** -- `printc` and `color_text` for styled console messages
- **String parsing** -- bidirectional `parse()` to extract variables from path patterns
- **Plot text helpers** -- format axis labels, titles, and tick labels for publication figures
- **Numeric formatting** -- factor out common digits, human-readable byte sizes

## Installation

Requires Python >= 3.10.

```bash
pip install scitex-str
```

> **SciTeX users**: `pip install scitex` already includes this. Use `import scitex` then `scitex.str`.

## Quick Start

```python
import scitex_str as ss

# LaTeX-style formatting
ss.to_latex_style("theta")        # r"$\theta$"
ss.safe_to_latex_style("unknown") # "unknown" (no error)

# Colored terminal output
ss.printc("Success!", color="green")
ss.ct("Warning", color="yellow")  # returns colored string

# Parse structured paths
result = ss.parse("./data/Patient_23/Hour_12", "./data/Patient_{id}/Hour_{hour}")
# {'id': 23, 'hour': 12}

# Format plot text
ss.format_plot_text("amplitude_mv")  # "Amplitude [mV]"

# Human-readable bytes
ss.readable_bytes(1_500_000)  # "1.43 MB"
```

## Part of SciTeX

scitex-str is part of [**SciTeX**](https://scitex.ai), a Python framework for scientific research automation.

| Module | Package | Role |
|--------|---------|------|
| `scitex.str` | [scitex-str](https://github.com/ywatanabe1989/scitex-str) | Text processing utilities |
| `scitex.stats` | [scitex-stats](https://github.com/ywatanabe1989/scitex-stats) | Statistical testing |
| `scitex.io` | [scitex-io](https://github.com/ywatanabe1989/scitex-io) | Universal file I/O |
| `scitex.plt` | [figrecipe](https://github.com/ywatanabe1989/figrecipe) | Publication-ready figures |

---

<p align="center">
  <a href="https://scitex.ai" target="_blank">scitex.ai</a>
</p>

<!-- EOF -->
