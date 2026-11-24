# TOFIX

Findings from a code scan on 2026-10-04.

## Medium

- `src/pyapikey/core.py:13` - `old_get_key()` is a leftover that reads keys from a plaintext `~/.config/pyapikey.json`, contradicting the pass-only design of `get_key()`; nothing in the fleet calls it - delete it.
- `src/pyapikey/core.py:55` - `TempStore` is unused anywhere in the fleet and writes `~/.config/pyapikey.temp.json` with default (umask, usually world-readable) permissions from a package whose purpose is handling secrets; delete it, or if it is kept, create the file with mode 0600.
- `tests/unit_tests/test_basic.py:10` - the only test is an empty `pass`, so `get_key()` is never exercised; add a test that mocks `subprocess.Popen` for the success and failure paths.
- `pyproject.toml:88` - `[[tool.mypy.overrides]]` sets `ignore_missing_imports` for `pyapikey.*`, i.e. the package itself, which is not a third-party library without stubs; remove the override (and fix any resulting mypy errors).

## Low

- `src/pyapikey/core.py:30` - docstring says `Raises: Exception` but the function raises `ValueError` (line 39); document the actual exception.
- `pyproject.toml:83` - `mypy_path = "src:python:scripts"` names `python/` and `scripts/` directories that do not exist in this repo; reduce it to `src`.
- `rsconstruct.toml:28` - `[processor.ruff]` and `[processor.mypy]` (line 32) list `config` in `src_dirs`, but `config/` holds only `.lua` files; drop it.
- `doc/TODO.txt:1` - the file is empty; delete it.
