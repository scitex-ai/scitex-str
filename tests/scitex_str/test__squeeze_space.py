#!/usr/bin/env python3
"""Tests for scitex_str._squeeze_space.squeeze_spaces."""

import pytest

from scitex_str._squeeze_space import squeeze_spaces


class TestSqueezeSpaces:
    def test_collapses_multiple_spaces(self):
        assert squeeze_spaces("Hello   world") == "Hello world"

    def test_single_space_unchanged(self):
        assert squeeze_spaces("Hello world") == "Hello world"

    def test_no_spaces_unchanged(self):
        assert squeeze_spaces("Hello") == "Hello"

    def test_custom_pattern_collapses_dashes(self):
        assert squeeze_spaces("a---b--c-d", pattern="-+", repl="-") == "a-b-c-d"

    def test_pattern_replaces_with_empty(self):
        assert squeeze_spaces("a-b-c", pattern="-", repl="") == "abc"

    def test_empty_string_returns_empty(self):
        assert squeeze_spaces("") == ""

    def test_only_spaces_collapsed_to_single(self):
        assert squeeze_spaces("     ") == " "


if __name__ == "__main__":
    import os

    pytest.main([os.path.abspath(__file__), "-v"])

# EOF
