> [!info] Markup Validation Service  
> W3C's easy-to-use markup validation service, based on SGML and XML parsers.  
> [https://validator.w3.org/](https://validator.w3.org/)  
# Служебные теги
[https://developer.mozilla.org/ru/docs/Web/HTML/Element/meta](https://developer.mozilla.org/ru/docs/Web/HTML/Element/meta)
```HTML
<!DOCTYPE html>
<html lang="ru"><!-- Для переводчика и читалок -->
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1">
		<title>Title</title>
	</head>
	<body>
	</body>
</html>
```
# Базовые теги

> [!info]  
>  
> [https://webref.ru/layout/learn-html-css/getting-to-know-html](https://webref.ru/layout/learn-html-css/getting-to-know-html)  

> [!info] Справочник HTML  
> HTML (HyperText Markup Language, язык разметки гипертекста) - это система вёрстки, которая определяет, как и какие элементы должны располагаться на веб-странице.  
> [https://webref.ru/html](https://webref.ru/html)  

> [!info]  
>  
> [https://html5book.ru/html-html5/](https://html5book.ru/html-html5/)  
## Заголовки
Всего 6 уровней – h1…h6.
`<h1>` – должен быть один на страницу и содержать её основной смысл (важно для поисковиков).
## Блочные и строчные тэги
Блочные идут отдельным блоком, например `<h1>`, `<p>`. Блок занимает всю доступную ему ширину. Строчные идут внутри строки, например `<a>`, `<em>`.
## anchor
[https://developer.mozilla.org/ru/docs/Web/HTML/Element/A](https://developer.mozilla.org/ru/docs/Web/HTML/Element/A)
[https://css-tricks.com/a-complete-guide-to-links-and-buttons/](https://css-tricks.com/a-complete-guide-to-links-and-buttons/)
`<a href=”#” download>` – Этот атрибут сообщает о том, что эта ссылка должна быть использована для скачивания файла, и, когда пользователь нажимает на ссылку, ему будет предложено сохранить файл как локальный. Если у этого атрибута есть значение, оно будет использовано как заполненное название файла в Окне сохранения, которое открывается, когда пользователь нажимает на ссылку (пользователь может поменять название перед сохранением файла).
## button
[https://css-tricks.com/a-complete-guide-to-links-and-buttons/](https://css-tricks.com/a-complete-guide-to-links-and-buttons/)
## Выделение жирным, курсивом
`<i>`, `<b>` – декоративное выделение.
`<em>`, `<strong>` – также и смысловое выделение, важно для поисковиков, голосовых читалок.
## Цитаты
`<q>` – текст цитаты. Кавычки ставятся при этом браузером автоматически.
`<cite>` – имя автора.
## Иллюстрация
[https://developer.mozilla.org/ru/docs/Web/HTML/Element/figure](https://developer.mozilla.org/ru/docs/Web/HTML/Element/figure)
`<figure>` – группирующий тэг.
`<figcaption>` – описание контента, необязательный текст.
```HTML
<figure>
	<img src="" alt="">
	<figcaption>...</figcaption>
</figure>
```
## Списки
### ul / ol
[https://developer.mozilla.org/ru/docs/Web/HTML/Element/ol](https://developer.mozilla.org/ru/docs/Web/HTML/Element/ol)
[https://developer.mozilla.org/ru/docs/Web/HTML/Element/ul](https://developer.mozilla.org/ru/docs/Web/HTML/Element/ul)
### li
[https://developer.mozilla.org/ru/docs/Web/HTML/Element/li](https://developer.mozilla.org/ru/docs/Web/HTML/Element/li)
## Таблицы
[https://developer.mozilla.org/ru/docs/Learn/HTML/Tables/Basics](https://developer.mozilla.org/ru/docs/Learn/HTML/Tables/Basics)
`<caption>` – заголовок таблицы.
`<thead><tr><th>…</th></tr></thead>` – названия столбцов
`<tbody>` – сама таблица
`<tfoot>` – итоги или примечания таблицы.
# Прочие
`<pre>` – учитывать пробелы, табуляцию
`<code>` – код
`<pre><code>` – код + сохранение табуляций
`<sub>` – нижний индекс
`<sup>` – верхний индекс (степень)
`<s>` – зачеркнутый (strikethru)
`<abbr title=”World Wide Web”>`WWW`</abbr>` – аббревиатуры
`<wbr>` – предпочтительные точки переноса в длинных, сложносоставных словах (_только_ когда не хватает ширины экрана!)