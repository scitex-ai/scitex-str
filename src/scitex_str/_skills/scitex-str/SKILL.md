---
name: scitex-str
description: |
  [WHAT] Text-processing utilities for scientific Python — colored/boxed console prints, LaTeX safety with mathtext/unicode fallback, plot-label formatting, and grep/search/parse/replace helpers.
  [WHEN] Printing colored or boxed text, rendering LaTeX with fallback when TeX is missing, formatting axis labels with units, factoring digits from tick labels, grepping/parsing strings, or masking API keys.
  [HOW] `from scitex_str import printc, color_text, to_latex_style, latex_to_mathtext, format_axis_label, grep, ...` — pure Python helpers, no shared state.
tags: [scitex-str]
primary_interface: python
interfaces:
  python: 3
  cli: 0
  mcp: 0
  skills: 2
  http: 0
---

# scitex-str

> **Interfaces:** Python ⭐⭐⭐ (primary) · CLI — · MCP — · Skills ⭐⭐ · Hook — · HTTP —

Grab-bag of string helpers used across SciTeX. Three rough themes:

## Installation & import (two equivalent paths)

The same module is reachable via two install paths. Both forms work at
runtime; which one a user has depends on their install choice.

```python
# Standalone — pip install scitex-str
import scitex_str
scitex_str.printc(...)

# Umbrella — pip install scitex
import scitex.str
scitex.str.printc(...)
```

`pip install scitex-str` alone does NOT expose the `scitex` namespace;
`import scitex.str` raises `ModuleNotFoundError`. To use the
`scitex.str` form, also `pip install scitex`.

See [../../general/02_interface-python-api.md] for the ecosystem-wide
rule and empirical verification table.

1. **Console / debugging** — colored prints, block prints, ANSI stripping.
2. **LaTeX safety** — convert to LaTeX, fall back to mathtext/unicode when a
   LaTeX install is absent.
3. **Plot-text formatting** — axis labels, titles, unit checks, digit factoring
   for tick labels.

## Sub-skills

- [01_installation.md](01_installation.md) — pip install + smoke verify
- [02_quick-start.md](02_quick-start.md) — colored print, LaTeX, axis-label snippets
- [03_python-api.md](03_python-api.md) — grouped public API
- [10_quick-start.md](10_quick-start.md) — legacy quick-start (kept for context)
- [11_python-api.md](11_python-api.md) — legacy API notes (kept for context)

No CLI, no MCP tools.
