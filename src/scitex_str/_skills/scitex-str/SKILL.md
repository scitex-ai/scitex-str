---
name: scitex-str
description: Text-processing utilities for scientific workflows — colored console prints, LaTeX safety/fallbacks, path cleaning, grep/search/parse/replace, and plot-label formatting. Use when formatting scientific text or console output.
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
