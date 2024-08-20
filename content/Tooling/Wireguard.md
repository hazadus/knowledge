**WireGuard** — это протокол, разработанный с целью обеспечения безопасной и эффективной передачи данных в интернете. Как заявляет разработчик, он чрезвычайно простой, но в то же время быстрый и инновационный. Изначально он был доступен только для ОС семейства Linux, но немногим позже стал кроссплатформенным. Ниже перечислим основные его преимущества:

- Бесплатный и легкий в использовании;
- Оптимизирован для обеспечения максимальной скорости обмена данными;
- Обеспечивает достойный уровень безопасности за счет использования новейших алгоритмов и механизмов аутентификации.

## Справочные материалы

- [WireGuard на своем сервере: подробная инструкция](https://timeweb.cloud/tutorials/network-security/wireguard-na-svoem-servere)
- [Видео Голобурдина](https://www.youtube.com/watch?v=5Aql0V-ta8A)

----
## Инструкция по настройке

Сейчас Wireguard уже блокируют некоторые операторы.

Работает Marzban. На Хабре есть статья о его настройке, гуглите. Если статья перестанет открываться без VPN, можно открыть её в startpage.com в анонимном режиме. Ссылку на статью не прилагаю, чтобы ничего не нарушать. Гуглится легко.

Обновляем сервер:

```bash
apt update && apt upgrade -y
```

Ставим wireguard:

```bash
apt install -y wireguard
```

Генерим ключи сервера:

```bash
wg genkey | tee /etc/wireguard/privatekey | wg pubkey | tee /etc/wireguard/publickey
```

Проставляем права на приватный ключ:

```bash
chmod 600 /etc/wireguard/privatekey
```

Проверим, как у вас называется сетевой интерфейс:

```bash
ip a
```

Скорее всего у вас сетевой интерфейс `eth0`, но возможно и другой, например, `ens3` или как-то иначе. Это название интерфейса используется далее в конфиге `/etc/wireguard/wg0.conf`, который мы сейчас создадим:

```bash
vim /etc/wireguard/wg0.conf
```

```
[Interface]

PrivateKey = <privatekey>
Address = 10.0.0.1/24
ListenPort = 51830
PostUp = iptables -A FORWARD -i %i -j ACCEPT; iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
PostDown = iptables -D FORWARD -i %i -j ACCEPT; iptables -t nat -D POSTROUTING -o eth0 -j MASQUERADE
```

Если не знаете текстовый редактор [[vim]] — откройте файл с `nano`, он проще в работе.

Обратите внимание — в строках PostUp и PostDown использован как раз сетевой интерфейс `eth0`. Если у вас другой — замените `eth0` на ваш.

Вставляем вместо `<privatekey>` содержимое файла `/etc/wireguard/privatekey`.

Настраиваем IP форвардинг:

```bash
echo "net.ipv4.ip_forward=1" >> /etc/sysctl.conf
sysctl -p
```

Включаем `systemd` демон с `wireguard`:

```bash
systemctl enable wg-quick@wg0.service
systemctl start wg-quick@wg0.service
systemctl status wg-quick@wg0.service
```

Создаём ключи клиента:

```bash
wg genkey | tee /etc/wireguard/goloburdin_privatekey | wg pubkey | tee /etc/wireguard/goloburdin_publickey
```

Добавляем в конфиг сервера клиента:

```bash
vim /etc/wireguard/wg0.conf
```

```
[Peer]

PublicKey = <goloburdin_publickey>
AllowedIPs = 10.0.0.2/32
```

Вместо `<goloburdin_publickey>`  — заменяем на содержимое файла `/etc/wireguard/goloburdin_publickey`.
`
Перезагружаем `systemd` сервис с `wireguard`:

```bash
systemctl restart wg-quick@wg0
systemctl status wg-quick@wg0
```

На локальной машине (например, на ноутбуке) создаём текстовый файл с конфигом клиента:

```bash
vim goloburdin_wb.conf
```


```
[Interface]

PrivateKey = <CLIENT-PRIVATE-KEY>
Address = 10.0.0.2/32
DNS = 8.8.8.8

[Peer]

PublicKey = <SERVER-PUBKEY>
Endpoint = <SERVER-IP>:51830
AllowedIPs = 0.0.0.0/0
PersistentKeepalive = 20
```

Здесь `<CLIENT-PRIVATE-KEY>` заменяем на приватный ключ клиента, то есть содержимое файла `/etc/wireguard/goloburdin_privatekey` на сервере.  `<SERVER-PUBKEY>` заменяем на публичный ключ сервера, то есть на содержимое файла `/etc/wireguard/publickey` на сервере. `<SERVER-IP>` заменяем на IP сервера. 

Этот файл открываем в Wireguard клиенте (есть для всех операционных систем, в том числе мобильных) — и жмем в клиенте кнопку подключения.



----
📂 [[Tooling]] | Последнее изменение: 20.08.2024 08:00