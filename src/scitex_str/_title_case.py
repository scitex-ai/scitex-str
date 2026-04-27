#!/usr/bin/env python3
# Timestamp: 2026-04-27
# File: /home/ywatanabe/proj/scitex-str/src/scitex_str/_title_case.py

"""Title case conversion — thin wrapper over the `titlecase` PyPI package.

We delegate to `titlecase` (Stuart Colville's implementation of the
NYT Manual of Style) and supply a small callback for technical acronyms
that the upstream package doesn't recognise out of the box (AI, ML, GPU,
3D, APIs, …). This keeps grammar/edge-case handling outside our codebase
where it belongs.
"""

from __future__ import annotations

import re

from titlecase import set_small_word_list
from titlecase import titlecase as _titlecase

# Extend `titlecase`'s default SMALL list (a|an|and|as|at|but|by|en|for|if|in|
# of|on|or|the|to|v.?|via|vs.?) with stopwords the SciTeX docs/tests
# expect to remain lowercase. ``nor`` and ``with`` aren't in the upstream
# default — adding them keeps behaviour consistent with the previous in-tree
# implementation that the test suite was written against.
set_small_word_list(
    "a|an|and|as|at|but|by|en|for|if|in|nor|of|on|or|the|to|v\\.?|via|vs\\.?|with"
)

# Technical acronyms common in the SciTeX domain that should be uppercase
# even if the input was lowercase. Stored lower-cased for matching.
_ACRONYMS: set[str] = {
    # Computing / web
    "api",
    "url",
    "uri",
    "cpu",
    "gpu",
    "tpu",
    "ram",
    "io",
    "os",
    "vm",
    "ip",
    "tcp",
    "udp",
    "http",
    "https",
    "html",
    "css",
    "js",
    "ts",
    "json",
    "xml",
    "yaml",
    "csv",
    "pdf",
    "sql",
    "db",
    "rest",
    "ci",
    "cd",
    "cli",
    "ide",
    "ssh",
    "ssl",
    "tls",
    "id",
    "uuid",
    # ML / AI
    "ai",
    "ml",
    "dl",
    "nlp",
    "lstm",
    "gru",
    "cnn",
    "rnn",
    "gan",
    "vae",
    # Bio / signal
    "eeg",
    "ecg",
    "mri",
    "fmri",
    "ct",
    "pet",
    "iqr",
    "rms",
    "snr",
}

# 3D / 2D / 4K etc. — number followed by 1-3 letters that's typically an acronym.
_NUMBERED_ACRONYM = re.compile(r"^\d+[a-zA-Z]{1,3}$")


def _acronym_callback(word: str, **_kwargs) -> str | None:
    """Callback for `titlecase` — return the desired form, or None to defer.

    Handles:
    - Plural acronyms: ``apis`` → ``APIs`` (uppercase root + lowercase 's').
    - Bare acronyms: ``ai`` → ``AI``.
    - Numbered acronyms: ``3d`` → ``3D``.
    """
    lower = word.lower()
    if lower in _ACRONYMS:
        return lower.upper()
    if lower.endswith("s") and lower[:-1] in _ACRONYMS:
        return lower[:-1].upper() + "s"
    if _NUMBERED_ACRONYM.match(word):
        return word.upper()
    return None  # let titlecase handle it


def title_case(text: str) -> str:
    """Convert a string to title case (NYT Manual of Style + SciTeX acronyms).

    Examples
    --------
    >>> title_case("welcome to the world of ai and using CPUs for gaming")
    'Welcome to the World of AI and Using CPUs for Gaming'

    >>> title_case("3d printing")
    '3D Printing'

    >>> title_case("the cat")
    'The Cat'
    """
    return _titlecase(text, callback=_acronym_callback)


# EOF
