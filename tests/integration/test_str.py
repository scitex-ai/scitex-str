#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tests for scitex-str package core functions."""

import pytest


# ---------------------------------------------------------------------------
# 1. Core string utilities
# ---------------------------------------------------------------------------
class TestCleanPath:
    """Tests for clean_path function."""

    def test_normalizes_double_slashes(self):
        from scitex_str import clean_path

        assert clean_path("/home//user//file.txt") == "/home/user/file.txt"

    def test_resolves_dot_segments(self):
        from scitex_str import clean_path

        assert clean_path("/home/user/./folder/../file.txt") == "/home/user/file.txt"

    def test_preserves_trailing_slash_for_directories(self):
        from scitex_str import clean_path

        result = clean_path("/home/user/dir/")
        assert result.endswith("/")

    def test_rejects_non_string_input(self):
        from scitex_str import clean_path

        with pytest.raises((TypeError, ValueError)):
            clean_path(123)

    def test_handles_pathlike_object(self):
        from pathlib import Path

        from scitex_str import clean_path

        result = clean_path(Path("/home/user/file.txt"))
        assert result == "/home/user/file.txt"


class TestDecapitalize:
    """Tests for decapitalize function."""

    def test_lowercase_first_char(self):
        from scitex_str import decapitalize

        assert decapitalize("Hello") == "hello"

    def test_preserves_rest_of_string(self):
        from scitex_str import decapitalize

        assert decapitalize("WORLD") == "wORLD"

    def test_empty_string_returns_empty(self):
        from scitex_str import decapitalize

        assert decapitalize("") == ""

    def test_single_char(self):
        from scitex_str import decapitalize

        assert decapitalize("A") == "a"

    def test_already_lowercase_unchanged(self):
        from scitex_str import decapitalize

        assert decapitalize("hello") == "hello"


class TestRemoveAnsi:
    """Tests for remove_ansi function."""

    def test_strips_color_codes(self):
        from scitex_str import remove_ansi

        colored = "\033[91mHello\033[0m"
        assert remove_ansi(colored) == "Hello"

    def test_plain_text_unchanged(self):
        from scitex_str import remove_ansi

        assert remove_ansi("plain text") == "plain text"

    def test_multiple_codes_stripped(self):
        from scitex_str import remove_ansi

        text = "\033[91mRed\033[0m and \033[92mGreen\033[0m"
        assert remove_ansi(text) == "Red and Green"


class TestSqueezeSpaces:
    """Tests for squeeze_spaces function."""

    def test_collapses_multiple_spaces(self):
        from scitex_str import squeeze_spaces

        assert squeeze_spaces("Hello   world") == "Hello world"

    def test_single_space_unchanged(self):
        from scitex_str import squeeze_spaces

        assert squeeze_spaces("Hello world") == "Hello world"

    def test_custom_pattern_and_replacement(self):
        from scitex_str import squeeze_spaces

        assert squeeze_spaces("a---b--c-d", pattern="-+", repl="-") == "a-b-c-d"


class TestTitleCase:
    """Tests for title_case function."""

    def test_basic_title_case(self):
        from scitex_str import title_case

        result = title_case("welcome to the world")
        assert result == "Welcome to the World"

    def test_handles_mixed_case(self):
        from scitex_str import title_case

        result = title_case("using cpus for tasks")
        assert result[0] == "U"  # First word capitalized

    def test_lowercase_prepositions(self):
        from scitex_str import title_case

        result = title_case("the art of war and peace")
        # "the", "of", "and" should stay lowercase
        words = result.split()
        assert words[1] == "Art"
        assert words[2] == "of"
        assert words[4] == "and"


class TestReadableBytes:
    """Tests for readable_bytes function."""

    def test_bytes(self):
        from scitex_str import readable_bytes

        assert readable_bytes(100) == "100.0 B"

    def test_kibibytes(self):
        from scitex_str import readable_bytes

        assert readable_bytes(1024) == "1.0 KiB"

    def test_mebibytes(self):
        from scitex_str import readable_bytes

        assert readable_bytes(1048576) == "1.0 MiB"

    def test_gibibytes(self):
        from scitex_str import readable_bytes

        assert readable_bytes(1073741824) == "1.0 GiB"

    def test_custom_suffix(self):
        from scitex_str import readable_bytes

        result = readable_bytes(1024, suffix="b")
        assert "Kib" in result


