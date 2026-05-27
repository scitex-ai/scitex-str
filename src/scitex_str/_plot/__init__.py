"""Plot-text helpers (axis labels, tick formatters, scientific notation)."""

from ._factor_out_digits import (
    auto_factor_axis,
    factor_out_digits,
    smart_tick_formatter,
)
from ._format_plot_text import (
    axis_label,
    check_unit_consistency,
    format_axis_label,
    format_plot_text,
    format_title,
    scientific_text,
    title,
)

__all__ = [
    "auto_factor_axis",
    "axis_label",
    "check_unit_consistency",
    "factor_out_digits",
    "format_axis_label",
    "format_plot_text",
    "format_title",
    "scientific_text",
    "smart_tick_formatter",
    "title",
]
