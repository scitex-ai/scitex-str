"""Unit tests for `scitex_str._case._decapitalize` (mirrors `src/scitex_str/_case/_decapitalize.py`)."""

from scitex_str._case import decapitalize, title_case


def test_decapitalize_lowers_first_character_only():
    # Arrange
    text = "Hello World"
    # Act
    result = decapitalize(text)
    # Assert
    assert result == "hello World"


def test_decapitalize_empty_string_returns_empty_string():
    # Arrange
    text = ""
    # Act
    result = decapitalize(text)
    # Assert
    assert result == ""


def test_title_case_capitalizes_significant_words():
    # Arrange
    text = "hello world"
    # Act
    result = title_case(text)
    # Assert
    assert result == "Hello World"
