**AWK** ([ɔːk] is a [domain-specific language](https://en.m.wikipedia.org/wiki/Domain-specific_language "Domain-specific language") designed for text processing and typically used as a [data extraction](https://en.m.wikipedia.org/wiki/Data_extraction "Data extraction") and reporting tool. Like [sed](https://en.m.wikipedia.org/wiki/Sed "Sed") and [grep](https://en.m.wikipedia.org/wiki/Grep "Grep"), it is a [filter](https://en.m.wikipedia.org/wiki/Filter_(software) "Filter (software)"), and is a standard #cli feature of most [Unix-like operating systems](https://en.m.wikipedia.org/wiki/Unix-like "Unix-like").

The AWK language is a [data-driven](https://en.m.wikipedia.org/wiki/Data-driven_programming "Data-driven programming") [scripting language](https://en.m.wikipedia.org/wiki/Scripting_language "Scripting language") consisting of a set of actions to be taken against [streams](https://en.m.wikipedia.org/wiki/Stream_(computing) "Stream (computing)") of textual data – either run directly on files or used as part of a [pipeline](https://en.m.wikipedia.org/wiki/Pipeline_(Unix) "Pipeline (Unix)") – for purposes of extracting or transforming text, such as producing formatted reports.

----
Допустим, есть текстовый файл `info.txt` следующего содержания:

```
fristName       lastName        age     city       ID

Thomas          Shelby          30      Rio        400
Omega           Night           45      Ontario    600
Wood            Tinker          54      Lisbon     N/A
Giorgos         Georgiou        35      London     300
Timmy           Turner          32      Berlin     N/A
```

## Вывод нужных строк и колонок

Вывести содержимое файла с нумерацией строк:
```shell
awk '{print NR,$0}' info.txt
```

Вывести только первую колонку файла:
```bash
awk '{print $1}' info.txt
```

Для вывода второй колонки использовать `$2`, и т.д. По умолчанию, колонки определяются по пробелам.

Можно вывести несколько колонок:
```bash
awk '{print $1, $4}' info.txt
```

Вывести только крайнюю правую колонку:
```bash
awk '{print $NF}' info.txt
```

Вывести только первую строку, первую колонку:
```shell
awk '{print $1}' info.txt | head -1
```

Вывести первые три строки, первую колонку:
```shell
awk '{print $1}' info.txt | head -3
```

## Вывод строк по RegExp

Вывод строк, начинающихся на `O`:
```bash
awk '/^O/' info.txt
```

Вывод строк, завершающихся `0`:
```bash
awk '/0$/' info.txt
```

Можно использовать `!` в качестве отрицания – вывести строки, НЕ заканчивающиеся на `0`:
```bash
awk '! /0$/' info.txt
```

## Операторы сравнения

Вывести только строки, где третья колонка меньше 40:

```bash
awk '$3 <  40 { print $0 }' info.txt
```

----
📂 [[Tooling]]