"""Unit tests for `scitex_str._plot._factor_out_digits` (mirrors `src/scitex_str/_plot/_factor_out_digits.py`)."""

import numpy as np

from scitex_str._plot import factor_out_digits, format_plot_text


def test_factor_out_digits_scales_thousands_into_unit_range():
    # Arrange
    values = np.array([1_000.0, 2_000.0, 3_000.0])
    # Act
    factored, _label = factor_out_digits(values)
    # Assert
    assert factored[0] == 1.0


def test_factor_out_digits_label_mentions_the_thousands_exponent():
    # Arrange
    values = np.array([1_000.0, 2_000.0, 3_000.0])
    # Act
    _factored, label = factor_out_digits(values)
    # Assert
    assert "3" in label


def test_format_plot_text_returns_a_non_empty_string():
    # Arrange
    raw = "amplitude"
    # Act
    result = format_plot_text(raw)
    # Assert
    assert isinstance(result, str) and result
