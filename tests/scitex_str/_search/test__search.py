"""Unit tests for `scitex_str._search._search` (mirrors `src/scitex_str/_search/_search.py`)."""

from scitex_str._search import grep, parse, replace, search


def test_search_finds_substring_match_in_string_list():
    # Arrange
    patterns = ["foo"]
    candidates = ["foo", "bar", "foobar"]
    # Act
    matched_indices, _ = search(patterns, candidates)
    # Assert
    assert 0 in matched_indices and 2 in matched_indices


def test_grep_returns_lines_containing_the_pattern():
    # Arrange
    lines = ["alpha", "beta", "gamma"]
    pattern = "be"
    # Act
    _indices, hits = grep(lines, pattern)
    # Assert
    assert any("beta" in line for line in hits)


def test_replace_substitutes_named_placeholder_with_value():
    # Arrange
    template = "hello {who}"
    mapping = {"who": "there"}
    # Act
    result = replace(template, mapping)
    # Assert
    assert result == "hello there"


def test_parse_extracts_named_fields_from_format_pattern():
    # Arrange
    raw = "p10_e25"
    pattern = "p{patient}_e{epoch}"
    # Act
    parsed = parse(raw, pattern)
    # Assert
    assert int(parsed["patient"]) == 10
