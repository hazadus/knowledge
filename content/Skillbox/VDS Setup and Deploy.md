```bash
ssh-keygen -t rsa -b 2048 -C "Comment - VDS Name" -f ~/.ssh/filename
```

Сгенерируются два файла с ключами: `filename` (приватный ключ) и `filename.pub` (публичный ключ).

```
ssh -i filename root@123.45.67.8
```

```bash
adduser username
# Add `username` to `sudo` group
usermod -aG sudo username
# Switch to `username`
su - username
```

Добавим ключ `ssh` новому пользователю. Для этого, заходим под его именем по `ssh` на сервер, и далее:

```bash
cd ~
mkdir -p .ssh
# 700 - all rights for current user, none for others.
chmod 700 .ssh

echo "<PUBLIC_KEY>" >> ~/.ssh/authorized_keys
```

Можно отключить возможность входа по `ssh` по логину и паролю, оставив только вход по ключу. Для этого, на сервере нужно открыть файл конфигурации `ssh`:

```bash
sudo nano /etc/ssh/sshd_config
```

Стрелкой вниз домотайте до строки с `PasswordAuthentication` и вместо _yes_ напишите _no_:
![[Pasted image 20231122214129.png]]

После этого перечитайте конфигурацию сервера `sshd` (сервер ssh daemon):

```bash
sudo systemctl reload sshd.service
```

Теперь можно будет зайти только с использованием ключа:
![[Pasted image 20231122214236.png]]

Для входа на сервер с ключом, указываем флаг и полный путь к ключу:

```bash
ssh -i ~/.ssh/keyname user@123.45.67.8
```

Чтобы больше не указывать имя ключа при подключении, необходимо сделать следующее:

1. Создайте в папке `~/.ssh` файл с именем `config`:
```bash
touch ~/.ssh/config && chmod 600 ~/.ssh/config  
```
2. Скопируйте приватный и публичный ключи в папку ~/.ssh/:
```bash
chmod 600 ~/.ssh/timeweb*
cp -fv timeweb timeweb.pub ~/.ssh/
```
3. Отредактируйте файл `~/.ssh/config`, написав следующие строки:
```
Host <ip_address_of_your_machine>  
User <your_remote_system_user_name>  
IdentityFile ~/.ssh/timeweb
```
4. Подключитесь по `ssh` без указания имени ключа:
```
ssh <your_remote_system_user_name>@<ip_address_of_your_machine>
```


```bash
python3 -V
sudo apt install python3-virtualenv
mkdir ~/workspace
cd ~/workspace
python3 -m virtualenv -p python3 .venv
source .venv/bin/activate
# or `. .venv/bin/activate`
pip install flask
```

Всё, что запускается на `localhost` (`127.0.0.1`) доступно только изнутри машины. Поэтому приложение Flask нужно запускать с указанием IP адреса VDS (если не указывать порт, по умолчанию запустится на 80):

```bash
flask run -h 123.45.67.8
# or
gunicorn --bind 0.0.0.0:5000 app:app --daemon
```

https://www.howtogeek.com/225487/what-is-the-difference-between-127.0.0.1-and-0.0.0.0/

#### Шпаргалка по rsync

- Синхронизация каталогов dir1 и dir2 на одной машине:
    `rsync -a dir1 dir2`
- Синхронизация удалённой системы:
    `rsync -a local_dir username@remote_host:remote_dir`
- В обратную сторону:
    `rsync -a username@remote_host:remote_dir local_dir`
- Использование с ключом:
    `rsync -e 'ssh -i timeweb' -Paz username@remote_host:remote_dir local_dir`

**Опции:**

−r — рекурсивная синхронизация.  
−a — режим архива, эквивалент -rlptgoD.  
−z — сжатие данных.  
−P — показать прогресс синхронизации.  
−e — используется для задания параметров при подключении через SSH.

Полный список опций можно найти [в документации](https://linux.die.net/man/1/rsync).

![[Docker Setup]]