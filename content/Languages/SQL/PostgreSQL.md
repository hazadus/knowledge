## Отличия от других СУБД
[PostgreSQL vs. MySQL: A 360-degree Comparison [Syntax, Performance, Scalability and Features] (enterprisedb.com)](https://www.enterprisedb.com/blog/postgresql-vs-mysql-360-degree-comparison-syntax-performance-scalability-and-features)
[SQLite vs MySQL vs PostgreSQL: A Comparison Of Relational Database Management Systems | DigitalOcean](https://www.digitalocean.com/community/tutorials/sqlite-vs-mysql-vs-postgresql-a-comparison-of-relational-database-management-systems)

## List all constraints of a table in PostgreSQL

```sql
SELECT con.*
    FROM pg_catalog.pg_constraint con
        INNER JOIN pg_catalog.pg_class rel ON rel.oid = con.conrelid
        INNER JOIN pg_catalog.pg_namespace nsp ON nsp.oid = connamespace
        WHERE nsp.nspname = '{schema name}'
             AND rel.relname = '{table name}';
```

![[Pasted image 20240915133700.png]]



----
📂 [[SQL]] | Последнее изменение: 15.09.2024 13:37