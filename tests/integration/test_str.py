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
        # Arrange
        from scitex_str import clean_path

        path = "/home//user//file.txt"
        # Act
        result = clean_path(path)
        # Assert
        assert result == "/home/user/file.txt"

    def test_resolves_dot_segments(self):
        # Arrange
        from scitex_str import clean_path

        path = "/home/user/./folder/../file.txt"
        # Act
        result = clean_path(path)
        # Assert
        assert result == "/home/user/file.txt"

    def test_preserves_trailing_slash_for_directories(self):
        # Arrange
        from scitex_str import clean_path

        path = "/home/user/dir/"
        # Act
        result = clean_path(path)
        # Assert
        assert result.endswith("/")

    def test_rejects_non_string_input(self):
        # Arrange
        from scitex_str import clean_path

        bad_input = 123
        # Act
        action = lambda: clean_path(bad_input)
        # Assert
        with pytest.raises((TypeError, ValueError)):
            action()

    def test_handles_pathlike_object(self):
        # Arrange
        from pathlib import Path

        from scitex_str import clean_path

        path_obj = Path("/home/user/file.txt")
        # Act
        result = clean_path(path_obj)
        # Assert
        assert result == "/home/user/file.txt"


class TestDecapitalize:
    """Tests for decapitalize function."""

    def test_lowercases_first_character_of_word(self):
        # Arrange
        from scitex_str import decapitalize

        word = "Hello"
        # Act
        result = decapitalize(word)
        # Assert
        assert result == "hello"

    def test_preserves_rest_of_string_unchanged(self):
        # Arrange
        from scitex_str import decapitalize

        word = "WORLD"
        # Act
        result = decapitalize(word)
        # Assert
        assert result == "wORLD"

    def test_empty_string_returns_empty_string(self):
        # Arrange
        from scitex_str import decapitalize

        word = ""
        # Act
        result = decapitalize(word)
        # Assert
        assert result == ""

    def test_single_character_is_lowercased(self):
        # Arrange
        from scitex_str import decapitalize

        word = "A"
        # Act
        result = decapitalize(word)
        # Assert
        assert result == "a"

    def test_already_lowercase_string_unchanged(self):
        # Arrange
        from scitex_str import decapitalize

        word = "hello"
        # Act
        result = decapitalize(word)
        # Assert
        assert result == "hello"


class TestRemoveAnsi:
    """Tests for remove_ansi function."""

    def test_strips_ansi_color_codes(self):
        # Arrange
        from scitex_str import remove_ansi

        colored = "\033[91mHello\033[0m"
        # Act
        result = remove_ansi(colored)
        # Assert
        assert result == "Hello"

    def test_plain_text_passes_through_unchanged(self):
        # Arrange
        from scitex_str import remove_ansi

        plain = "plain text"
        # Act
        result = remove_ansi(plain)
        # Assert
        assert result == "plain text"

    def test_multiple_ansi_codes_all_stripped(self):
        # Arrange
        from scitex_str import remove_ansi

        text = "\033[91mRed\033[0m and \033[92mGreen\033[0m"
        # Act
        result = remove_ansi(text)
        # Assert
        assert result == "Red and Green"


class TestSqueezeSpaces:
    """Tests for squeeze_spaces function."""

    def test_collapses_multiple_spaces_into_one(self):
        # Arrange
        from scitex_str import squeeze_spaces

        text = "Hello   world"
        # Act
        result = squeeze_spaces(text)
        # Assert
        assert result == "Hello world"

    def test_single_space_passes_through_unchanged(self):
        # Arrange
        from scitex_str import squeeze_spaces

        text = "Hello world"
        # Act
        result = squeeze_spaces(text)
        # Assert
        assert result == "Hello world"

    def test_custom_pattern_and_replacement_collapses_dashes(self):
        # Arrange
        from scitex_str import squeeze_spaces

        text = "a---b--c-d"
        # Act
        result = squeeze_spaces(text, pattern="-+", repl="-")
        # Assert
        assert result == "a-b-c-d"


