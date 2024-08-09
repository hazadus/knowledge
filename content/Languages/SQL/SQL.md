## Ссылки
[[INSERT statement]]
[[SQL Injection]]
[[Primary and Foreign Keys]]
[[JOIN, UNION]]

[Конспект в Notion по курсу SQL](https://www.notion.so/hazadus/SQL-cd49bd3d856c49caad2a7ac0b74e633e?pvs=4) (*перенести его сюда!*)
[[Моргунов Е.П. PostgreSQL. Основы языка SQL.pdf]]
## Структурные запросы MySQL
`SHOW DATABASES;` – показать список БД.
`USE database_name;` – выбрать БД для дальнейших запросов.
`CREATE DATABASE databaseName;` – создать БД.
`DROP DATABASE databaseName;` – удалить БД.
`SHOW TABLES;` – показать таблицы.
``DESCRIBE `tableName`;`` – посмотреть структуру таблицы.
## Команды SQL
### SELECT
**WHERE**
```SQL
SELECT * FROM `user` WHERE `reg_date` BETWEEN '2019-01-01' AND '2019-01-31';
SELECT COUNT(*) FROM `user` WHERE `reg_date` BETWEEN '2019-01-01' AND '2019-01-31';
SELECT * FROM `good` WHERE `count` < 20;
```
**LIKE**
```SQL
# Найдет конкретно "чай"
SELECT * from `good_category` WHERE `name` LIKE 'Tea';
# Маски  % - 0 или любое количество любых символов, _ - один любой символ
SELECT * from `good_category` WHERE `name` LIKE '%чай%';
```
**IS NULL**
```SQL
SELECT * FROM `good_category` WHERE `parent_id` IS NULL;
SELECT * FROM `good_category` WHERE `parent_id` IS NOT NULL;
```
“> 0” не идентично “IS NOT NULL” !!!
**IN**
```SQL
SELECT * FROM `order` WHERE `status_id` IN (7, 8);
```
**Сложный запрос с AND, OR, IN**
```SQL
SELECT * FROM `order_status_change`
WHERE (
(src_status_id = 4 AND dst_status_id = 8) 
OR 
(src_status_id = 1 AND dst_status_id IN(4,6))
) 
AND `time` BETWEEN '2018-01-01' AND '2018-12-31';
```
**ORDER BY**
```SQL
SELECT * FROM `good` ORDER BY `name` ASC;
SELECT * FROM `good` ORDER BY `name` ASC, `category_id` DESC;
```
**LIMIT**
```SQL
# 5 самых дорогих товаров
SELECT * FROM `good` ORDER BY `price` DESC LIMIT 5;
# Строки - 10 штук начиная с 20-й
SELECT * FROM `good` ORDER BY `id` LIMIT 20, 10;
```
**JOIN**
**Inner Join** - выводятся записи, данные из которых встречаются сразу в обеих таблицах.
```SQL
SELECT `good_category`.`name` AS `Name`, `good`.`name` AS `Category` 
FROM `good` 
JOIN `good_category` ON `good_category`.`id` = `good`.`category_id`
ORDER BY `good`.`price` DESC 
LIMIT 10;
# Аналогично с сокращенным именованием таблиц:
SELECT g.name goodName, c.name categoryName, g.price
FROM `good` g 
JOIN `good_category` c ON c.id = g.category_id
ORDER BY g.price DESC
LIMIT 10
```
**Left Join, Right Join** - выводятся соответственно все записи из первой (второй) таблицы, а из другой - только которые есть соответствующие. Вместо отсутствующих записей будет NULL.
```SQL
# Выберем все товары, которых нет ни в одном заказе:
SELECT g.id, g.name, o2g.order_id 
FROM `good` g
LEFT JOIN `order2good` o2g ON o2g.good_id = g.id
WHERE o2g.order_id IS NULL
```
После оператора **ON** можно писать условиях по аналогии с оператором **WHERE**, только через **AND**:
```SQL
# Много джоинов
SELECT c.name CategoryName,
	g.name ProductName,
    o.creation_date OrderDate,
    u.name UserName
FROM `good` g
JOIN `good_category` c ON c.id = g.category_id
JOIN `order2good` o2g ON o2g.good_id = g.id
JOIN `order` o ON o.id = o2g.order_id AND
	o.creation_date BETWEEN '2018-01-01' AND '2018-01-31'
JOIN `user` u ON u.id = o.user_id
# Вывести имя чувака, который брал пуэр с молоком
SELECT u.name 
FROM `good` g 
JOIN order2good o2g ON o2g.good_id = g.id
JOIN `order` o ON o2g.order_id = o.id
JOIN user u ON u.id = o.user_id
WHERE g.name LIKE 'пуэр с молоком'
```
**DISTINCT**
```SQL
SELECT DISTINCT `name` FROM `good`
# Уникальность по нескольким полям (уникальные комбинации)
SELECT DISTINCT src_status_id, dst_status_id
FROM `order_status_change`
```
**GROUP BY**
```SQL
# Cчитаем кол-во товаров в каждой категории
SELECT `category_id`, COUNT(*) FROM `good` GROUP BY `category_id`;
SELECT `category_id`, COUNT(*) AS Count
FROM `good` GROUP BY `category_id` ORDER BY Count DESC;
SELECT c.name, COUNT(*) AS Qty
FROM `good` g 
JOIN good_category c ON g.category_id = c.id
GROUP BY g.category_id
ORDER BY Qty DESC;
# Top-15 самых заказываемых товаров
SELECT g.name, COUNT(*) AS qty, c.name AS `Category`
FROM `order2good` o2g
JOIN good g ON g.id = o2g.good_id
JOIN good_category c ON g.category_id = c.id
GROUP BY  o2g.good_id
ORDER BY qty DESC
LIMIT 15
```

#### Вложенные запросы

Пример:

```SQL
SELECT full_name
FROM manager
WHERE city IN
	(SELECT DISTINCT city
	FROM manager
	WHERE city != 'Moscow');
```

### GROUP BY … HAVING
`HAVING` задает условия вывода после группировки, типа как `WHERE`.
```SQL
# Запрос выберет категории, в которых менее 50 товаров 
SELECT c.name, COUNT(*) `count` 
FROM `good` g 
JOIN good_category c ON c.id = g.category_id
GROUP BY g.category_id
HAVING `count` < 50
ORDER BY `count` ASC;
```
### UNION
Позволяет объединить результаты нескольких совершенно разных SELECT-запросов. Важно, чтобы каждый из них выдавал одинаковые поля, чтобы не было путаницы. Пишется между этими запросами. Точка с запятой может быть только в конце большого запроса, НЕ после промежуточных SELECT.
![[attachments/Untitled 18.png|Untitled 18.png]]
### INSERT
Полям `id` ставят свойство `AUTO_INCREMENT`, так что значение в него записывается при создании записи автоматически.
```SQL
INSERT INTO `good` (category_id, name, count, price)
VALUES (6, 'Адский чефир', 666, 123)
```
Если необходимо вставить несколько записей, их лучше всегда объединять в один запрос – даже очень большой, он выполнится быстрее, чем несколько запросов по отдельности.
```SQL
INSERT INTO `good` (category_id, name, count, price)
VALUES 
(6, 'Адский чефир', 666, 123),
...
(6, 'Адский чефир', 789, 456);
```
### UPDATE
```SQL
UPDATE `good` 
SET `name` = 'Конфета'
WHERE `id` = 1055;
```
Можно обновлять сразу несколько записей по какому-то условию:
```SQL
UPDATE `good` SET
price = price + 50
WHERE `count` BETWEEN 1 AND 9
# = WHERE `count` > 0 AND `count` < 10
```
### DELETE
```SQL
DELETE FROM `good`
WHERE `id` = 1373;
```
### IF (OR/AND)
```SQL
SELECT `id`, `name`,
	IF (
        `count` < 20,
        `price` * 0.8,
        `price` 
        ) `price`
FROM `sql_tea_shop`.`good`;
#	IF (
#        `count` < 20,  - условие
#        `price` * 0.8, - если условие выполнено
#        `price`        - если условие НЕ выполнено
#        ) `price`      - название результирующей колонки
SELECT `id`, `name`,
	IF (
        `count` < 20 OR `count` > 500,
        `price` * 0.8,
        `price` 
        ) `price`
FROM `sql_tea_shop`.`good`;
SELECT `id`, `name`,
	IF (
        (`count` < 20 OR `count` > 500)
        AND `price` > 600,
        `price` * 0.8,
        `price` 
        ) `price`
FROM `sql_tea_shop`.`good`;
```
### IF … IS NULL
```SQL
SELECT `id`, `name`,
	IF (
        `parent_id` IS NULL,
        'YES',
        'NO' 
        ) `is_root`
FROM `sql_tea_shop`.`good_category`;
```
### CASE … WHEN … END
```SQL
SELECT `id`, `name`,
	CASE
    	WHEN `count` < 20 THEN 'Мало'
        WHEN `count` > 500 THEN 'Много'
        ELSE 'Нормально'
	END `count` 
FROM `sql_tea_shop`.`good`;
```
## Функции для работы со строками

> [!info] MySQL :: MySQL 8.0 Reference Manual :: 12.8 String Functions and Operators  
> MySQL Backup and Recovery MySQL Globalization MySQL Information Schema MySQL Installation Guide Security in MySQL Starting and Stopping MySQL MySQL and Linux/Unix MySQL and Windows MySQL and macOS MySQL and Solaris Building MySQL from Source MySQL Restrictions and Limitations MySQL Partitioning MySQL Tutorial MySQL Performance Schema MySQL Replication Using the MySQL Yum Repository MySQL NDB Cluster 8.  
> [https://dev.mysql.com/doc/refman/8.0/en/string-functions.html](https://dev.mysql.com/doc/refman/8.0/en/string-functions.html)  
### CHAR_LENGTH()
```SQL
SELECT `id`, `name`,
CHAR_LENGTH(`name`) `length`
FROM `sql_tea_shop`.`good`
ORDER BY `length` DESC;
```
### SUBSTR()
Нумерация символов в строке в SQL начинается с ЕДИНИЦЫ, а не с нуля, как обычно во всех языках программирования.
```SQL
SELECT `id`, 
SUBSTR(`name`, 1, 20) `name`
FROM `sql_tea_shop`.`good`;
```
### CONCAT()

В качестве параметра может передаваться сколько угодно строк для объединения.

```SQL
SELECT `id`, 
IF (
    CHAR_LENGTH(`name`) > 20,
    CONCAT(
        SUBSTR(`name`, 1, 20),
        '...'
        ),
    `name`
) `name` 
FROM `sql_tea_shop`.`good`;
```
### GROUP_CONCAT()

Соединяет результаты выборки в одну строку.

```SQL
SELECT
	o.id,
    GROUP_CONCAT(g.name SEPARATOR ', ') products
FROM `sql_tea_shop`.`order` o 
JOIN `sql_tea_shop`.`order2good` o2g ON 
	o2g.order_id = o.id 
JOIN `sql_tea_shop`.`good` g ON 
	g.id = o2g.good_id 
GROUP BY o.id;
```
### TRIM()

Удаляет пробелы в начале и конце строки.

```SQL
SELECT
	o.id,
    GROUP_CONCAT(TRIM(g.name) SEPARATOR ', ') products
FROM `sql_tea_shop`.`order` o 
JOIN `sql_tea_shop`.`order2good` o2g ON 
	o2g.order_id = o.id 
JOIN `sql_tea_shop`.`good` g ON 
	g.id = o2g.good_id 
GROUP BY o.id;
```
### REPLACE()
Usage: `REPLACE(field, from, to)`
## Функции работы с датами

> [!info] MySQL :: MySQL 8.0 Reference Manual :: 12.7 Date and Time Functions  
> MySQL Backup and Recovery MySQL Globalization MySQL Information Schema MySQL Installation Guide Security in MySQL Starting and Stopping MySQL MySQL and Linux/Unix MySQL and Windows MySQL and macOS MySQL and Solaris Building MySQL from Source MySQL Restrictions and Limitations MySQL Partitioning MySQL Tutorial MySQL Performance Schema MySQL Replication Using the MySQL Yum Repository MySQL NDB Cluster 8.  
> [https://dev.mysql.com/doc/refman/8.0/en/date-and-time-functions.html](https://dev.mysql.com/doc/refman/8.0/en/date-and-time-functions.html)  
### DATEDIFF(), CURRENT_DATE(), DATE()
```SQL
# количество дней с даты регистрации
SELECT `id`, `name`,
	DATEDIFF(CURRENT_DATE(), DATE(reg_date)) `days_regged`,
    `reg_date`
FROM `sql_tea_shop`.`user`
ORDER BY `days_regged` ASC;
```
### DATE_FORMAT()
```SQL
SELECT `id`, `name`,
	DATEDIFF(CURRENT_DATE(), DATE(reg_date)) `days_regged`,
    DATE_FORMAT(`reg_date`, '%d.%m.%Y') `date_formatted`
FROM `sql_tea_shop`.`user`
ORDER BY `days_regged` ASC;
```
![[attachments/Untitled 1 7.png|Untitled 1 7.png]]
Динамика заказов по месяцам:
```SQL
SELECT
	DATE_FORMAT(creation_date, '%m') `month`,
    COUNT(*) `count` 
FROM `sql_tea_shop`.`order` 
GROUP BY `month` 
ORDER BY `month`;
```
## Агрегатные функции

> [!info] MySQL :: MySQL 8.0 Reference Manual :: 12.20.1 Aggregate Function Descriptions  
> The , , and aggregate functions perform bit operations.  
> [https://dev.mysql.com/doc/refman/8.0/en/aggregate-functions.html](https://dev.mysql.com/doc/refman/8.0/en/aggregate-functions.html)  
### COUNT()
Посчитать количество строк с уникальным значением поля `name`:
```SQL
SELECT COUNT(DISTINCT `name`) FROM `good`
```
### SUM()
Посчитать суммарное количество запасов товаров:
```SQL
SELECT SUM(`count`) FROM `good`
```
Посчитать общую стоимость товаров:
```SQL
SELECT SUM(`price` * `count`) FROM `sql_tea_shop`.`good`;
```

## Функции для работы с числами
## `ROUND()`

Округление до целого значения.

## Индексы и пр.
### Типы индексов в MySQL
- BTREE – для поиска по диапазонам значений.
- HASH – для поиска по совпадениям.
### Установка индексов
При создании таблицы:
```SQL
CREATE TABLE `good_type` (
	`id` INT NOT NULL AUTO_INCREMENT,
	`name` VARCHAR(255),
	PRIMARY KEY(`id`)
);
```
При изменении таблицы:
```SQL
ALTER TABLE `good`
	ADD PRIMARY KEY (`id`);
```
`PRIMARY KEY` – установить _первичный ключ._
Если необходимо установить _просто индекс:_
```SQL
ALTER TABLE `good`
	ADD KEY (`category_id`);
```
Если необходимо установить уникальный индекс:
```SQL
ALTER TABLE `good`
	ADD UNIQUE (`code`);
```
Индексы могут устанавливаться по нескольким полям. Это бывает необходимо, если часто производится поиск по значениям двух полей:
```SQL
ALTER TABLE `order_status_change`
	ADD KEY (
		`src_status_id`, `dst_status_id`
);
```
Индексы можно устанавливать не только по числовым полям и полям с датами, но и по текстовым полям. В этом случае в скобках необходимо указать длину части текста, по которой будет строиться индекс:
```SQL
ALTER TABLE `good`
	ADD KEY (`name` (30));
```
Отличия первичного ключа от уникального ключа:
![[attachments/Untitled 2 6.png|Untitled 2 6.png]]
### Виды связей
- один ко многим
- один к одному (не часто используется, пример – расширение одной таблицы при помощи другой, например таблицы пользователей таблицей с инфо о профиле в Django)
- многие ко многим
**Нарушение целостности данных** в БД – наличие ссылок на отсутствующие записи в других таблицах.
**Решение:** установка связей с ограничениями.
**Установка связи “один ко многим”:**
![[attachments/Untitled 3 5.png|Untitled 3 5.png]]
**Установка связи “один к одному”:**
![[attachments/Untitled 4 4.png|Untitled 4 4.png]]
**Установка связи “многие ко многим”** делается через таблицу, в которой есть id из двух связываемых таблиц:
![[attachments/Untitled 5 4.png|Untitled 5 4.png]]
![[attachments/Untitled 6 4.png|Untitled 6 4.png]]
Ключи (ограничения) можно именовать:
![[attachments/Untitled 7 3.png|Untitled 7 3.png]]
По именам в дальнейшем можно обращаться к ключам, например, чтобы удалить:
![[attachments/Untitled 8 2.png|Untitled 8 2.png]]
Для обеспечения целостности данных можно указывать действия, которые нужно произвести с записью при удалении или изменении связанной записи:
![[attachments/Untitled 9 2.png|Untitled 9 2.png]]
Это означает: при удалении записи из таблицы **good_category** в таблице **good** в соответствующих записях в поле **category_id** будет проставлено значение **NULL**.
При изменении поля **id** в таблице **good_category** произойдет ошибка в случае, если в таблице **good** есть хотя бы одна запись, которая ссылается на этот **id** в таблице **good_category**.
**Возможные действия при нарушении целостности данных в БД:**
![[attachments/Untitled 10 2.png|Untitled 10 2.png]]
![[attachments/Untitled 11 2.png|Untitled 11 2.png]]
![[attachments/Untitled 12 2.png|Untitled 12 2.png]]
`TRUNCATE tableName;` – очистить таблицу, но не удалять её. При этом сбрасывается индекс автоинкремента.
`DROP tableName;` – удалить таблицу.
## Представления (view)
Это “временные” таблицы, создаваемые динамически на основе какого-то запроса.
![[attachments/Untitled 13 2.png|Untitled 13 2.png]]
К представлению можно обращаться с помощью обычных SQL-запросов.