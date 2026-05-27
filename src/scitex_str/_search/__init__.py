"""Pattern matching, parsing, and string substitution."""

from ._grep import grep
from ._parse import parse
from ._replace import replace
from ._search import search

__all__ = ["grep", "parse", "replace", "search"]