class TestTitleCase:
    """Tests for title_case function."""

    def test_capitalizes_content_words_in_sentence(self):
        # Arrange
        from scitex_str import title_case

        sentence = "welcome to the world"
        # Act
        result = title_case(sentence)
        # Assert
        assert result == "Welcome to the World"

    def test_handles_mixed_case_first_word_capitalized(self):
        # Arrange
        from scitex_str import title_case

        sentence = "using cpus for tasks"
        # Act
        result = title_case(sentence)
        # Assert
        assert result[0] == "U"

    def test_lowercase_prepositions_stay_lowercase(self):
        # Arrange
        from scitex_str import title_case

        sentence = "the art of war and peace"
        # Act
        words = title_case(sentence).split()
        # Assert
        assert words[1:5] == ["Art", "of", "War", "and"]


class TestReadableBytes:
    """Tests for readable_bytes function."""

    def test_formats_bytes_unit(self):
        # Arrange
        from scitex_str import readable_bytes

        n = 100
        # Act
        result = readable_bytes(n)
        # Assert
        assert result == "100.0 B"

    def test_formats_kibibytes_unit(self):
        # Arrange
        from scitex_str import readable_bytes

        n = 1_024
        # Act
        result = readable_bytes(n)
        # Assert
        assert result == "1.0 KiB"

    def test_formats_mebibytes_unit(self):
        # Arrange
        from scitex_str import readable_bytes

        n = 1_048_576
        # Act
        result = readable_bytes(n)
        # Assert
        assert result == "1.0 MiB"

    def test_formats_gibibytes_unit(self):
        # Arrange
        from scitex_str import readable_bytes

        n = 1_073_741_824
        # Act
        result = readable_bytes(n)
        # Assert
        assert result == "1.0 GiB"

    def test_custom_suffix_appears_in_output(self):
        # Arrange
        from scitex_str import readable_bytes

        n = 1_024
        # Act
        result = readable_bytes(n, suffix="b")
        # Assert
        assert "Kib" in result


# ---------------------------------------------------------------------------
# 2. Search / Replace / Grep
# ---------------------------------------------------------------------------
class TestGrep:
    """Tests for grep function."""

    def test_basic_substring_match_returns_matched_strings(self):
        # Arrange
        from scitex_str import grep

        strings = ["apple", "banana", "cherry"]
        # Act
        indices, matched = grep(strings, "an")
        # Assert
        assert matched == ["banana"]

    def test_basic_substring_match_returns_matched_indices(self):
        # Arrange
        from scitex_str import grep

        strings = ["apple", "banana", "cherry"]
        # Act
        indices, matched = grep(strings, "an")
        # Assert
        assert indices == [1]

    def test_regex_anchor_pattern_matches_prefixes(self):
        # Arrange
        from scitex_str import grep

        strings = ["cat", "car", "dog"]
        # Act
        indices, matched = grep(strings, "^ca")
        # Assert
        assert set(matched) == {"cat", "car"}

    def test_no_matches_returns_empty_matched_list(self):
        # Arrange
        from scitex_str import grep

        strings = ["apple", "banana"]
        # Act
        indices, matched = grep(strings, "xyz")
        # Assert
        assert matched == []

    def test_no_matches_returns_empty_indices_list(self):
        # Arrange
        from scitex_str import grep

        strings = ["apple", "banana"]
        # Act
        indices, matched = grep(strings, "xyz")
        # Assert
        assert indices == []


