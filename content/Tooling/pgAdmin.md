## References
- [pgAdmin: Container Deployment Docs](https://www.pgadmin.org/docs/pgadmin4/latest/container_deployment.html#container-deployment)
- [Run PostgreSQL and PGAdmin using docker compose](https://medium.com/@vishal.sharma./run-postgresql-and-pgadmin-using-docker-compose-34120618bcf9)

## Docker Compose Example

```
version: "3.8"  

services:  
	db:  
		image: postgres  
		container_name: local_pgdb  
		# restart: always  
		ports:  
			- "5432:5432"  
		environment:  
			POSTGRES_USER: user-name  
			POSTGRES_PASSWORD: strong-password  
		volumes:  
			- local_pgdata:/var/lib/postgresql/data  
	pgadmin:  
		image: dpage/pgadmin4  
		container_name: pgadmin4_container  
		# restart: always  
		ports:  
			- "8888:80"  
		environment:  
			PGADMIN_DEFAULT_EMAIL: user-name@domain-name.com  
			PGADMIN_DEFAULT_PASSWORD: strong-password  
		volumes:  
			- pgadmin-data:/var/lib/pgadmin  
  
volumes:  
	local_pgdata:  
	pgadmin-data:
```


----
📂 [[Tooling]] | Последнее изменение: 15.04.2024 12:53