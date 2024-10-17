`cloc` = Count Lines of Code

`cloc` counts blank lines, comment lines, and physical lines of source code in many programming languages.

https://github.com/AlDanial/cloc

----

`cloc .`

```
github.com/AlDanial/cloc v 2.02  T=0.14 s (313.8 files/s, 24744.7 lines/s)
-------------------------------------------------------------------------------
Language                     files          blank        comment           code
-------------------------------------------------------------------------------
Go                              30            443            305           2084
Markdown                         5             97              0            375
YAML                             5              6              4            138
SQL                              2              4              0             37
make                             1              8              8             28
Dockerfile                       1              0              0              7
Bourne Shell                     1              0              0              4
-------------------------------------------------------------------------------
SUM:                            45            558            317           2673
-------------------------------------------------------------------------------
```

```bash
cloc --fullpath --not-match-d="(.venv|.pytest_cache|htmlcov|celerybeat-schedule|temp)" .
```

```bash
cloc --fullpath --not-match-d="(node_modules|App/ios|App/android)" --not-match-f="(yarn\.lock|package\.json|package\-lock\.json)" .
```

----
📂 [[Tooling]] | Последнее изменение: 04.10.2024 19:52