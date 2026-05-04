---
description: |
  [TOPIC] scitex-str Installation
  [DETAILS] pip install scitex-str (pure Python, no extras); smoke verify with import + version.
tags: [scitex-str-installation]
---

# Installation

## Standard

```bash
pip install scitex-str
```

Pure-Python; no required runtime dependencies. The LaTeX-fallback path
will use matplotlib mathtext or unicode when a real LaTeX install is
unavailable — no system TeX is required for the package to import.

## Verify

```bash
python -c "import scitex_str; print(scitex_str.__version__)"
python -c "from scitex_str import printc, color_text, to_latex_style, latex_to_mathtext; print('ok')"
```

## Editable install (development)

```bash
git clone https://github.com/ywatanabe1989/scitex-str
cd scitex-str
pip install -e '.[dev]'
```

## Umbrella alternative

```bash
pip install scitex   # exposes scitex.str as a submodule
```

See SKILL.md for the standalone-vs-umbrella import rule.
