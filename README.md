# SciTeX Str (`scitex-str`)

<p align="center">
  <a href="https://scitex.ai">
    <img src="docs/scitex-logo-blue-cropped.png" alt="SciTeX" width="400">
  </a>
</p>

<p align="center"><b>Text processing utilities for scientific workflows.</b></p>

<p align="center">
  <a href="https://scitex-str.readthedocs.io/">Full Documentation</a> · <code>uv pip install scitex-str[all]</code>
</p>

<!-- scitex-badges:start -->
<p align="center">
  <a href="https://pypi.org/project/scitex-str/"><img src="https://img.shields.io/pypi/v/scitex-str?label=pypi" alt="pypi"></a>
  <a href="https://pypi.org/project/scitex-str/"><img src="https://img.shields.io/pypi/pyversions/scitex-str?label=python" alt="python"></a>
  <a href="https://scitex-str.readthedocs.io/en/latest/"><img src="https://img.shields.io/github/actions/workflow/status/ywatanabe1989/scitex-str/ci.yml?branch=develop&label=docs" alt="docs"></a>
  <a href="https://scitex-str.readthedocs.io/en/latest/"><img src="https://img.shields.io/readthedocs/scitex-str?label=docs" alt="docs"></a>
</p>
<p align="center">
  <a href="https://github.com/ywatanabe1989/scitex-str/actions/workflows/ci.yml"><img src="https://img.shields.io/github/actions/workflow/status/ywatanabe1989/scitex-str/ci.yml?branch=develop&label=tests" alt="tests"></a>
  <a href="https://github.com/ywatanabe1989/scitex-str/actions/workflows/ci.yml"><img src="https://img.shields.io/github/actions/workflow/status/ywatanabe1989/scitex-str/ci.yml?branch=develop&label=install-check" alt="install-check"></a>
  <a href="https://github.com/ywatanabe1989/scitex-str/actions/workflows/ci.yml"><img src="https://img.shields.io/github/actions/workflow/status/ywatanabe1989/scitex-str/ci.yml?branch=develop&label=quality" alt="quality"></a>
  <a href="https://codecov.io/gh/ywatanabe1989/scitex-str"><img src="https://img.shields.io/codecov/c/github/ywatanabe1989/scitex-str/develop?label=cov" alt="cov"></a>
</p>
<!-- scitex-badges:end -->

---

## Problem and Solution

| # | Problem | Solution |
|---|---------|----------|
| 1 | **Missing TeX** — CI runners, laptops without MacTeX, Colab without `!apt install texlive` all fail to render labels | **`safe_latex_render(s)`** — auto-detects LaTeX; falls back to mathtext then unicode silently |
| 2 | **Ad-hoc snippets** — ANSI color codes + grep/parse reinvented as one-off `re` patterns in every script | **Helper grab-bag** — `printc`, `color_text`, `grep`, `parse`, `replace`, `mask_api`, `readable_bytes` — boring but consistent across 33 packages |


## Demo

```python
import scitex_str as ss

# 1) LaTeX-safe label rendering — no crash if TeX missing
label = ss.safe_to_latex_style("theta")    # "$\\theta$" or unicode fallback

# 2) Colored terminal status
ss.printc("[ok] tunnel established", color="green")
ss.printc("[warn] retry in 3s",      color="yellow")

# 3) Parse a structured directory
ss.parse("./data/Patient_23/Hour_12",
         "./data/Patient_{id}/Hour_{hour}")  # → {'id': 23, 'hour': 12}

# 4) Human-readable byte size
ss.readable_bytes(1_500_000)               # → "1.43 MB"

# 5) Mask credentials before logging
ss.mask_api_key("sk-abc...7890")     # → "sk-***7890"
```

```mermaid
flowchart LR
    A[Raw value] --> B{kind?}
    B -- bytes --> RB[readable_bytes]
    B -- path --> P[parse]
    B -- math --> L[safe_to_latex_style]
    B -- secret --> M[mask_api_key]
    B -- log line --> PC[printc]
    RB --> O[Pretty output]
    P --> O
    L --> O
    M --> O
    PC --> O
    style O fill:#27ae60,stroke:#2c3e50,color:#fff
```

<p align="center"><sub><b>Figure 1.</b> Demo. Pick the helper by what you have, not by where it lives.</sub></p>

## Installation

```bash
uv pip install "scitex-str[all]"
```

Requires Python >= 3.10.

<details>
<summary>Extras</summary>

- `scitex-str[all]` — everything: matplotlib-backed LaTeX rendering / tick formatting, pandas/xarray-aware search inputs.
- `scitex-str[dev]` — maintainer tools (pytest, sphinx).

</details>

## Architecture

```
scitex_str/
├── _latex/                                          # LaTeX rendering with fallback
│   ├── _latex.py / _latex_fallback.py
│   └── ...
├── _ansi/                                           # ANSI color helpers
│   ├── _color_text.py / _remove_ansi.py
│   └── ...
├── _search/                                         # text search & template parse
│   ├── _grep.py / _parse.py / _search.py / _replace.py
│   └── ...
├── _plot/                                           # axis-label formatter
│   ├── _format_plot_text.py / _factor_out_digits.py
│   └── ...
├── _print/                                          # colored / debug console output
│   ├── _printc.py / _print_block.py / _print_debug.py
│   └── ...
├── _mask/                                           # sanitization
│   ├── _mask_api.py / _mask_api_key.py
│   └── ...
├── _case/                                           # case transforms
│   ├── _title_case.py / _decapitalize.py
│   └── ...
├── _readable_bytes.py                               # numeric formatting
├── _clean_path.py                                   # path normalization
├── _squeeze_space.py                                # whitespace collapse
└── ...                                              # ~20 boring helpers, one per file
```

```mermaid
flowchart LR
    LX[LaTeX/mathtext<br/>fallback] --> A[to_latex_style<br/>safe_latex_render]
    ANSI[ANSI tooling] --> B[printc / ct / remove_ansi]
    Tmpl[Template parsing] --> C[parse / grep / search / replace]
    Fmt[Numeric formatting] --> D[readable_bytes<br/>factor_out_digits]
    Plot[Plot text] --> E[format_plot_text]
    Sanit[Sanitization] --> F[mask_api_key]
```

<p align="center"><sub><b>Figure 2.</b> Module layout. Each helper is a single-file leaf — boring on purpose, consistent across 33 ecosystem packages.</sub></p>
## 1 Interfaces

<details open>
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
`scitex.str` (Python) or `scitex str ...` (CLI).

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
