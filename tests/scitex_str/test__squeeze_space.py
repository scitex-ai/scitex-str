#!/usr/bin/env python3
"""Tests for scitex_str._squeeze_space.squeeze_spaces."""

import pytest

from scitex_str._squeeze_space import squeeze_spaces


class TestSqueezeSpaces:
    def test_collapses_multiple_spaces_into_one(self):
        # Arrange
        text = "Hello   world"
        # Act
        result = squeeze_spaces(text)
        # Assert
        assert result == "Hello world"

    def test_single_space_passes_through_unchanged(self):
        # Arrange
        text = "Hello world"
        # Act
        result = squeeze_spaces(text)
        # Assert
        assert result == "Hello world"

    def test_no_spaces_passes_through_unchanged(self):
        # Arrange
        text = "Hello"
        # Act
        result = squeeze_spaces(text)
        # Assert
        assert result == "Hello"

    def test_custom_pattern_collapses_consecutive_dashes(self):
        # Arrange
        text = "a---b--c-d"
        # Act
        result = squeeze_spaces(text, pattern="-+", repl="-")
        # Assert
        assert result == "a-b-c-d"

    def test_pattern_with_empty_replacement_removes_matches(self):
        # Arrange
        text = "a-b-c"
        # Act
        result = squeeze_spaces(text, pattern="-", repl="")
        # Assert
        assert result == "abc"

    def test_empty_string_returns_empty_string(self):
        # Arrange
        text = ""
        # Act
        result = squeeze_spaces(text)
        # Assert
        assert result == ""

    def test_string_of_only_spaces_collapses_to_single_space(self):
        # Arrange
        text = "     "
        # Act
        result = squeeze_spaces(text)
        # Assert
        assert result == " "


if __name__ == "__main__":
    import os

    pytest.main([os.path.abspath(__file__), "-v"])

# EOF
