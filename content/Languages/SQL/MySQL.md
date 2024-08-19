## Поднимаем БД с phpMyAdmin через Docker
[https://migueldoctor.medium.com/run-mysql-phpmyadmin-locally-in-3-steps-using-docker-74eb735fa1fc](https://migueldoctor.medium.com/run-mysql-phpmyadmin-locally-in-3-steps-using-docker-74eb735fa1fc)
[https://docs.docker.com/compose/networking/#links](https://docs.docker.com/compose/networking/#links)

> [!info] mysql - Official Image | Docker Hub  
> MySQL is a widely used, open-source relational database management system (RDBMS).  
> [https://hub.docker.com/_/mysql](https://hub.docker.com/_/mysql)  

> [!info] Docker Hub  
>  
> [https://hub.docker.com/r/phpmyadmin/phpmyadmin/](https://hub.docker.com/r/phpmyadmin/phpmyadmin/)  
`arm64v8/mysql:oracle` – образ, который подходит на Mac M1.
Данные БД будут храниться в подпапке `./data/mysql` где лежит файл docker-compose.
```Docker
version: "3.9"
services:
  db:
    image: arm64v8/mysql:oracle
# image: mysql
    volumes:
      - ./data/mysql:/var/lib/mysql
    environment:
      - "MYSQL_ROOT_PASSWORD=mypass123"
    ports:
      - "3306:3306"
  admin:
    image: phpmyadmin/phpmyadmin
    ports:
      - "8081:80"
    links:
      - "db:db"
```
```Bash
# test:
docker exec -it mysql-db-1 bash
mysql --user=root --password=mypass123 --default-character-set=utf8mb4
# mysql> show databases;
```
phpMyAdmin будет на адресе [http://127.0.0.1:8081/index.php](http://127.0.0.1:8081/index.php)
```Bash
show databases;
use db_name;
show tables;
# turn on cyrillic:
\C utf8mb4
SET NAMES 'utf8mb4';
```

----
📂 [[SQL]] | Последнее изменение: 07.02.2024 14:50