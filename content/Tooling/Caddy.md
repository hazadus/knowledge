## Установка

Документация: https://caddyserver.com/docs/install

Для Ubuntu:

```bash
sudo apt install -y debian-keyring debian-archive-keyring apt-transport-https 

curl curl -1sLf 'https://dl.cloudsmith.io/public/caddy/stable/gpg.key' | sudo gpg --dearmor -o /usr/share/keyrings/caddy-stable-archive-keyring.gpg

curl -1sLf 'https://dl.cloudsmith.io/public/caddy/stable/debian.deb.txt' | sudo tee /etc/apt/sources.list.d/caddy-stable.list

sudo apt update
sudo apt install caddy
```

## Настройка при помощи `Caddyfile`

Пример:

```
{
	email hazadus7@gmail.com
	admin off
}

postcard.hazadus.ru {
	root * /usr/projects/go-postcard/cards
	file_server browse
	reverse_proxy /v1/* 0.0.0.0:8008
}
```

`email` нужен для автоматизированной работы с SSL сертификатами от Let's Encrypt.

Такая конфигурация настроит работу указанного домена через HTTPS с проксированием всех запросов на указанный локальный сервис.

## Запуск

Запуск с настройками из `Caddyfile` в текущей директории:

```bash
# foreground:
caddy run

# background:
caddy start
```

- `caddy stop`: остановить фоновый процесс.
- `caddy reload`: перезапустить процесс с настройками из файла.

----
📂 [[Tooling]] | Последнее изменение: 23.09.2024 12:32