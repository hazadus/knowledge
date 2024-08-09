Взято отсюда: https://github.com/yandex-cloud-examples/yc-practicum-serverless-telegram-bot/blob/main/steps/05-create-lockbox/README.md

---
Создадим секрет с именем `bot-secrets` и поместим пару переменных со значениями `YDB_ENDPOINT` и `YDB_DATABASE`

```bash
yc lockbox secret create --name bot-secrets \
--description "The secrets for the serverless bot" \
--payload "[{'key': 'YDB_ENDPOINT', 'text_value': $YDB_ENDPOINT},{'key': 'YDB_DATABASE', 'text_value': $YDB_DATABASE}]" \
--cloud-id $YC_CLOUD_ID \
--folder-id $YC_FOLDER_ID 
```

Посмотрим конфигурацию секрета `bot-secrets`:

```bash
yc lockbox secret get --name bot-secrets
```

