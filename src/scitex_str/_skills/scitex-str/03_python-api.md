---
description: |
  [TOPIC] scitex-str Python API
  [DETAILS] Public callables grouped by theme — console, LaTeX safety, plot text formatting, search/parse, misc utilities.
tags: [scitex-str-python-api]
---

# Python API

## Imports

```python
from scitex_str import (
    # Console
    printc, color_text, ct, print_debug, remove_ansi,
    # LaTeX
    to_latex_style, safe_to_latex_style, latex_style,
    add_hat_in_latex_style, hat_latex_style, safe_add_hat_in_latex_style,
    # LaTeX fallback
    latex_to_mathtext, latex_to_unicode, safe_latex_render,
    check_latex_capability, get_latex_status,
    enable_latex_fallback, disable_latex_fallback,
    get_fallback_mode, set_fallback_mode, reset_latex_cache,
    LaTeXFallbackError, latex_fallback_decorator,
    # Plot text
    format_axis_label, format_plot_text, format_title,
    axis_label, title, scientific_text, check_unit_consistency,
    factor_out_digits, auto_factor_axis, smart_tick_formatter,
    # Search / parse
    grep, search, parse, replace,
    # Misc
    clean_path, decapitalize, mask_api,
    readable_bytes, squeeze_spaces, title_case,
)
```

## Console

| Symbol | Purpose |
|---|---|
| `printc(msg, c=...)` | Boxed colored print |
| `color_text(msg, c=...)` / `ct` | Wrap text in ANSI color codes |
| `print_debug(...)` | Debug-only print honoring env-var gate |
| `remove_ansi(s)` | Strip ANSI escape codes |

## LaTeX styling

`to_latex_style`, `latex_style`, `add_hat_in_latex_style`,
`hat_latex_style`, plus `safe_*` variants that defer to the fallback
chain.

## LaTeX fallback

`latex_to_mathtext` and `latex_to_unicode` convert LaTeX to forms that
render without a TeX install. `safe_latex_render` picks the best mode
based on `check_latex_capability()`. `latex_fallback_decorator` wraps a
function so its output is auto-converted.

## Plot text formatting

`format_axis_label`, `format_title`, `axis_label`, `title`,
`format_plot_text`, `scientific_text`, `check_unit_consistency`,
plus tick-label helpers `factor_out_digits`, `auto_factor_axis`,
`smart_tick_formatter`.

## Search / parse

`grep` (ripgrep-style on a list of lines), `search` (return first
group), `parse` (named groups), `replace` (regex replace with helpers).

## Misc

| Symbol | Purpose |
|---|---|
| `clean_path(p)` | Normalize a path string |
| `decapitalize(s)` | Lower the first letter |
| `mask_api(key)` | Mask all but a few chars of an API key |
| `readable_bytes(n)` | "1.2 MB" formatting |
| `squeeze_spaces(s)` | Collapse runs of whitespace |
| `title_case(s)` | Title-case respecting acronyms |

## Two import paths

```python
import scitex_str        # standalone
import scitex.str        # umbrella (requires `pip install scitex`)
```