# ---------------------------------------------------------------------------
# 2. Search / Replace / Grep
# ---------------------------------------------------------------------------
class TestGrep:
    """Tests for grep function."""

    def test_basic_match(self):
        from scitex_str import grep

        indices, matched = grep(["apple", "banana", "cherry"], "an")
        assert matched == ["banana"]
        assert indices == [1]

    def test_regex_pattern(self):
        from scitex_str import grep

        indices, matched = grep(["cat", "car", "dog"], "^ca")
        assert set(matched) == {"cat", "car"}

    def test_no_matches_returns_empty(self):
        from scitex_str import grep

        indices, matched = grep(["apple", "banana"], "xyz")
        assert matched == []
        assert indices == []


class TestSearch:
    """Tests for search function (requires numpy, natsort)."""

    @pytest.fixture(autouse=True)
    def _check_deps(self):
        pytest.importorskip("numpy")
        pytest.importorskip("natsort")

    def test_single_pattern_multiple_strings(self):
        from scitex_str import search

        indices, matched = search("orange", ["apple", "orange", "orange_juice"])
        assert "orange" in matched
        assert "orange_juice" in matched

    def test_multiple_patterns(self):
        from scitex_str import search

        indices, matched = search(
            ["orange", "banana"],
            ["apple", "orange", "banana", "orange_juice"],
        )
        assert "orange" in matched
        assert "banana" in matched

    def test_perfect_match_mode(self):
        from scitex_str import search

        indices, matched = search(
            "orange",
            ["orange", "orange_juice"],
            only_perfect_match=True,
        )
        assert matched == ["orange"]

    def test_as_bool_mode(self):
        import numpy as np

        from scitex_str import search

        bools, matched = search("apple", ["apple", "banana", "pineapple"], as_bool=True)
        assert isinstance(bools, np.ndarray)
        assert bools.dtype == bool
        assert bools[0] is np.True_


class TestReplace:
    """Tests for replace function."""

    @pytest.fixture(autouse=True)
    def _check_deps(self):
        pytest.importorskip("scitex_dict")

    def test_dict_replacement(self):
        from scitex_str import replace

        result = replace("Hello, {name}!", {"name": "World"})
        assert result == "Hello, World!"

    def test_string_replacement_returns_new_string(self):
        from scitex_str import replace

        assert replace("old", "new") == "new"

    def test_none_replacements_returns_original(self):
        from scitex_str import replace

        assert replace("hello", None) == "hello"

    def test_multiple_placeholders(self):
        from scitex_str import replace

        result = replace("{a} and {b}", {"a": "X", "b": "Y"})
        assert result == "X and Y"

    def test_non_string_input_raises(self):
        from scitex_str import replace

        with pytest.raises(TypeError):
            replace(123, {"key": "val"})


# ---------------------------------------------------------------------------
# 3. LaTeX utilities
# ---------------------------------------------------------------------------
class TestToLatexStyle:
    """Tests for to_latex_style and safe_to_latex_style."""

    def test_wraps_string_in_dollars(self):
        from scitex_str import to_latex_style

        assert to_latex_style("x^2") == "$x^2$"

    def test_wraps_number(self):
        from scitex_str import to_latex_style

        assert to_latex_style(123) == "$123$"

    def test_avoids_double_wrapping(self):
        from scitex_str import to_latex_style

        assert to_latex_style("$already$") == "$already$"

    def test_empty_input_returns_empty(self):
        from scitex_str import to_latex_style

        assert to_latex_style("") == ""
        assert to_latex_style(None) == ""

    def test_safe_alias_identical(self):
        from scitex_str import safe_to_latex_style, to_latex_style

        assert safe_to_latex_style("abc") == to_latex_style("abc")

    def test_zero_is_handled(self):
        from scitex_str import to_latex_style

        assert to_latex_style(0) == "$0$"


