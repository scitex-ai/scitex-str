"""Console printing helpers (block borders, colored print, debug banner)."""

# `_print_block.py` and `_printc.py` both define `printc`; the historical
# package-level behaviour was that `_printc.printc` shadowed `_print_block.printc`.
# Preserve that by importing `_printc.printc` last.
from ._print_debug import print_debug
from ._printc import printc

__all__ = ["print_debug", "printc"]
