`chmod a+x ./run.sh`
в файле / shebang:
`#!/bin/bash`
`…`

## Сгенерить случайный пароль

20 символов:

```bash
LC_ALL=C tr -dc 'A-Za-z0-9@#%^&*()_+=-{}[]:;<>,.?/' \
    < /dev/urandom | head -c 20 | xargs echo
```

## Цикл `for`

Пример:

```bash
for i in {1..6}; do curl http://localhost:4000/v1/healthcheck; done
```

----
📂 [[Tooling]] | Последнее изменение: 01.12.2024 13:53