---
name: scitex-str
description: Text-processing utilities for scientific Python — colored/boxed console prints, LaTeX safety with mathtext/unicode fallback, plot-label formatting, and search/parse/replace helpers. Public API — console (`printc`, `color_text`/`ct`, `print_debug`, `remove_ansi`), LaTeX (`to_latex_style`, `safe_to_latex_style`, `add_hat_in_latex_style`, `safe_add_hat_in_latex_style`, `hat_latex_style`, `latex_style`), LaTeX fallback (`check_latex_capability`, `get_latex_status`, `latex_to_mathtext`, `latex_to_unicode`, `safe_latex_render`, `latex_fallback_decorator`, `set_fallback_mode` / `get_fallback_mode`, `enable_latex_fallback` / `disable_latex_fallback`, `reset_latex_cache`, `LaTeXFallbackError`), plot text (`axis_label`, `format_axis_label`, `format_plot_text`, `format_title`, `title`, `scientific_text`, `check_unit_consistency`, `factor_out_digits`, `auto_factor_axis`, `smart_tick_formatter`), parsing/search (`grep`, `search`, `parse`, `replace`), misc (`clean_path`, `decapitalize`, `title_case`, `squeeze_spaces`, `readable_bytes`, `mask_api`). No CLI, no MCP tools. Drop-in replacement for hand-rolling ANSI color codes (colorama), ad-hoc `re` patterns for grep/search in Python, manual `$\hat{x}$` LaTeX wrapping, custom `try/except` blocks around matplotlib LaTeX rendering, and bespoke tick-label digit-factoring (×10⁶) logic. Use whenever the user asks to "print colored text to console", "add a debug print with file/line info", "strip ANSI codes from a log", "render a label as LaTeX with fallback when TeX is missing", "check if LaTeX is available on this system", "format an axis label with units", "factor out common digits from tick labels", "grep lines from a string", "parse a formatted string", "mask an API key for logging", "make bytes human-readable", "convert a filename to title case", or mentions printc, color_text, latex_fallback, scitex.str.
user-invocable: false
---

# scitex-str

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

- [01_quick-start.md](01_quick-start.md) — install, import, a few recipes
- [02_python-api.md](02_python-api.md) — grouped public API

No CLI, no MCP tools.