class TestSearch:
    """Tests for search function (requires numpy, natsort)."""

    @pytest.fixture(autouse=True)
    def _check_deps(self):
        pytest.importorskip("numpy")
        pytest.importorskip("natsort")

    def test_single_pattern_matches_exact_string(self):
        # Arrange
        from scitex_str import search

        strings = ["apple", "orange", "orange_juice"]
        # Act
        indices, matched = search("orange", strings)
        # Assert
        assert "orange" in matched

    def test_single_pattern_matches_prefix_string(self):
        # Arrange
        from scitex_str import search

        strings = ["apple", "orange", "orange_juice"]
        # Act
        indices, matched = search("orange", strings)
        # Assert
        assert "orange_juice" in matched

    def test_multiple_patterns_match_first_pattern(self):
        # Arrange
        from scitex_str import search

        strings = ["apple", "orange", "banana", "orange_juice"]
        # Act
        indices, matched = search(["orange", "banana"], strings)
        # Assert
        assert "orange" in matched

    def test_multiple_patterns_match_second_pattern(self):
        # Arrange
        from scitex_str import search

        strings = ["apple", "orange", "banana", "orange_juice"]
        # Act
        indices, matched = search(["orange", "banana"], strings)
        # Assert
        assert "banana" in matched

    def test_perfect_match_mode_excludes_substring_matches(self):
        # Arrange
        from scitex_str import search

        strings = ["orange", "orange_juice"]
        # Act
        indices, matched = search("orange", strings, only_perfect_match=True)
        # Assert
        assert matched == ["orange"]

    def test_as_bool_mode_returns_numpy_array(self):
        # Arrange
        import numpy as np

        from scitex_str import search

        strings = ["apple", "banana", "pineapple"]
        # Act
        bools, matched = search("apple", strings, as_bool=True)
        # Assert
        assert isinstance(bools, np.ndarray)

    def test_as_bool_mode_array_has_bool_dtype(self):
        # Arrange
        from scitex_str import search

        strings = ["apple", "banana", "pineapple"]
        # Act
        bools, matched = search("apple", strings, as_bool=True)
        # Assert
        assert bools.dtype == bool

    def test_as_bool_mode_first_element_matches(self):
        # Arrange
        import numpy as np

        from scitex_str import search

        strings = ["apple", "banana", "pineapple"]
        # Act
        bools, matched = search("apple", strings, as_bool=True)
        # Assert
        assert bools[0] is np.True_


class TestReplace:
    """Tests for replace function."""

    @pytest.fixture(autouse=True)
    def _check_deps(self):
        pytest.importorskip("scitex_dict")

    def test_dict_replacement_substitutes_placeholder(self):
        # Arrange
        from scitex_str import replace

        template = "Hello, {name}!"
        # Act
        result = replace(template, {"name": "World"})
        # Assert
        assert result == "Hello, World!"

    def test_string_replacement_returns_new_string(self):
        # Arrange
        from scitex_str import replace

        original = "old"
        # Act
        result = replace(original, "new")
        # Assert
        assert result == "new"

    def test_none_replacements_returns_original_unchanged(self):
        # Arrange
        from scitex_str import replace

        original = "hello"
        # Act
        result = replace(original, None)
        # Assert
        assert result == "hello"

    def test_multiple_placeholders_all_substituted(self):
        # Arrange
        from scitex_str import replace

        template = "{a} and {b}"
        # Act
        result = replace(template, {"a": "X", "b": "Y"})
        # Assert
        assert result == "X and Y"

    def test_non_string_input_raises_type_error(self):
        # Arrange
        from scitex_str import replace

        bad_input = 123
        # Act
        action = lambda: replace(bad_input, {"key": "val"})
        # Assert
        with pytest.raises(TypeError):
            action()


# ---------------------------------------------------------------------------
# 3. LaTeX utilities
# ---------------------------------------------------------------------------
class TestToLatexStyle:
    """Tests for to_latex_style and safe_to_latex_style."""

    def test_wraps_plain_string_in_dollars(self):
        # Arrange
        from scitex_str import to_latex_style

        expr = "x^2"
        # Act
        result = to_latex_style(expr)
        # Assert
        assert result == "$x^2$"

    def test_wraps_numeric_value_in_dollars(self):
        # Arrange
        from scitex_str import to_latex_style

        expr = 123
        # Act
        result = to_latex_style(expr)
        # Assert
        assert result == "$123$"

    def test_already_wrapped_input_not_double_wrapped(self):
        # Arrange
        from scitex_str import to_latex_style

        expr = "$already$"
        # Act
        result = to_latex_style(expr)
        # Assert
        assert result == "$already$"

    def test_empty_string_input_returns_empty(self):
        # Arrange
        from scitex_str import to_latex_style

        # Act
        result = to_latex_style("")
        # Assert
        assert result == ""

    def test_none_input_returns_empty(self):
        # Arrange
        from scitex_str import to_latex_style

        # Act
        result = to_latex_style(None)
        # Assert
        assert result == ""

    def test_safe_alias_matches_canonical_function(self):
        # Arrange
        from scitex_str import safe_to_latex_style, to_latex_style

        expr = "abc"
        # Act
        result = safe_to_latex_style(expr)
        # Assert
        assert result == to_latex_style(expr)

    def test_zero_value_is_wrapped(self):
        # Arrange
        from scitex_str import to_latex_style

        expr = 0
        # Act
        result = to_latex_style(expr)
        # Assert
        assert result == "$0$"


