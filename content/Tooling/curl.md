📂 [[Tooling]]

Reference: https://everything.curl.dev/index.html

----
## Примеры запросов

- Отправка GET-запроса: `curl <URL>`
- Отправка GET-запроса с параметрами: `curl "<URL>?param1=value1&param2=value2"`
- Follow redirect: `-L` aka `--location`
- Отправка POST-запроса с данными в теле запроса: `curl -d "data" <URL>`
- Отправка POST-запроса с данными в теле запроса в формате JSON: `curl -H "Content-Type: application/json" -d '{"key": "value"}' <URL>`

### Sending Curl Request with Bearer Token

```bash
curl https://reqbin.com/echo/get/json \
  -H "Accept: application/json" \
  -H "Authorization: Bearer {token}"
```
### Запрос с cookie

```bash
curl -X 'POST' \
  'https://bbah8njcdanroda7498u.containers.yandexcloud.net/api/v1/vacancies' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
--cookie "access_token=Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxNzA0N2RhMi02ZGY5LTRkZjYtODQwMi0zZGNjZmI0NmFiNGUiLCJleHAiOjE3MjMxMzk0OTl9.XWGEXR6w2afbRQz5GXp4HWlLjN-nuDsVfZxfx9d4F50" \
  -d '{
  "title": "Python-developer",
  "preview_text": "Python-developer",
  "content": "Python-developer",
  "salary": 10000,
  "experience": 1,
  "type": "string",
  "published_at": "2024-08-08T17:31:03.689666Z"
}'
```


----
📂 [[Tooling]] | Последнее изменение: 23.11.2024 23:33