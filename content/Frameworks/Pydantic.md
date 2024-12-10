В Pydantic 2 конфигурация моделей теперь задаётся через `ConfigDict`, а не через старый формат с классом `Config`.

```python
from pydantic import BaseModel, ConfigDict

class MyModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)
```

## References

- https://habr.com/ru/companies/amvera/articles/851642
- [BugBytes Pydantic Playlist](https://www.youtube.com/playlist?list=PL-2EBeDYMIbQQGc6kiBSm81XspmwVuk-t)
- https://docs.pydantic.dev/2.0/migration/#changes-to-config


----
📂 [[Frameworks]] | Последнее изменение: 10.12.2024 23:42