class TestAddHatInLatexStyle:
    """Tests for add_hat_in_latex_style."""

    def test_adds_hat_around_string_symbol(self):
        # Arrange
        from scitex_str import add_hat_in_latex_style

        symbol = "x"
        # Act
        result = add_hat_in_latex_style(symbol)
        # Assert
        assert result == r"$\hat{x}$"

    def test_adds_hat_around_numeric_symbol(self):
        # Arrange
        from scitex_str import add_hat_in_latex_style

        symbol = 1
        # Act
        result = add_hat_in_latex_style(symbol)
        # Assert
        assert result == r"$\hat{1}$"

    def test_empty_input_returns_empty_string(self):
        # Arrange
        from scitex_str import add_hat_in_latex_style

        # Act
        result = add_hat_in_latex_style("")
        # Assert
        assert result == ""


class TestLatexToUnicode:
    """Tests for latex_to_unicode conversion."""

    def test_greek_letter_macro_becomes_unicode_alpha(self):
        # Arrange
        from scitex_str import latex_to_unicode

        expr = r"$\\alpha$"
        # Act
        result = latex_to_unicode(expr)
        # Assert
        assert "α" in result

    def test_math_macro_becomes_unicode_plus_minus(self):
        # Arrange
        from scitex_str import latex_to_unicode

        expr = r"$\\pm$"
        # Act
        result = latex_to_unicode(expr)
        # Assert
        assert "±" in result

    def test_empty_string_input_returns_empty_string(self):
        # Arrange
        from scitex_str import latex_to_unicode

        # Act
        result = latex_to_unicode("")
        # Assert
        assert result == ""

    def test_none_input_returns_none(self):
        # Arrange
        from scitex_str import latex_to_unicode

        # Act
        result = latex_to_unicode(None)
        # Assert
        assert result is None


# ---------------------------------------------------------------------------
# 4. Color text and mask_api
# ---------------------------------------------------------------------------
class TestColorText:
    """Tests for color_text and ct alias."""

    def test_applies_red_ansi_open_code(self):
        # Arrange
        from scitex_str import color_text

        text = "hello"
        # Act
        result = color_text(text, "red")
        # Assert
        assert "\033[91m" in result

    def test_applies_ansi_reset_code(self):
        # Arrange
        from scitex_str import color_text

        text = "hello"
        # Act
        result = color_text(text, "red")
        # Assert
        assert "\033[0m" in result

    def test_preserves_original_text_content(self):
        # Arrange
        from scitex_str import color_text

        text = "hello"
        # Act
        result = color_text(text, "red")
        # Assert
        assert "hello" in result

    def test_ct_alias_matches_color_text(self):
        # Arrange
        from scitex_str import color_text, ct

        # Act
        result = ct("hi", "blue")
        # Assert
        assert result == color_text("hi", "blue")

    def test_default_color_is_green(self):
        # Arrange
        from scitex_str import color_text

        text = "test"
        # Act
        result = color_text(text)
        # Assert
        assert "\033[92m" in result

    def test_unknown_color_falls_back_to_reset(self):
        # Arrange
        from scitex_str import color_text

        text = "test"
        # Act
        result = color_text(text, "nonexistent")
        # Assert
        assert "\033[0m" in result


