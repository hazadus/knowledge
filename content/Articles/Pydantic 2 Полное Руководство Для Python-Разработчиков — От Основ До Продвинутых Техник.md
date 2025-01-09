# Pydantic 2: Полное Руководство Для Python-Разработчиков — От Основ До Продвинутых Техник

![rw-book-cover](https://habrastorage.org/getpro/habr/upload_files/1d2/de0/023/1d2de0023eaecba2f96915c2fbad1d6f.png)

## Metadata
- Author: [[Хабр]]
- Full Title: Pydantic 2: Полное Руководство Для Python-Разработчиков — От Основ До Продвинутых Техник
- Category: #articles
- Document Tags: [[pydantic]] 
- Summary: Pydantic 2 is a powerful library for Python developers that helps validate and transform data. It allows for easy customization of data models and supports features like inheritance and validation of input parameters. Practicing with Pydantic 2 will enhance your projects and improve data consistency.
- URL: https://habr.com/ru/companies/amvera/articles/851642/

## Highlights
- `@computed_field` — поле, которое вычисляется на основе других данных в модели. Его можно использовать для автоматической генерации значений, а также для валидации. ([View Highlight](https://read.readwise.io/read/01jes3p08fccfphvqxjejefv8g))

- Декоратор `field_validator` служит для проверки корректности заполнения полей модели Pydantic. Помимо валидации, его можно использовать для преобразования данных перед их сохранением в модели. ([View Highlight](https://read.readwise.io/read/01jes3v7vv6wvze59fk6kzes7y))

- Валидатор модели (model_validator) в Pydantic
  В старых версиях Pydantic этот декоратор назывался `root_validator`. Его основное назначение — валидация модели **в целом**, после того как все поля уже прошли индивидуальную проверку. Это позволяет выполнять комплексные проверки, зависящие от нескольких полей модели одновременно.
  Основные особенности декоратора @model_validator:
  • Выполняется после валидации отдельных полей.
  • Имеет доступ ко всем полям модели одновременно.
  • Может изменять значения полей или всю модель целиком.
  • Используется для сложных проверок, связанных с несколькими полями. ([View Highlight](https://read.readwise.io/read/01jes3y9fxz7ctzh18rg3q34ta))

- 3. regex — для проверки по регулярному выражению
  Этот валидатор позволяет проверять строковые значения **на соответствие регулярному выражению**. Регулярные выражения (regex) дают возможность гибко описывать допустимые форматы строк — например, для проверки адресов электронной почты, телефонных номеров, форматов дат и т. д.
  • `regex`: Задаёт регулярное выражение, которому должна соответствовать строка.Пример: `Field(regex=r"[^@]+@[^@]+\.[^@]+")` — проверка, что строка является корректным email-адресом. ([View Highlight](https://read.readwise.io/read/01jes43c30jf8datwd1ttzy4h6))

- Вместо того чтобы писать:
  class MyModel(BaseModel): class Config: from_attributes = True
  теперь используем **ConfigDict**:
  from pydantic import BaseModel, ConfigDictclass MyModel(BaseModel): model_config = ConfigDict(from_attributes=True) ([View Highlight](https://read.readwise.io/read/01jes4sc26dx0mkcbegfx1zhbs))





----
📂 [[Articles]] | Последнее изменение: 19.12.2024 14:22