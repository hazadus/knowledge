Для исключения SQL-инъекции, используем параметризованный SQL-запрос в Python (заодно тут показано, как выполнить вставку нескольких строк из списка):

```python
def add_characters_to_database(characters: list[Character]) -> None:
    with sqlite3.connect(DATABASE_FILENAME) as conn:
        cursor = conn.cursor()
        cursor.executemany(
            """
            INSERT INTO characters(name, gender, birth_year)
            VALUES ($1, $2, $3)
            """,
            [(ch.name, ch.gender, ch.birth_year) for ch in characters],
        )
```

----
📂 [[SQL]] | Последнее изменение: 30.01.2024 17:40