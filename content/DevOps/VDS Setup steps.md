1) save all new passwords to 1Password!
2) add new linux user
Reference: [https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu-20-04](https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu-20-04)
```Bash
adduser hazadus
# Add new user to sudo group
# When running 'sudo' use THIS USER's password, not root's!
usermod -aG sudo hazadus
```
3) setup `ufw`
```Bash
ufw app list
ufw allow OpenSSH
ufw enable
ufw status
```

> [!info] UFW Essentials: Common Firewall Rules and Commands | DigitalOcean  
> UFW ( uncomplicated fire wall) is a firewall configuration tool that runs on top of iptables, included by default within Ubuntu distributions.  
> [https://www.digitalocean.com/community/tutorials/ufw-essentials-common-firewall-rules-and-commands](https://www.digitalocean.com/community/tutorials/ufw-essentials-common-firewall-rules-and-commands)  
4) настройка подключения `ssh` с ssh-ключами

> [!info] Основы Docker. Большой практический выпуск  
> Или: @amatyashov_bot Телеграм канал https://t.  
> [https://www.youtube.com/watch?v=QF4ZF857m44&t=1706s](https://www.youtube.com/watch?v=QF4ZF857m44&t=1706s)  
[[SSH]]

> [!info] How To Install and Use Docker on Ubuntu 22.04 | DigitalOcean  
> Docker is an application that simplifies the process of managing application processes in containers.  
> [https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-22-04](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-22-04)  
```Bash
# 1
sudo apt update

# 2
sudo apt install apt-transport-https ca-certificates curl software-properties-common

# 3
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

# 4
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

$ 5..8
sudo apt update
apt-cache policy docker-ce
sudo apt install docker-ce
sudo systemctl status docker
```

> [!info] How To Install and Use Docker Compose on Ubuntu 22.04 | DigitalOcean  
> Docker simplifies the process of managing application processes in containers.  
> [https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-compose-on-ubuntu-22-04](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-compose-on-ubuntu-22-04)  
5) install `nginx`
```Bash
sudo apt install nginx
sudo ufw allow 'Nginx Full'
sudo ufw allow 'Nginx HTTP'
sudo ufw allow 'Nginx HTTPS'
```
6) copy files to remote if needed
```Bash
scp ./db.sqlite3 hazadus@85.193.89.177:~/projects/django-website/
```

----
📂 [[DevOps]]