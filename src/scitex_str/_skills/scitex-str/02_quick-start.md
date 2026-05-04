---
description: |
  [TOPIC] scitex-str Quick start
  [DETAILS] Smallest examples for colored print, LaTeX-with-fallback, and axis-label formatting.
tags: [scitex-str-quick-start]
---

# Quick Start

## Colored / boxed console output

```python
from scitex_str import printc, color_text

printc("Saved 42 rows", c="green")           # boxed, colored
print(color_text("warning", c="yellow"))     # inline ANSI
```

## LaTeX with safe fallback

```python
from scitex_str import to_latex_style, latex_to_mathtext

label = to_latex_style("alpha")              # -> r"$\alpha$"
mathtext = latex_to_mathtext(r"$\alpha_{i}$") # mathtext-safe form
```

If a TeX install is missing, `safe_latex_render` automatically falls
back to mathtext or unicode — your script keeps working.

## Format an axis label with units

```python
from scitex_str import format_axis_label

label = format_axis_label("Voltage", unit="mV")
# "Voltage (mV)"
```

## Grep-style helpers

```python
from scitex_str import grep, search, parse, replace

matches = grep(r"^ERROR", lines)
hit     = search(r"v(\d+)", "release v42")    # -> "42"
```

## Mask secrets in logs

```python
from scitex_str import mask_api

safe = mask_api("sk-1234567890abcdef")        # "sk-1234***cdef"
```

## Next

- [03_python-api.md](03_python-api.md) — grouped public surface
- [SKILL.md](SKILL.md) — themes overview
