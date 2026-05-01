# SciTeX Str (`scitex-str`)

<!-- scitex-badges:start -->
[![PyPI](https://img.shields.io/pypi/v/scitex-str.svg)](https://pypi.org/project/scitex-str/)
[![Python](https://img.shields.io/pypi/pyversions/scitex-str.svg)](https://pypi.org/project/scitex-str/)
[![Tests](https://github.com/ywatanabe1989/scitex-str/actions/workflows/test.yml/badge.svg)](https://github.com/ywatanabe1989/scitex-str/actions/workflows/test.yml)
[![Install Test](https://github.com/ywatanabe1989/scitex-str/actions/workflows/install-test.yml/badge.svg)](https://github.com/ywatanabe1989/scitex-str/actions/workflows/install-test.yml)
[![Coverage](https://codecov.io/gh/ywatanabe1989/scitex-str/graph/badge.svg)](https://codecov.io/gh/ywatanabe1989/scitex-str)
[![Docs](https://readthedocs.org/projects/scitex-str/badge/?version=latest)](https://scitex-str.readthedocs.io/en/latest/)
[![License: AGPL v3](https://img.shields.io/badge/license-AGPL_v3-blue.svg)](https://www.gnu.org/licenses/agpl-3.0)
<!-- scitex-badges:end -->

<p align="center">
  <a href="https://scitex.ai">
    <img src="docs/scitex-logo-blue-cropped.png" alt="SciTeX" width="400">
  </a>
</p>

<p align="center"><b>Text processing utilities for scientific workflows.</b></p>

<p align="center">
  <a href="https://scitex-str.readthedocs.io/">Full Documentation</a> · <code>pip install scitex-str</code>
</p>

---

## Problem and Solution

| # | Problem | Solution |
|---|---------|----------|
| 1 | **LaTeX labels crash matplotlib when TeX isn't installed** — CI runners, laptops without MacTeX, Colab without `!apt install texlive` all fail | **`safe_latex_render(s)`** — auto-detects LaTeX; falls back to mathtext then unicode silently |
| 2 | **ANSI color codes + grep/parse sprinkled as ad-hoc `re` patterns** — each script reinvents the wheel | **Grab-bag of helpers** — `printc`, `color_text`, `grep`, `parse`, `replace`, `mask_api`, `readable_bytes` — boring but consistent across 33 packages |

## Installation

Requires Python >= 3.10.

```bash
pip install scitex-str
```

## Quick Start

```python
import scitex_str as ss

ss.to_latex_style("theta")        # r"$\theta$"
ss.printc("Success!", color="green")
ss.parse("./data/Patient_23/Hour_12", "./data/Patient_{id}/Hour_{hour}")
ss.readable_bytes(1_500_000)      # "1.43 MB"
```

## 1 Interfaces

<details>
<summary><strong>Python API</strong></summary>

<br>

```python
import scitex_str as ss

# LaTeX-style formatting (with safe fallback)
ss.to_latex_style("theta")              # r"$\theta$"
ss.safe_to_latex_style("unknown")       # "unknown" (no error)

# Colored terminal output
ss.printc("Success!", color="green")
ss.ct("Warning", color="yellow")        # returns colored string

# Parse structured paths
ss.parse("./data/Patient_23/Hour_12",
         "./data/Patient_{id}/Hour_{hour}")  # {'id': 23, 'hour': 12}

# Plot text formatting
ss.format_plot_text("amplitude_mv")     # "Amplitude [mV]"

# Numeric formatting
ss.readable_bytes(1_500_000)            # "1.43 MB"
ss.factor_out_digits([1000, 2000, 3000])

# Misc
ss.grep(pattern, lines)
ss.search(...)
ss.replace(...)
ss.mask_api_key("sk-...")
ss.remove_ansi(text)
ss.squeeze_space("a  b   c")            # "a b c"
ss.title_case("hello world")
ss.decapitalize("Hello")
```

</details>

## Part of SciTeX

`scitex-str` is part of [**SciTeX**](https://scitex.ai). Install via
the umbrella with `pip install scitex[str]` to use as
`scitex.str` (Python).

>Four Freedoms for Research
>
>0. The freedom to **run** your research anywhere — your machine, your terms.
>1. The freedom to **study** how every step works — from raw data to final manuscript.
>2. The freedom to **redistribute** your workflows, not just your papers.
>3. The freedom to **modify** any module and share improvements with the community.
>
>AGPL-3.0 — because we believe research infrastructure deserves the same freedoms as the software it runs on.

## License

AGPL-3.0-only.

---

<p align="center">
  <a href="https://scitex.ai" target="_blank"><img src="docs/scitex-icon-navy-inverted.png" alt="SciTeX" width="40"/></a>
</p>
