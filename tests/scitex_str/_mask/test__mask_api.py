"""Unit tests for `scitex_str._mask._mask_api` (mirrors `src/scitex_str/_mask/_mask_api.py`).

The subpackage ships two `mask_api` definitions (`_mask_api.py` and
`_mask_api_key.py`); the latter shadows the former at package level by
historical convention.  These tests cover the public-API surface, which
is what consumers see.
"""

from scitex_str._mask import mask_api


def test_mask_api_preserves_short_prefix_of_key():
    # Arrange
    key = "sk-1234567890abcdef"
    # Act
    result = mask_api(key)
    # Assert
    assert result.startswith("sk-1")


def test_mask_api_preserves_short_suffix_of_key():
    # Arrange
    key = "sk-1234567890abcdef"
    # Act
    result = mask_api(key)
    # Assert
    assert result.endswith("cdef")


def test_mask_api_inserts_asterisks_in_the_middle_of_the_key():
    # Arrange
    key = "sk-1234567890abcdef"
    # Act
    result = mask_api(key)
    # Assert
    assert "****" in result
