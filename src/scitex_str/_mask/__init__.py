"""Secret-masking helpers (API keys, credentials)."""

# `_mask_api.py` (`n`-configurable variant) and `_mask_api_key.py` (fixed
# 4-char variant) both export `mask_api`. The historical package-level
# behaviour was that `_mask_api_key.mask_api` shadowed `_mask_api.mask_api`;
# preserve that by importing `_mask_api_key` last.
from ._mask_api_key import mask_api

__all__ = ["mask_api"]
