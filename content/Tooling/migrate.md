Repo: https://github.com/golang-migrate/migrate

🔖 #go #DB #DevTools 

## Create Migration

```bash
migrate create -seq -ext=.sql -dir ./migrations create_prices_table
```

Эта команда создаст два SQL-файла под up и down миграции в указанной директории.
## Apply Migrations

```bash
migrate -path=./migrations -database="postgres://postgres:postgres@localhost:5432/postgres?sslmode=disable" up

migrate -path=./migrations -database="postgres://postgres:postgres@localhost:5432/postgres?sslmode=disable" down
```

----
📂 [[Tooling]] | Последнее изменение: 14.11.2024 17:40