class TestAddHatInLatexStyle:
    """Tests for add_hat_in_latex_style."""

    def test_adds_hat(self):
        from scitex_str import add_hat_in_latex_style

        result = add_hat_in_latex_style("x")
        assert result == r"$\hat{x}$"

    def test_hat_with_number(self):
        from scitex_str import add_hat_in_latex_style

        result = add_hat_in_latex_style(1)
        assert result == r"$\hat{1}$"

    def test_empty_returns_empty(self):
        from scitex_str import add_hat_in_latex_style

        assert add_hat_in_latex_style("") == ""


class TestLatexToUnicode:
    """Tests for latex_to_unicode conversion."""

    def test_greek_letter(self):
        from scitex_str import latex_to_unicode

        result = latex_to_unicode(r"$\\alpha$")
        assert "α" in result

    def test_math_symbol(self):
        from scitex_str import latex_to_unicode

        result = latex_to_unicode(r"$\\pm$")
        assert "±" in result

    def test_empty_returns_empty(self):
        from scitex_str import latex_to_unicode

        assert latex_to_unicode("") == ""
        assert latex_to_unicode(None) is None


# ---------------------------------------------------------------------------
# 4. Color text and mask_api
# ---------------------------------------------------------------------------
class TestColorText:
    """Tests for color_text and ct alias."""

    def test_applies_ansi_codes(self):
        from scitex_str import color_text

        result = color_text("hello", "red")
        assert "\033[91m" in result
        assert "\033[0m" in result
        assert "hello" in result

    def test_ct_is_alias(self):
        from scitex_str import color_text, ct

        assert ct("hi", "blue") == color_text("hi", "blue")

    def test_default_color_is_green(self):
        from scitex_str import color_text

        result = color_text("test")
        assert "\033[92m" in result

    def test_unknown_color_falls_back_to_reset(self):
        from scitex_str import color_text

        result = color_text("test", "nonexistent")
        assert "\033[0m" in result


class TestMaskApi:
    """Tests for mask_api function."""

    def test_masks_middle(self):
        from scitex_str import mask_api

        result = mask_api("sk-1234567890abcdef")
        assert result.startswith("sk-1")
        assert result.endswith("cdef")
        assert "****" in result

    def test_masks_long_key(self):
        from scitex_str import mask_api

        result = mask_api("abcdefghijklmnopqrstuvwxyz")
        # Should mask some portion of the key
        assert "****" in result or "***" in result or len(result) < 26


# ---------------------------------------------------------------------------
# 5. Numeric formatting (factor_out_digits)
# ---------------------------------------------------------------------------
class TestFactorOutDigits:
    """Tests for factor_out_digits function."""

    @pytest.fixture(autouse=True)
    def _check_deps(self):
        pytest.importorskip("numpy")

    def test_thousands(self):
        from scitex_str import factor_out_digits

        factored, factor_str = factor_out_digits([1000, 2000, 3000])
        assert factored == [1.0, 2.0, 3.0]
        assert "10" in factor_str
        assert "3" in factor_str

    def test_small_values_no_factor(self):
        from scitex_str import factor_out_digits

        factored, factor_str = factor_out_digits([1, 2, 3])
        assert factor_str == ""

    def test_scalar_input(self):
        from scitex_str import factor_out_digits

        factored, factor_str = factor_out_digits(1e6)
        assert isinstance(factored, float)
        assert "6" in factor_str

    def test_all_zeros_no_factor(self):
        from scitex_str import factor_out_digits

        factored, factor_str = factor_out_digits([0, 0, 0])
        assert factor_str == ""

    def test_negative_powers(self):
        from scitex_str import factor_out_digits

        factored, factor_str = factor_out_digits([0.001, 0.002, 0.003])
        assert factored == [1.0, 2.0, 3.0]
        assert "-3" in factor_str

    def test_unicode_mode(self):
        from scitex_str import factor_out_digits

        _, factor_str = factor_out_digits(
            [1000, 2000], return_latex=False, return_unicode=True
        )
        assert "×10" in factor_str


# ---------------------------------------------------------------------------
# 6. Printc smoke test (output-only function)
# ---------------------------------------------------------------------------
class TestPrintc:
    """Tests for printc function (prints to stdout)."""

    def test_does_not_raise(self, capsys):
        from scitex_str import printc

        printc("test message", c="green")
        captured = capsys.readouterr()
        assert "test message" in captured.out


# EOF
