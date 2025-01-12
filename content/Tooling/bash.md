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

More examples: https://www.cyberciti.biz/faq/bash-for-loop/

Пример:

```bash
for i in {1..6}; do curl http://localhost:4000/v1/healthcheck; done
```

### Infinite loop

```bash
for (( ; ; ))
do
   echo "infinite loops [ hit CTRL+C to stop]"
done
```

## Add Numbers

```bash
num=$((num1 + num2))
num=$(($num1 + $num2))       # Also works
num=$((num1 + 2 + 3))        # ...
num=$[num1+num2]             # Old, deprecated arithmetic expression syntax
```



----
📂 [[Tooling]] | Последнее изменение: 11.01.2025 19:12