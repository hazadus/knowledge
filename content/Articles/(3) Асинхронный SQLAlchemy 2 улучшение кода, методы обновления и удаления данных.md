# (3) Асинхронный SQLAlchemy 2: улучшение кода, методы обновления и удаления данных

![rw-book-cover](https://habrastorage.org/getpro/habr/upload_files/dba/434/295/dba434295afaeb8d18dac0df78a5fb48.jpg)

## Metadata
- Author: [[Хабр]]
- Full Title: (3) Асинхронный SQLAlchemy 2: улучшение кода, методы обновления и удаления данных
- Category: #articles
- Document Tags: [[Outline]] [[sqlalchemy]] 
- Summary: The article discusses improvements in using asynchronous SQLAlchemy for updating and deleting data. It emphasizes the importance of understanding previous concepts and introduces universal methods for data manipulation. Additionally, it highlights the benefits of code clarity and efficiency, especially in larger projects.
- URL: https://habr.com/ru/companies/amvera/articles/855740/

## Highlights
- **Управление уровнем изоляции**
  Теперь можно выбирать подходящий уровень изоляции для разных операций:
  • **READ COMMITTED** — для обычных запросов (по умолчанию в PostgreSQL).
  • **SERIALIZABLE** — для финансовых операций, требующих максимальной надежности.
  • **REPEATABLE READ** — для отчетов и аналитики. ([View Highlight](https://read.readwise.io/read/01je8kkn3hf48epgatv7ax1rjx))

- Кроме того, для преобразования данных из SQLAlchemy ORM в модель Pydantic я использовал методы `from_orm()` и `dict()` для создания словаря. В новой версии Pydantic 2 эти методы были переименованы, хотя их прежние названия пока остаются поддерживаемыми:
  • `from_orm()` теперь называется `model_validate()`
  • `dict()` заменён на `model_dump()` ([View Highlight](https://read.readwise.io/read/01je8kt1prc9ervzsjttfv1mnd))





----
📂 [[Articles]] | Последнее изменение: 10.12.2024 14:19