#!/usr/bin/env python3
"""scitex-str: Text processing utilities for scientific workflows."""

from __future__ import annotations

try:
    from importlib.metadata import PackageNotFoundError
    from importlib.metadata import version as _v

    try:
        __version__ = _v("scitex-str")
    except PackageNotFoundError:
        __version__ = "0.0.0+local"
    del _v, PackageNotFoundError
except ImportError:  # pragma: no cover — only on ancient Pythons
    __version__ = "0.0.0+local"

# Subpackage re-exports — see `general/02_package_02_project-structure-src.md`.
from ._ansi import color_text, ct, remove_ansi
from ._case import decapitalize, title_case
from ._clean_path import clean_path
from ._latex import (
    LaTeXFallbackError,
    add_hat_in_latex_style,
    check_latex_capability,
    disable_latex_fallback,
    enable_latex_fallback,
    get_fallback_mode,
    get_latex_status,
    hat_latex_style,
    latex_fallback_decorator,
    latex_style,
    latex_to_mathtext,
    latex_to_unicode,
    reset_latex_cache,
    safe_add_hat_in_latex_style,
    safe_latex_render,
    safe_to_latex_style,
    set_fallback_mode,
    to_latex_style,
)
from ._latex._latex_fallback import logger as _logger  # Internal
from ._mask import mask_api
from ._plot import (
    auto_factor_axis,
    axis_label,
    check_unit_consistency,
    factor_out_digits,
    format_axis_label,
    format_plot_text,
    format_title,
    scientific_text,
    smart_tick_formatter,
    title,
)
from ._print import print_debug, printc
from ._readable_bytes import readable_bytes
from ._search import grep, parse, replace, search
from ._squeeze_space import squeeze_spaces

__all__ = [
    "__version__",
    "LaTeXFallbackError",
    "add_hat_in_latex_style",
    "auto_factor_axis",
    "axis_label",
    "check_latex_capability",
    "check_unit_consistency",
    "clean_path",
    "color_text",
    "ct",
    "decapitalize",
    "disable_latex_fallback",
    "enable_latex_fallback",
    "factor_out_digits",
    "format_axis_label",
    "format_plot_text",
    "format_title",
    "get_fallback_mode",
    "get_latex_status",
    "grep",
    "hat_latex_style",
    "latex_fallback_decorator",
    "latex_style",
    "latex_to_mathtext",
    "latex_to_unicode",
    "mask_api",
    "parse",
    "print_debug",
    "printc",
    "readable_bytes",
    "remove_ansi",
    "replace",
    "reset_latex_cache",
    "safe_add_hat_in_latex_style",
    "safe_latex_render",
    "safe_to_latex_style",
    "scientific_text",
    "search",
    "set_fallback_mode",
    "smart_tick_formatter",
    "squeeze_spaces",
    "title",
    "title_case",
    "to_latex_style",
]

# EOF
