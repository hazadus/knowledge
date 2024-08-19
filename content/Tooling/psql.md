📂 [[Tooling]]

----
## Basic Commands
- `psql -d DB -U ROLE -h HOST -p PORT`: run psql and Connect.
- `\h` : List server SQL commands.
- `\h ALTER TABLE` : Get syntax for specified SQL command.
- `\?` : List psql commands.
- `\q` : Quit psql.
- `\conninfo` : Check connection.
- `\c` , `\connect` : Connect from inside psql.
- `\! pwd` : Execute shell commands.
- `\o dev1_psql.log` : Output results of subsequent query to the specified file.
    - `\o` : Switch output back to console.
- `\i dev1_psql.log` : Run SQL commands from the file.
    - `psql < filename` , `psql -f filename` : Another way to run SQL from file.
- `\dn` (describe namespace): show list of schemas
    - `\dnS` : also show system schemas
- `\dt public.*` : show all tables in `public` schema.
- `\dT`: show all types.
- `\db` : list of tablespaces.
- `\timing on`, `\timing off` : turn on/off timing.
## Formatting Options
- `\a` : Toggle alignment.
- `\t` : Toggle header and summary.
- `\pset` : psql formatting options.
    - `\pset fieldsep ''` : use `''` instead of `|` as field separator.
```JavaScript
# Format results as single "record" - add \gx instead of ; at the end of query:
SELECT name, setting, unit, category, context, vartype, min_val, max_val, boot_val, reset_val 
FROM pg_settings 
WHERE name = 'work_mem' \gx
```
![[attachments/Untitled 12.png|Untitled 12.png]]
## Variables
- `\set TEST Hello` : Set value of psql variable `TEST` equal to `Hello!`.
- `\echo :TEST` : Print variable value.
- `\unset TEST` : Unset variable value.
- `:top5` : Run SQL statement from variable.
- `\gset` : Save query results in variable, e.g. `SELECT current_setting('work_mem') AS current_work_mem \gset` - result will be stored in `current_work_mem` .
- `\set` : List all variables.
- `\? variables` : Info about built-in variables.

----
📂 [[Tooling]] | Последнее изменение: 14.04.2024 14:28