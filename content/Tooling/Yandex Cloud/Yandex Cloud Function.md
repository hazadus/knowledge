## Создаём функцию

Команды перечислены тут: https://github.com/yandex-cloud-examples/yc-practicum-serverless-telegram-bot/blob/main/steps/03-first-bot-function/README.md

```bash
yc serverless function create --name first-bot-function
```

Загружаем код. В окрежении должны быть верно установлены переменные `SERVICE_ACCOUNT_DEPLOY_ID`, `TELEGRAM_BOT_TOKEN`.

```bash
yc serverless function version create \
--function-name first-bot-function \
--memory 128m \
--execution-timeout 5s \
--runtime python311 \
--entrypoint index.handler \
--service-account-id $SERVICE_ACCOUNT_DEPLOY_ID \
--environment TELEGRAM_BOT_TOKEN=$TELEGRAM_BOT_TOKEN \
--source-path index.py
```

После этого, функция появится в консоли. Также можно получить список функций:

```bash
yc serverless function list
```

Получить инфу о функции:

```bash
yc serverless function version list --function-name first-bot-function
```

В результате вызова последней команды в столбце `FUNCTION ID` вы узнаете идентификатор функции и сможете сделать вызов функции с помощью следующей команды:

```bash
yc serverless function invoke <идентификатор функции>
```

По умолчанию функция создается не публичной. Чтобы сделать функцию `first-bot-function` публичной, вызовете следующую команду:

```bash
yc serverless function allow-unauthenticated-invoke first-bot-function
```

Получить URL функции:

```bash
yc serverless function get first-bot-function
```

## Создаём API Gateway

Настраиваем конфиг `first-bot-apigw.yml`:

```yaml
openapi: 3.0.0
info:
  title: first-bot-apigw
  version: 1.0.0
paths:
  /forwebhook:
    post:
      x-yc-apigateway-integration:
        type: cloud-functions
        function_id: <идентификатор функции>
        service_account_id: <ID сервисного аккаунта>
      operationId: first-bot-function
```

В конфиге указан путь, метод, и какую функцию вызывать для обработки этого запроса.

После внесения изменений в спецификацию `first-bot-apigw.yml`, используем ее для инициализации:

```bash
yc serverless api-gateway create \
--name first-bot-apigw \
--spec=first-bot-apigw.yml \
--description "first-bot-apigw"
```

В консоли увидим, в том числе, имя служебного домена гейтвея.

```bash
yc serverless api-gateway list
yc serverless api-gateway get --name first-bot-apigw
```

Служебный домен нужен нам для того, чтобы соединить нашу функцию и телеграм, Согласно нашей спецификации, функция будет доступна по адресу если в конце `domain` дописать `/forwebhook`. Должно получиться следующее:

```
https://<ID API Gateway>.apigw.yandexcloud.net/forwebhook
```

Сохраним полученный URL в переменную `TELEGRAM_BOT_URL`.

```bash
echo "export TELEGRAM_BOT_URL=https://d5dvar0dnmvu6kt1uujs.apigw.yandexcloud.net/forwebhook" >> ~/.bashrc && . ~/.bashrc
echo $TELEGRAM_BOT_URL
```

## Деплой новой версии функции

Взято отсюда: https://github.com/yandex-cloud-examples/yc-practicum-serverless-telegram-bot/blob/main/steps/06-update-function/README.md

Сначала создадим архив с нужным кодом:  `zip src.zip index.py requirements.txt

Чтобы передеплоить функцию с новыми параметрами, находясь в директории с архивом, вызовем следующую команду, не забыв подставить свои значения `id` и `version-id`:

```bash
yc serverless function version create \
--function-name first-bot-function \
--memory 128m \
--execution-timeout 5s \
--runtime python311 \
--entrypoint index.handler \
--service-account-id $SERVICE_ACCOUNT_DEPLOY_ID \
--secret environment-variable=TELEGRAM_BOT_TOKEN,id=e6qbrqvn8jv0gtfhkr5q,version-id=e6qej8pukfhq94petq0t,key=TELEGRAM_BOT_TOKEN \
--secret environment-variable=YDB_ENDPOINT,id=e6qbrqvn8jv0gtfhkr5q,version-id=e6qej8pukfhq94petq0t,key=YDB_ENDPOINT \
--secret environment-variable=YDB_DATABASE,id=e6qbrqvn8jv0gtfhkr5q,version-id=e6qej8pukfhq94petq0t,key=YDB_DATABASE \
--source-path src.zip
```