---

---
**hey** - HTTP load generator, formerly known as `rakyll/boom`.

```bash
# Отправить 200 запросов (количество по умолчанию)
BODY='{"email": "hazadus7@gmail.com", "password": "12345678"}'
hey -d "$BODY" -m "POST" https://my.api.ru/v1/users/login
```

```bash
# Запросы с аутентификацией, 1000 штук
hey -H 'accept: application/json' \
	-H 'X-Authorization: token_value' \
	-n 1000 \
	'https://my.api.net/api/v1/endpoint'
```

[man page](https://manpages.ubuntu.com/manpages/focal/man1/hey.1.html)

----
#DevTools 

----
📂 [[Tooling]] | Последнее изменение: 07.01.2025 16:22