## Отличия от других СУБД
[PostgreSQL vs. MySQL: A 360-degree Comparison [Syntax, Performance, Scalability and Features] (enterprisedb.com)](https://www.enterprisedb.com/blog/postgresql-vs-mysql-360-degree-comparison-syntax-performance-scalability-and-features)
[SQLite vs MySQL vs PostgreSQL: A Comparison Of Relational Database Management Systems | DigitalOcean](https://www.digitalocean.com/community/tutorials/sqlite-vs-mysql-vs-postgresql-a-comparison-of-relational-database-management-systems)
## Поднимаем Postgre и pgAdmin в Docker

> [!info] How to run PostgreSQL & PgAdmin in 3 steps using Docker  
> Note: This article is a PostgreSQL and PgAdmin adapted version of my post Run MySQL & phpMyAdmin locally in 3 steps using Docker Installing a relational database with a web based management tool is a very common requirement for a wide range of software projects.  
> [https://migueldoctor.medium.com/how-to-run-postgresql-pgadmin-in-3-steps-using-docker-d6fe06e47ca1](https://migueldoctor.medium.com/how-to-run-postgresql-pgadmin-in-3-steps-using-docker-d6fe06e47ca1)  

> [!info] postgres - Official Image | Docker Hub  
> The PostgreSQL object-relational database system provides reliability and data integrity.  
> [https://hub.docker.com/_/postgres?tab=description&page=1&ordering=last_updated](https://hub.docker.com/_/postgres?tab=description&page=1&ordering=last_updated)  

> [!info] Container Deployment - pgAdmin 4 6.16 documentation  
> pgAdmin can be deployed in a container using the image at: There are various tags that you can select from to get the version of pgAdmin that you want, using a command such as this if you're using Docker: docker pull dpage/pgadmin4: where is one of the following: The PostgreSQL utilities pg_dump, pg_dumpall, pg_restore and psql are included in the container to allow backups to be created and restored and other maintenance functions to be executed.  
> [https://www.pgadmin.org/docs/pgadmin4/latest/container_deployment.html](https://www.pgadmin.org/docs/pgadmin4/latest/container_deployment.html)  
```Docker
version: "3.9"
services:
  db:
    image: postgres:13
    volumes:
      - ./data/postgres:/var/lib/postgresql/data/
    environment:
      - "POSTGRES_PASSWORD=drbzdrbz"
    ports:
      - "5432:5432"
  admin:
    image: dpage/pgadmin4
    volumes:
      - ./data/pgadmin:/var/lib/pgadmin
    environment:
      - "PGADMIN_DEFAULT_EMAIL=hazadus@hazadus.ru"
      - "PGADMIN_DEFAULT_PASSWORD=drbzdrbz"
    ports:
      - "82:80"
# Простенькая альтернатива (работает MySQL тоже!)
	adminer:
	    image: adminer
	    ports:
	      - 8080:8080
```
pgAdmin: [http://localhost:82/](http://localhost:82/login?next=%2F)
```Bash
docker exec -it postgres-db-1 bash
# then:
psql -h localhost -U postgres
# SQL (to set password):
# ALTER USER postgres PASSWORD 'drbzdrbz';
# To get IP:
docker inspect postgres-db-1 -f "{{json .NetworkSettings.Networks }}"
# {"postgres_default":{"IPAMConfig":null,"Links":null,
# "Aliases":["postgres-db-1","db","80f726a177b9"],
# "NetworkID":"02e562d5816e2925367379caf00a3175702354a399bca4d03d8469afd61fc73c",
# "EndpointID":"733528ef94790dd2e8543ad48e71b5050b495d1603d1aa693327a87175db1699",
# "Gateway":"172.19.0.1",
# "IPAddress":"172.19.0.3",
# "IPPrefixLen":16,"IPv6Gateway":"","GlobalIPv6Address":"","GlobalIPv6PrefixLen":0,"MacAddress":"02:42:ac:13:00:03","DriverOpts":null}}
```

----
📂 [[SQL]] | Последнее изменение: 07.02.2024 14:50