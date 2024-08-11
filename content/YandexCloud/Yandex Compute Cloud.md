## Создание VM из CLI с запуском установочного скрипта (взято из [практикума](https://practicum.yandex.ru/trainer/ycloud/lesson/397f028f-1e36-4601-83a0-b0291b4b2703/))

Сохранить в `startup.sh`:

```bash
#!/bin/bash
apt-get update
apt-get install -y nginx
service start nginx
sed -i -- "s/nginx/Yandex Cloud - ${HOSTNAME}/" /var/www/html/index.nginx-debian.html
EOF
```

Выполнить команду:

```bash
yc compute instance create \
--name demo-1 \
--hostname demo-1 \
--metadata-from-file user-data=startup.sh \
--create-boot-disk image-folder-id=standard-images,image-family=ubuntu-2004-lts \
--zone ru-central1-a \
--network-interface subnet-name=default-ru-central1-a,nat-ip-version=ipv4
```

Выполняя команду несколько раз с разными `name` и `hostname`, можно насоздавать сколько угодно одинаковых ВМ.

Можно посмотреть список всех запущенных ВМ:

```bash
yc compute instance list
```



----
📂 [[YandexCloud]]