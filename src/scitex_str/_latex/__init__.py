"""LaTeX formatting helpers + matplotlib-rendering fallback."""

from ._latex import (
    add_hat_in_latex_style,
    hat_latex_style,
    latex_style,
    safe_add_hat_in_latex_style,
    safe_to_latex_style,
    to_latex_style,
)
from ._latex_fallback import (
    LaTeXFallbackError,
    check_latex_capability,
    disable_latex_fallback,
    enable_latex_fallback,
    get_fallback_mode,
    get_latex_status,
    latex_fallback_decorator,
    latex_to_mathtext,
    latex_to_unicode,
    logger,
    reset_latex_cache,
    safe_latex_render,
    set_fallback_mode,
)

__all__ = [
    "LaTeXFallbackError",
    "add_hat_in_latex_style",
    "check_latex_capability",
    "disable_latex_fallback",
    "enable_latex_fallback",
    "get_fallback_mode",
    "get_latex_status",
    "hat_latex_style",
    "latex_fallback_decorator",
    "latex_style",
    "latex_to_mathtext",
    "latex_to_unicode",
    "logger",
    "reset_latex_cache",
    "safe_add_hat_in_latex_style",
    "safe_latex_render",
    "safe_to_latex_style",
    "set_fallback_mode",
    "to_latex_style",
]
