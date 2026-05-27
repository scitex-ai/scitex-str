"""Unit tests for `scitex_str._latex._latex` (mirrors `src/scitex_str/_latex/_latex.py`)."""

from scitex_str._latex import (
    add_hat_in_latex_style,
    safe_latex_render,
    to_latex_style,
)


def test_to_latex_style_wraps_plain_string_in_dollar_signs():
    # Arrange
    symbol = "x"
    # Act
    result = to_latex_style(symbol)
    # Assert
    assert result == "$x$"


def test_to_latex_style_is_idempotent_on_already_wrapped_input():
    # Arrange
    already_wrapped = "$y$"
    # Act
    result = to_latex_style(already_wrapped)
    # Assert
    assert result == "$y$"


def test_add_hat_in_latex_style_wraps_symbol_with_latex_hat():
    # Arrange
    symbol = "p"
    # Act
    result = add_hat_in_latex_style(symbol)
    # Assert
    assert "\\hat{p}" in result


def test_safe_latex_render_returns_string_when_engine_missing():
    # Arrange
    text = "x"
    # Act
    result = safe_latex_render(text)
    # Assert
    assert isinstance(result, str)
