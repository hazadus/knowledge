Для этого в корне проекта я создаю .env файл вот с такой строкой

```
PYTHONPATH=/Users/chrnmaxim/Projects/MiniApp_v2:${PYTHONPATH}
```

И также в корне проекта создаю .vscode/settings.json с такими параметрами

```json
{
    "terminal.integrated.env.osx": {
        "PYTHONPATH": "/Users/chrnmaxim/Projects/MiniApp_v2"
    },
}
```

```bash
export PYTHONPATH=/Users/hazadus/Projects/MiniApp_v2:${PYTHONPATH}
```



----
📂 [[Python]] | Последнее изменение: 28.01.2025 18:27