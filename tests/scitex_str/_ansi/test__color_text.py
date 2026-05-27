"""Unit tests for `scitex_str._ansi._color_text` (mirrors `src/scitex_str/_ansi/_color_text.py`)."""

from scitex_str._ansi import color_text, ct, remove_ansi


def test_color_text_wraps_text_with_ansi_escape_sequence():
    # Arrange
    text = "hello"
    # Act
    out = color_text(text, "red")
    # Assert
    assert "\033[" in out


def test_color_text_preserves_original_text_content():
    # Arrange
    text = "hello"
    # Act
    out = color_text(text, "red")
    # Assert
    assert "hello" in out


def test_ct_is_alias_of_color_text():
    # Arrange
    text, color = "x", "red"
    # Act
    result = ct(text, color)
    # Assert
    assert result == color_text(text, color)


def test_remove_ansi_strips_color_codes_round_trip():
    # Arrange
    colored = color_text("abc", "green")
    # Act
    stripped = remove_ansi(colored)
    # Assert
    assert stripped == "abc"