class TestMaskApi:
    """Tests for mask_api function."""

    def test_keeps_short_prefix_of_key(self):
        # Arrange
        from scitex_str import mask_api

        key = "sk-1234567890abcdef"
        # Act
        result = mask_api(key)
        # Assert
        assert result.startswith("sk-1")

    def test_keeps_short_suffix_of_key(self):
        # Arrange
        from scitex_str import mask_api

        key = "sk-1234567890abcdef"
        # Act
        result = mask_api(key)
        # Assert
        assert result.endswith("cdef")

    def test_masks_middle_with_asterisks(self):
        # Arrange
        from scitex_str import mask_api

        key = "sk-1234567890abcdef"
        # Act
        result = mask_api(key)
        # Assert
        assert "****" in result

    def test_long_key_is_partially_masked(self):
        # Arrange
        from scitex_str import mask_api

        key = "abcdefghijklmnopqrstuvwxyz"
        # Act
        result = mask_api(key)
        # Assert
        assert "***" in result or len(result) < 26


# ---------------------------------------------------------------------------
# 5. Numeric formatting (factor_out_digits)
# ---------------------------------------------------------------------------
class TestFactorOutDigits:
    """Tests for factor_out_digits function."""

    @pytest.fixture(autouse=True)
    def _check_deps(self):
        pytest.importorskip("numpy")

    def test_thousands_factored_to_units(self):
        # Arrange
        from scitex_str import factor_out_digits

        values = [1_000, 2_000, 3_000]
        # Act
        factored, factor_str = factor_out_digits(values)
        # Assert
        assert factored == [1.0, 2.0, 3.0]

    def test_thousands_factor_string_contains_exponent_base(self):
        # Arrange
        from scitex_str import factor_out_digits

        values = [1_000, 2_000, 3_000]
        # Act
        factored, factor_str = factor_out_digits(values)
        # Assert
        assert "10" in factor_str

    def test_thousands_factor_string_contains_exponent_digit(self):
        # Arrange
        from scitex_str import factor_out_digits

        values = [1_000, 2_000, 3_000]
        # Act
        factored, factor_str = factor_out_digits(values)
        # Assert
        assert "3" in factor_str

    def test_small_values_yield_empty_factor_string(self):
        # Arrange
        from scitex_str import factor_out_digits

        values = [1, 2, 3]
        # Act
        factored, factor_str = factor_out_digits(values)
        # Assert
        assert factor_str == ""

    def test_scalar_input_returns_float_factored_value(self):
        # Arrange
        from scitex_str import factor_out_digits

        value = 1e6
        # Act
        factored, factor_str = factor_out_digits(value)
        # Assert
        assert isinstance(factored, float)

    def test_scalar_input_factor_string_contains_exponent(self):
        # Arrange
        from scitex_str import factor_out_digits

        value = 1e6
        # Act
        factored, factor_str = factor_out_digits(value)
        # Assert
        assert "6" in factor_str

    def test_all_zero_values_yield_empty_factor_string(self):
        # Arrange
        from scitex_str import factor_out_digits

        values = [0, 0, 0]
        # Act
        factored, factor_str = factor_out_digits(values)
        # Assert
        assert factor_str == ""

    def test_negative_power_factored_to_units(self):
        # Arrange
        from scitex_str import factor_out_digits

        values = [0.001, 0.002, 0.003]
        # Act
        factored, factor_str = factor_out_digits(values)
        # Assert
        assert factored == [1.0, 2.0, 3.0]

    def test_negative_power_factor_string_has_minus_three(self):
        # Arrange
        from scitex_str import factor_out_digits

        values = [0.001, 0.002, 0.003]
        # Act
        factored, factor_str = factor_out_digits(values)
        # Assert
        assert "-3" in factor_str

    def test_unicode_mode_uses_multiplication_sign(self):
        # Arrange
        from scitex_str import factor_out_digits

        values = [1_000, 2_000]
        # Act
        _, factor_str = factor_out_digits(
            values, return_latex=False, return_unicode=True
        )
        # Assert
        assert "×10" in factor_str


# ---------------------------------------------------------------------------
# 6. Printc smoke test (output-only function)
# ---------------------------------------------------------------------------
class TestPrintc:
    """Tests for printc function (prints to stdout)."""

    def test_printc_emits_message_to_stdout(self, capsys):
        # Arrange
        from scitex_str import printc

        message = "test message"
        # Act
        printc(message, c="green")
        captured = capsys.readouterr()
        # Assert
        assert "test message" in captured.out


# EOF
