Начал читать 22 мая 2024 г.
## Интересные фичи, рассмотренные в книге

Что нашел интересного для своих проектов во введении книги:

- **Chapter 2**: send emails with Django, and handle forms and model forms. You will also implement a comment system for blog posts.
- **Chapter 3**: build complex QuerySets to recommend similar posts; search engine using PostgreSQL’s full-text search capabilities.
- **Chapter 5**: Covers implementing social authentication and using the messages framework; how to use `django-extensions` to run the development server through HTTPS and customize the social authentication pipeline to automate the user profile creation.
- **Chapter 6**: how to generate image thumbnails; implement infinite scroll pagination.
- **Chapter 7**: implementing following system; user activity stream application; count image views and you will create a ranking of the most viewed images with Redis.
- **Chapter 8**: online shop, cart via sessions, Celery, asynchronous notifications...
- **Chapter 9**: export to CSV, PDF.
- **Chapter 10**: use Redis to store products that are usually bought together, and use this information to build a product recommendation engine.
- Chapter 11
- Chapter 12
- **Chapter 13**: use the Django groups and permissions system to restrict access to views and implement formsets to edit the content of courses. You will also create a drag-and-drop functionality to reorder course modules and their content using JavaScript.
- **Chapter 14**: how to cache content using the Django cache framework and configure the Memcached and Redis cache backends for your project. Finally, you will learn how to monitor Redis using the administration site.
- **Chapter 15**: building REST API
- ✅ **Chapter 16**: building Chat Server
- **Chapter 17**: deploy; how to use Django systems check framework.

----
## Впечатления
### Глава 1
Совсем забыл, что можно использовать вызовы типа `User.objects.get(email="...")`, обычно пользуюсь `.filter(...).first()`. `get()` выбрасывает исключения если ничего не находит, или находит несколько строк, что удобно. И ещё есть `get_or_create()`. В атрибуте `query` (не является частью публичного API!) у `QuerySet` находится соответствующий SQL-запрос, его можно вывести и изучить. Очень хорошо описано использование field lookups, это мощнейшая вещь в Django ORM. Фильтры можно чейнить. Это важно помнить, мне это очень пригодилось как раз недавно в проекте. Можно чейнить `filter().exclude()`. Отсортировать по рандому можно `order_by('?')`.

### Глава 2
Template filter для поддержки Markdown.

## Глава 5
[easy-thumbnails](https://github.com/SmileyChris/easy-thumbnails). Infinite page scrolling with vanilla JS.

### Глава 16
Глава 16, просто огонь! Отличный чат, простой, при этом полнофункциональный, и его можно развивать дальше. По аналогии, сделал чат в своём приложении. В 17 главе хорошо рассказано, как это всё задеплоить, она тоже помогла!

----
📂 [[Reading]]