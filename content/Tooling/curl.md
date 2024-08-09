📂 [[Tooling]]

----
## Cheatsheet
- Отправка GET-запроса: `curl <URL>`
- Отправка GET-запроса с параметрами: `curl "<URL>?param1=value1&param2=value2"`
- Отправка POST-запроса с данными в теле запроса: `curl -d "data" <URL>`
- Отправка POST-запроса с данными в теле запроса в формате JSON: `curl -H "Content-Type: application/json" -d '{"key": "value"}' <URL>`