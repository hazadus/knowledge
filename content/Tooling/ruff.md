An extremely fast Python linter and code formatter, written in Rust.

Docs (formatter): https://docs.astral.sh/ruff/formatter/

----
## [Sorting imports](https://docs.astral.sh/ruff/formatter/#sorting-imports)

Currently, the Ruff formatter does not sort imports. In order to both sort imports and format, call the Ruff linter and then the formatter:

```bash
ruff check --select I --fix
ruff format
```

---
## Check and Fix Unused Imports

```bash
# Check
uv run ruff check . && uv run ruff check --select I . && uv run ruff format --check .

# Fix
uv run ruff check --fix . && uv run ruff check --fix --select I . && uv run ruff format .
```

----
📂 [[Tooling]] | Последнее изменение: 19.01.2025 11:10