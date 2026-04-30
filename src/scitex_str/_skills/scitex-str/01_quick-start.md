---
name: quick-start
description: scitex-str — Quick Start — see file body for details.
tags: [scitex-str, scitex-package]
---

<!-- 01_quick-start.md -->

# scitex-str — Quick Start

## Install

```bash
pip install scitex-str
```

## Import

```python
from scitex_str import printc, color_text, readable_bytes, grep, to_latex_style
```

## Usage

### Colored console print (block-style)

```python
from scitex_str import printc

printc("Training started", c="green")
```

### Human-readable byte count

```python
from scitex_str import readable_bytes

readable_bytes(1_536_000)    # '1.5 MB'
```

### Grep-like search over a list of strings

```python
from scitex_str import grep

lines = ["alpha=1", "beta=2", "alpha=3"]
matches = grep(lines, r"^alpha")
# returns matched lines
```

### Safe LaTeX conversion with unicode fallback

```python
from scitex_str import safe_to_latex_style

label = safe_to_latex_style("alpha_1")
# Returns a LaTeX-style string if LaTeX is available,
# otherwise the unicode/mathtext equivalent.
```
