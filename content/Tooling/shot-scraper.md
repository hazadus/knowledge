Docs: https://shot-scraper.datasette.io/en/stable/installation.html

```bash
pip install shot-scraper
# Скачает браузер, 200+ Мб:
shot-scraper install

# Сделать скрин шириной 1280px в полную высоту:
shot-scraper https://hazadus.ru --width 1280

# Сделать скрин шириной 1280px в полную высоту с ожиданием 10 сек,
# чтобы все элементы загрузились:
shot-scraper https://hazadus.ru/blogroll --width 1280 --wait 10000
```

Пример файла `multi.yml`:

```yml
- output: hazadus.ru.png
  url: https://hazadus.ru/
  width: 1280
  wait: 500
- output: anvlink.ru.png
  url: https://anvlink.ru/
  width: 1280
  wait: 500
- output: speakers24.ru.png
  url: https://speakers24.ru/
  width: 1280
  wait: 500
- output: nameapp.anverali.tech.png
  url: http://nameapp.anverali.tech/
  width: 1280
  wait: 500
- output: knowledge.png
  url: https://hazadus.github.io/knowledge/
  width: 1280
  wait: 500
```

Делаем скрины по списку в файле:

```bash
shot-scraper multi shots.yml
```

----
📂 [[Tooling]] | Последнее изменение: 09.12.2024 15:10