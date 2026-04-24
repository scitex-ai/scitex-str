<!-- 02_python-api.md -->

# scitex-str — Python API

Everything below is exported from `scitex_str.__all__`.

## Console / debug printing

| Symbol | One-liner |
|--------|-----------|
| `printc` | Print a colored block-style message. |
| `print_debug` | Debug print with source-location prefix. |
| `color_text`, `ct` | Wrap a string in ANSI color codes. |
| `remove_ansi` | Strip ANSI escape sequences from text. |
| `readable_bytes` | Format an int byte-count as `'1.5 MB'` etc. |
| `mask_api` | Redact API-key-like substrings. |

## Path / string manipulation

| Symbol | One-liner |
|--------|-----------|
| `clean_path` | Normalize a path-string (thin sibling of `scitex_path.clean`). |
| `grep` | Filter a sequence of strings by regex. |
| `search` | Regex search helpers. |
| `parse` | Parse a formatted string back into a dict. |
| `replace` | Multi-pattern string replace. |
| `squeeze_spaces` | Collapse consecutive whitespace. |
| `decapitalize` | Lower-case the first letter only. |
| `title_case` | Title-case a string with sensible stop-words. |

## LaTeX and mathtext

| Symbol | One-liner |
|--------|-----------|
| `latex_style`, `to_latex_style`, `safe_to_latex_style` | Convert plain text to LaTeX. |
| `add_hat_in_latex_style`, `safe_add_hat_in_latex_style`, `hat_latex_style` | Add a `\hat{}` accent. |
| `latex_to_mathtext`, `latex_to_unicode` | Convert LaTeX source to matplotlib mathtext or unicode. |
| `safe_latex_render` | Render with automatic fallback. |
| `enable_latex_fallback`, `disable_latex_fallback`, `set_fallback_mode`, `get_fallback_mode` | Fallback toggles. |
| `check_latex_capability`, `get_latex_status`, `reset_latex_cache` | Capability probing. |
| `latex_fallback_decorator` | Decorator wrapping rendering functions with fallback. |
| `LaTeXFallbackError` | Exception raised when no rendering path works. |

## Plot-text formatting

| Symbol | One-liner |
|--------|-----------|
| `axis_label`, `format_axis_label` | Build an axis label string with unit. |
| `title`, `format_title` | Build a title string. |
| `format_plot_text` | Generic formatter for plot text. |
| `check_unit_consistency` | Validate that axes share compatible units. |
| `scientific_text` | Format numbers in scientific notation for plots. |
| `factor_out_digits`, `auto_factor_axis`, `smart_tick_formatter` | Extract a common power-of-ten from tick labels. |

See `scitex_str/_*.py` for exact signatures; every symbol is in its own
`_<symbol>.py` module and typically has a single keyword-free call form.
