Настраиваем на чистой VDS ([reference](https://timeweb.cloud/tutorials/servers/sentry-monitoring-i-otslezhivanie-oshibok)).

```bash
apt update && apt upgrade -y

apt install docker.io

# Ставим Docker и Docker Compose
VERSION=$(curl --silent https://api.github.com/repos/docker/compose/releases/latest | grep -Po '"tag_name": "\K.*\d')

DESTINATION=/usr/bin/docker-compose

sudo curl -L https://github.com/docker/compose/releases/download/${VERSION}/docker-compose-$(uname -s)-$(uname -m) -o $DESTINATION

sudo chmod 755 $DESTINATION

docker-compose --version

# Ставим Sentry
git clone https://github.com/getsentry/self-hosted.git
cd self-hosted
git checkout 23.8.0

./install.sh --skip-user-prompt --no-report-self-hosted-issues

# Запускаем на порту 9000
docker-compose up -d

# Создаем админа
docker-compose run --rm web createuser

```

----
📂 [[Tooling]] | Последнее изменение: 01.04.2024 17:39