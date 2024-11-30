An extremely fast Python linter and code formatter, written in Rust.

Docs (formatter): https://docs.astral.sh/ruff/formatter/

----
## [Sorting imports](https://docs.astral.sh/ruff/formatter/#sorting-imports)

Currently, the Ruff formatter does not sort imports. In order to both sort imports and format, call the Ruff linter and then the formatter:

```bash
ruff check --select I --fix
ruff format
```



----
📂 [[Tooling]] | Последнее изменение: 30.11.2024 09:24