📂 [[Tooling]]

----
## Shell Commands

> [!info] Docker run reference  
> Docker runs processes in isolated containers.  
> [https://docs.docker.com/engine/reference/run/](https://docs.docker.com/engine/reference/run/)  
```Bash
# List volumes
sudo docker volume ls
# Inspect volume (show where it is, too)
sudo docker volume inspect django-c3-pages-docker_postgres_data
# List containers
# https://docs.docker.com/engine/reference/commandline/ps/
sudo docker ps
```
### Backup / restore Volumes

```Bash
# Creates 'backup.tar' with postgresql data in current directory
#
# Container id of Postgres (f0de8da471d2) got from 'sudo docker ps' when containers are up
# '/var/lib/postgresql/data/' is from 'docker-compose.yml', lines:
# volumes:
#      - postgres_data:/var/lib/postgresql/data/
cd /Users/hazadus/backup
sudo docker run --rm --volumes-from 5e1ffd7ed38b -v $(pwd):/backup ubuntu tar cvf /backup/backup.tar /var/lib/postgresql/data/
```
```Bash
# Restoring postgresql data from backup tar
#
#
# ls -al
sudo docker run --rm -v django-c8-newspaper_postgres_data:/var/lib/postgresql/data/ -v $PWD:/backup-dir bash -c "cd /var/lib/postgresql/data/ && ls -al"
#
# untar - RUN FROM DIR WITH 'backup.tar' in it!!!
#
cd /Users/hazadus/backup
sudo docker run --rm -v django-c8-newspaper_postgres_data:/var/lib/postgresql/data/ -v $PWD:/backup-dir bash -c "tar xvf /backup-dir/backup.tar"
```
### Disk Cleanup
```Bash
docker system df
docker builder prune
docker system prune
```
```Bash
# "Advanced" cleanup
# https://habr.com/ru/post/486200/
docker system prune -f -a --volumes
```
### Docker Compose – run from file
```Bash
up_dev:
	docker compose -f docker-compose.dev.yml up --build
up_prod:
	docker compose -f docker-compose.prod.yml up -d --build
down:
	docker compose -f docker-compose.prod.yml down
```
### Docker `init`
Use CLI tool to create necessary Docker files in the project directory: `docker init`.

## Build Container and Push To Hub

```bash
# hub username=hazadus, tag=v1, ARG username=what_user
docker build --build-arg username=what_user -t hazadus/apusher-backend:v1 .

# list images
docker images

# push to Docker Hub
docker push hazadus/apusher-backend:v1
```

----
📂 [[Tooling]]