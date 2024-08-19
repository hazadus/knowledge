Инструмент для автоматизированного тестирования API по стандарту OpenAPI. См. книгу Любановича, стр. 198.

## References

- [Testing with authentication](https://schemathesis.readthedocs.io/en/stable/auth.html)

## Setup

```bash
poetry add --group dev hypothesis
poetry add --group dev schemathesis
```

## Usage

Пример использования с FastAPI ([репо](https://gitverse.ru/amgold/fastapi-learn/content/master/cryptids)):

```bash
schemathesis run http://localhost:8000/openapi.json --experimental=openapi-3.1
```


----
📂 [[Tooling]] | Последнее изменение: 08.04.2024 18:11