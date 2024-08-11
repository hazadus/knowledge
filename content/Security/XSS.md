📁 [[Security]]

----
**XSS** – Cross-Site Scripting. Виды атак:
- Отраженные (reflected): например, мы через форму засылаем на сайт JS-код, он рендерится и при этом выполняется.
- Хранимые (stored): например, вставляем в коммент `<img src="..." onLoad="..." />`.
- Атаки на DOM: если родной JS-код например парсит адресную строку и берет оттуда что-то, можно вставить вредоносный код в адресную строку.

## References
- [XSS Game](https://xss-game.appspot.com/level1)
- [XSS prevention for Flask](https://semgrep.dev/docs/cheat-sheets/flask-xss/)
- [XSS prevention for Django](https://semgrep.dev/docs/cheat-sheets/django-xss/)
- [HTTP **`Content-Security-Policy`** response header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Security-Policy)



----
📂 [[Security]]