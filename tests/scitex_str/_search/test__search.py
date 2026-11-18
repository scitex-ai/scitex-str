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


def test_import_scitex_str_does_not_import_pandas_or_xarray():
    # Arrange: a fresh interpreter, so modules other tests imported do not count
    import subprocess
    import sys

    code = (
        "import sys, scitex_str; "
        "print(sorted(m for m in ('pandas', 'xarray') if m in sys.modules))"
    )
    # Act
    out = subprocess.run(
        [sys.executable, "-c", code], capture_output=True, text=True, check=True
    ).stdout.strip()
    # Assert
    assert out == "[]"


def test_search_accepts_pandas_series_when_pandas_is_imported():
    # Arrange
    import pytest

    pd = pytest.importorskip("pandas")
    candidates = pd.Series(["foo", "bar", "foobar"])
    # Act
    matched_indices, _ = search(["foo"], candidates)
    # Assert
    assert list(matched_indices) == [0, 2]
