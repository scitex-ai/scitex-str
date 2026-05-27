# Changelog

All notable changes to `scitex-str` are documented here.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/);
versions follow [Semantic Versioning](https://semver.org/).

## [Unreleased]

## [0.1.12]

- Refactor: promote flat modules into topical subpackages (`_ansi/`, `_case/`, `_latex/`, `_mask/`, `_plot/`, `_print/`, `_search/`).
- CI: normalize codecov.yml to canonical shape.
- Fix(deps): scitex-dev pin floor to 0.11.7.

## [0.1.11]

- Fix(docs): docs workflow installs `[dev]` not removed `[docs]` extra.

## [0.1.10]

- Fix(workflows): resync integrated release pipeline from scitex-dev v0.11.20.

## [0.1.9]

- CI: sync GitHub Releases with PyPI publish.
- Chore(deps): bump scitex-dev pin floor to 0.11.7.
- Fix(release-safety): opt-in publish-pypi.yml (workflow_dispatch only).

## [0.1.8]

- Chore(version): switch `__version__` to importlib.metadata to prevent drift.

## [0.1.7]

- Initial CHANGELOG entry — see git log for prior history.
