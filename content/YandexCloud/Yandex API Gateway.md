В основе этого сервиса лежит классический паттерн программирования: внутреннее представление отделено от способа взаимодействовать с ним через прокси. Мы не афишируем нашу реализацию и отдаём наружу некий контракт.

Yandex API Gateway — важная часть serverless-экосистемы в Yandex Cloud. Он позволяет интегрировать компоненты микросервисного приложения и разрозненные API.

По своей сути Yandex API Gateway является управляемым RESTful API. Он находится между внешним пользователем и сервисами, которые обрабатывают запросы этого пользователя. Его основное преимущество — возможность свести в единую точку взаимодействие пользователей с ресурсами, которые расположены как в Yandex Cloud, так и на других серверах. Допустим, у вас есть три сущности:

1. Файлы в Object Storage.
2. Сайт на базе [WordPress](https://ru.wordpress.org/), развёрнутый на виртуальной машине.
3. API, который реализован с помощью Cloud Functions.

API Gateway позволит организовать взаимодействие со всеми тремя ресурсами через обращение к одному домену с единым API. Без него вам бы пришлось самостоятельно разворачивать шлюз или обратный прокси-сервер и администрировать его.

Поскольку API Gateway работает по модели PaaS, он гарантирует доступность вашего API в соответствии с SLA. А ещё HTTP/HTTPS-запросы ваших пользователей будут выполнены вне зависимости от их количества.

Сервис принимает запросы по HTTPS через служебный поддомен `apigw.yandexcloud.net` или через подключение к вашему домену через Certificate Manager, разбирает эти запросы и определяет их путь и параметры. Кроме того, он использует механизм сервисных аккаунтов для подключения к другим сервисам Yandex Cloud.

Созданный API-шлюз может обрабатывать запросы пятью разными способами:

1. Автоматически формировать статический ответ на запрос. Ответ будет разным в зависимости от параметров запроса.
2. Вызывать функцию, созданную в сервисе Yandex Cloud Functions, которая передаёт параметры запроса и возвращает результаты вызова в ответе.
3. Обращаться к сервису Yandex Object Storage, чтобы раздавать статические файлы.
4. Отправлять запрос на другой URL и формировать ответ как есть.
5. Вызывать [ноду DataSphere](https://cloud.yandex.ru/docs/datasphere/concepts/deploy/#python-nodes), развёрнутую в виде отдельного микросервиса.

### Настройка шлюза для доступа к сервисам в облаке

Практика: [https://practicum.yandex.ru/trainer/ycloud/lesson/a50c934d-8ca2-45af-acdb-092dc4bf154a/](https://practicum.yandex.ru/trainer/ycloud/lesson/a50c934d-8ca2-45af-acdb-092dc4bf154a/)

Пример моих настроек для раздачи фронта:

```yaml
openapi: 3.0.0
info:
  title: ServiceName
  version: 1.0.0
paths:

  /:
    get:
      summary: Отдаёт файл index.html
      x-yc-apigateway-integration:
        type: object_storage
        bucket: frontend-dev
        service_account_id: ajed7t6h5cuorqbn3fnn
        object: 'index.html'
  /{filename+}:
    get:
      summary: Отдаёт требуемые статические файлы фронта
      parameters:
        - name: filename
          in: path
          required: true
          schema:
            type: string
      x-yc-apigateway-integration:
        type: object_storage
        bucket: frontend-dev
        service_account_id: ajed7t6h5cuorqbn3fnn
        object: '{filename}'
  /api/{req+}:
    x-yc-apigateway-any-method:
      summary: Передаёт запросы к бэкенду
      parameters:
        - name: req
          in: path
          required: true
          schema:
            type: string
      x-yc-apigateway-integration:
        type: serverless_containers
        service_account_id: ajeob17dm99qqjsi9afi
        container_id: bbah8njcdanroda7498u
        object: '{req}'

```


----
📂 [[YandexCloud]] | Последнее изменение: 15.08.2024 13:26