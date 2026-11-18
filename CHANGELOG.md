# Changelog

All notable changes to `scitex-str` are documented here.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/);
versions follow [Semantic Versioning](https://semver.org/).

## [Unreleased]

## [0.1.13] - 2026-11-18

- Perf: `import scitex_str` no longer imports pandas / xarray (0.4–1.5 s, paid by every `@stx.session` start-up). `search()` recognises `pandas.Series` / `pandas.Index` / `xarray.DataArray` inputs whenever the caller has imported those packages (read from `sys.modules`; an object of their type cannot exist otherwise).
- Fix(audit): audit-all green. `printc` / `print_block` write via the scitex-logging plain console (same stdout bytes); matplotlib imports gated by `try_import_optional` (`smart_tick_formatter` now raises an `ImportError` with the `[all]` install hint instead of failing on a bare import); cross-package import test skips on the root and hard-imports the full path; CLA caller passes only the named PAT and an explicit hosted runner; CI installs one explicit `[all,dev]` profile with no fallback chain.
- Fix(docs): restore the `[docs]` extra (allowed by PS-225) so the org `rtd-sphinx-build` workflow installs sphinx; the skills-quality test now points at the repo root instead of `tests/` (it was silently skipping).
- Fix(deps): `scitex-logging>=0.2.2` (PlainConsole stdout handling).

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
