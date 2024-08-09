## Обзор и конструкции языка PL/pgSQL

> [!info] DEV1-12. 11. Обзор и конструкции языка PL/pgSQL  
> DEV1-12.  
> [https://www.youtube.com/watch?v=CSvxdO8XgAk](https://www.youtube.com/watch?v=CSvxdO8XgAk)  

> [https://edu.postgrespro.ru/dev1-12/dev1_11_plpgsql_introduction.html](https://edu.postgrespro.ru/dev1-12/dev1_11_plpgsql_introduction.html)  

Язык появился в версии 6.4 в 1998 году.

Цели создания:
- простой язык для написания пользовательских функций и триггеров;
- добавить управляющие структуры к языку SQL;
- сохранить возможность использования любых пользовательских типов, функций и операторов.
### Базовые особенности языка

Доступен по умолчанию, интегрирован с SQL, прост в использовании.

![[Untitled 11.png]]

Объявление переменных происходит в блоке `DECLARE`:

```plpgsql
foo text;
bar text := 'hello';
-- Модификаторы имеют очевидное действие:
baz integer NOT NULL := 0;
spam CONSTANT text := "answer is 42";
```

Вывод сообщения:

```plpgsql
-- Вместо % подставятся значения переменных
RAISE NOTICE '%, %!', foo, bar;
```

### Проверки при создании и выполнении подпрограмм

PL/pgSQL может выдавать предупреждения в некоторых подозрительных случаях. Для этого надо установить параметр (значение по умолчанию – none):

```
SET plpgsql.extra_warnings = 'all';
```

Так будут выводить предупреждения и советы при создании и вызове подпрограмм, где есть потенциально проблемные моменты в коде.

### Объявление функций

Функции и процедуры объявляются идентично для всех языков, но нужно указать соответствующий язык – `LANGUAGE plpgsql`. В конце объявления необходимо указать "категорию изменчивости" – `IMMUTABLE` в примере ниже.

Пример функции, возводящей параметр в квадрат и возвращающей значение:

```plpgsql
CREATE FUNCTION sqr_in(IN a NUMERIC) RETURNS numeric
AS $$
BEGIN
	RETURN a * a;
END;
$$ LANGUAGE plpgsql IMMUTABLE;
```

Та же функция, но с OUT-параметром. Возвращаемое значение присваивается этому параметру:

```plpgsql
CREATE FUNCTION sqr_out(IN a NUMERIC, OUT retval numeric)
AS $$
BEGIN
	retval := a * a;
END;
$$ LANGUAGE plpgsql IMMUTABLE;
```

Та же функция, но с INOUT-параметром. Такой параметр используется и для принятия входного значения, и для возврата значения функции:

```plpgsql
CREATE FUNCTION sqr_inout(INOUT a NUMERIC)
AS $$
BEGIN
	a := a * a;
END;
$$ LANGUAGE plpgsql IMMUTABLE;
```

#### Получение кода функции из БД по её названию

Сам написал:

```
DO $$
DECLARE
	-- Имя функции, которую мы хотим получить:
	proc_name TEXT := 'fmt';
	proc_oid INT;
	proc_code TEXT;
BEGIN
	SELECT oid INTO proc_oid FROM pg_proc WHERE proname = proc_name;
	RAISE NOTICE '% oid=%', proc_name, proc_oid;

	-- Получаем код функции и выводим его:
	SELECT pg_get_functiondef(proc_oid) INTO proc_code FROM pg_proc WHERE oid = proc_oid;
	RAISE NOTICE '%', proc_code;
END;
$$;
```

### Условные операторы

#### `IF...THEN...ELSE...`

Общий вид конструкции с оператором `IF`:

```
IF условие THEN
	-- операторы
ELSIF условие THEN
	-- операторы
ELSE
	-- операторы
END IF;
```

Пример функции, использующей условный оператор для форматирования номера телефона. Функция возвращает два значения - код и номер отдельно:

```
CREATE FUNCTION fmt(IN phone text, OUT code text, OUT num text)
AS $$
BEGIN
	IF PHONE ~ '^[0-9]*$' AND length(phone) = 10 THEN
		code := substr(phone, 1, 3);
		num  := substr(phone, 4);
	ELSE
		code := NULL;
		num  := NULL;
	END IF;
END;
$$ LANGUAGE plpgsql IMMUTABLE;
```

#### `CASE...WHEN...ELSE`

Общий вид оператора `CASE` (первый вариант – по условию):

```
CASE
	WHEN условие THEN
		-- операторы
	ELSE
		-- операторы
END CASE;
```

- Секция `WHEN` может повторяться несколько раз.
- Секция `ELSE` может отсутствовать.
- Выполняется блок, соответствующий первому истинному условию.
- Если ни одно из условий не истинно, выполнится блок `ELSE` (его отсутствие в таком случае вызовет ошибку).

```
DO $$
DECLARE
	code text := (fmt('8123556656')).code;
BEGIN
	CASE
		WHEN code IN ('495', '499') THEN
			RAISE NOTICE '% - Moscow', code;
		WHEN code = '812' THEN
			RAISE NOTICE '% - Saint-Petersburg', code;
		ELSE
			RAISE NOTICE '% - Misc', code;
	END CASE;
END;
$$;
```

Общий вид оператора `CASE` (второй вариант – по выражению):

```
CASE выражение
	WHEN значение, ... THEN
		-- операторы
	ELSE
		-- операторы
END CASE
```

- Секция `WHEN` может повторяться несколько раз.
- Секция `ELSE` может отсутствовать.
- Выполняется блок, соответствующий первому истинному условию "выражение = значение".
- Если ни одно из условий не истинно, выполнится блок `ELSE` (его отсутствие в таком случае вызовет ошибку).

```
DO $$
DECLARE
	code text := (fmt('8123556656')).code;
BEGIN
	CASE code
		WHEN '495', '499' THEN
			RAISE NOTICE '% - Moscow', code;
		WHEN '812' THEN
			RAISE NOTICE '% - Saint-Petersburg', code;
		ELSE
			RAISE NOTICE '% - Misc', code;
	END CASE;
END;
$$;
```

### Циклы

Все циклы используют общую конструкцию:

```
LOOP
	-- операторы
END LOOP;
```

#### `FOR`

Инкремент по умолчанию равен 1, low и high включаются в итерации цикла (то есть 0 .. 10 выполнится 11 раз):

```
FOR name IN low .. high BY increment
LOOP
	-- operators;
END LOOP;

-- итерации в обратном порядке:
FOR name IN REVERSE high .. low BY increment
LOOP
	-- operators;
END LOOP;
```

```
DO $$
BEGIN
	FOR i IN 0 .. 10
	LOOP
		RAISE NOTICE '%', i;
	END LOOP;
END;
$$;
```

Пример функции, которая переворачивает строку:

```
CREATE FUNCTION reverse_for (line TEXT) returns TEXT
AS $$
DECLARE
	line_len CONSTANT int := length(line);
	retval text := '';
BEGIN
	FOR i IN 1 .. line_len
	LOOP
		-- || - это конкатенация строк:
		retval := substr(line, i, 1) || retval;
	END LOOP;
	RETURN retval;
END;
$$ LANGUAGE plpgsql IMMUTABLE STRICT;
```
`STRICT` означает, что если хоть один входной параметр функции не определен, немедленно вернется `NULL` без выполнения тела функции.

#### `LOOP`

Цикл `LOOP` без заголовка выполняется бесконечно. Для выхода используется оператор `EXIT`: `EXIT label WHEN condition;`.
Метка не обязательна. `WHEN` тоже – при его отсутствии цикл прервется безусловно.

Вариант функции переворота строки с использованием `LOOP`:

```
CREATE FUNCTION reverse_loop (line TEXT) RETURNS text
AS $$
DECLARE
	line_len CONSTANT INT := length(line);
	i INT := 1;
	retval TEXT := '';
BEGIN
	<<main_loop>>
	LOOP
		EXIT main_loop WHEN i > line_len;
		retval := substr(line, i, 1) || retval;
		i := i + 1;
	END LOOP;
	RETURN retval;
END;
$$ LANGUAGE plpgsql IMMUTABLE STRICT;
```

Оператор `CONTINUE` начинает новую итерацию цикла, может быть с условием и без условия:

```
DO $$
DECLARE
	s INTEGER := 0;
BEGIN
	FOR i IN 1 .. 100
	LOOP
		s := s + i;
		CONTINUE WHEN mod(i, 10) != 0;
		-- Печатаем только для каждого 10 i:
		RAISE NOTICE 'i = %, s = %', i, s;
	END LOOP;
END;
$$;
```

## Вычисление выражений

Сам интерпретатор `pl/pgSQL` не умеет вычислять выражения, они вычисляются в контексте SQL. То есть, встречая некоторое выражение, делается `SELECT`+`выражение` и берется результат.

Особенности:
- можно использовать все возможности SQL, включая подзапросы;
- невысокая скорость выполнения, хотя разобранный запрос кэшируется;
- некоторые неоднозначности в разрешении имён.

Пример использования подзапроса:

```
DO $$
BEGIN
	RAISE NOTICE '%', (
		SELECT name
		FROM users
		WHERE id = 1
	);
END;
$$;
```

## Управление транзакциями в процедурах
 
После выполнения следующего кода в таблице `test` будет только значение `1`:

```
CREATE TABLE test(n INTEGER);

CREATE PROCEDURE foo()
AS $$
BEGIN
	INSERT INTO test VALUES(1);
	COMMIT;
	INSERT INTO test VALUES(2);
	ROLLBACK;
END;
$$ LANGUAGE plpgsql;

CALL foo();
```

Есть определенные ограничения:
- Процедура должна сама начинать новую транзакцию, а не выполняться в контексте уже начатой ранее.
- В стеке вызова процедуры не должно быть ничего, кроме оператора `CALL`.

## Выборка из таблиц в переменные

`SELECT ... INTO ...` может выбрать строку (или несколько, тогда будет исползована первая строка) из таблицы, и "разложить" значения по переменным:

```
DO $$
DECLARE
	r RECORD;
BEGIN
	SELECT id, name, address->>'country' INTO r FROM users WHERE id = 1;
	RAISE NOTICE '%', r;
END;
$$;
```

### Другие команды с выборкой в переменные

Команды `INSERT`, `UPDATE`, `DELETE` могут возвращать результат с помощью фразы `RETURNING`. Их можно использовать также, как в примере выше, добавив фразу `INTO`:

```
DO $$
DECLARE
	r RECORD;
BEGIN
	UPDATE table SET code = code || '!' WHERE id = 1 RETURNING * INTO r;
	RAISE NOTICE 'Updated row: %', r;
END;
DD;
```

### Проверка результата запроса

- `INTO STRICT` – гарантия получения ровно одной строки.
- Диагностика `ROW_COUNT` – число строк, возвращенных (обработанных) последней командой SQL. Чтобы её получить надо выполнить строчку в процедуре `GET DIAGNOSTICS rowcount = row_count;`.
- Переменная `FOUND` после команды SQL: истина, если команда вернула (обработала) строку; после цикла – признак того, что выполнилась хотя бы одна итерация. Её можно просто использовать в коде: `RAISE NOTICE 'found = %', FOUND;`.

## Табличные функции

Особенности:
- строки добавляются к результату, но выполнение функции не прекращается.
- команды можно выполнять несколько раз.
- результат не возвращается, пока функция не завершится.

Пример табличной функции:

```
-- LIKE t значит что вернет как поля в таблице t, чтобы заново не писать
CREATE FUNCTION t() RETURNS TABLE(LIKE t)
AS $$
BEGIN
	RETURN QUERY SELECT id, code FROM t ORDER BY id;
END;
$$ STABLE LANGUAGE plpgsql;
```

Другой вариант – возвращать значения построчно:

```
-- Функция вернет список дней недели от понедельника до вс, на языке локали
-- Локаль устанавливается: SET lc_time = 'en_US.UTF8'
CREATE FUNCTION days_of_week() RETURNS SETOF TEXT
AS $$
BEGIN
	FOR i IN 7 .. 13 LOOP
		RETURN NEXT to_char(to_date(i::text, 'J'), 'TMDy');
	END LOOP;
END;
-- STABLE потому что зависит от настроек локали
$$ STABLE LANGUAGE plpgsql;
```

----
## Курсоры

🔗 [Модуль 13: Курсоры](https://www.youtube.com/watch?v=7_wJ1Yn1TI4)

Операции с курсором:
 - выборка по одной строке
 - обращение к текущей строке курсора
 - обычно обработка выполняется в цикле
 - закрытие

### Объявление и открытие

Курсор может открывать для любой команды, возвращающей строки.

```
-- вариант 1
DO $$
DECLARE
	cur refcursor;
BEGIN
	-- связывание с запросом и открытие курсора
	OPEN cur FOR SELECT * FROM users;
END;
$$;
```

```
-- вариант 2
DO $$
DECLARE
	-- объявление и связывание переменной с запросом
	cur CURSOR(id INTEGER) FOR SELECT * FROM users WHERE users.id = cur.id;
BEGIN
	-- открытие курсора с указанием фактических параметров
	OPEN cur(1);
END;
$$;
```

### Операции с курсором

Чтение текущей строки из курсора выполняется командой `FETCH`. Если нужно только переместиться на следующую строку, можно использовать команду `MOVE`.

Примеры:

```
DO $$
DECLARE
	cur REFCURSOR;
	rec RECORD;
BEGIN
	OPEN cur FOR SELECT * FROM users ORDER BY id DESC;
	MOVE cur; -- пропускаем одну строку
	FETCH cur INTO rec;
	RAISE NOTICE 'rec = %', rec;
	CLOSE cur;
END;
$$;
```

```
DO $$
DECLARE
	cur REFCURSOR;
	rec RECORD;
BEGIN
	OPEN cur FOR SELECT id, name, coffee_id FROM users ORDER BY id DESC;
	LOOP
		FETCH cur INTO rec;
		EXIT WHEN NOT FOUND; -- FOUND - выбрана ли очередная строка?
		RAISE NOTICE 'rec = %', rec;
	END LOOP;
	CLOSE cur;
END;
$$;
```

```
DO $$
DECLARE
	cur CURSOR FOR SELECT id, name, coffee_id FROM users ORDER BY id DESC;
BEGIN
	FOR rec IN cur LOOP -- cur должна быть связана с запросом!
		RAISE NOTICE 'rec = %', rec;
	END LOOP;
END;
$$;
```

Код выше можно даже ещё сократить:

```
DO $$
DECLARE
	rec RECORD; -- надо объявить явно в данном случае
BEGIN
	FOR rec IN (SELECT id, name, coffee_id FROM users ORDER BY id DESC) LOOP
		RAISE NOTICE 'rec = %', rec;
	END LOOP;
END;
$$;
```

### Передача курсора клиенту

```
DO $$
DECLARE
	cur REFCURSOR;
BEGIN
	OPEN cur FOR SELECT * FROM users ORDER BY id DESC;
	RAISE NOTICE 'cur = %', cur; -- имя сервер выдает автоматически
END;
$$;
```

Таким образом, можно написать функцию, которая вернет курсор клиенту:

```
CREATE FUNCTION users_cur() RETURNS refcursor
AS $$
DECLARE
	cur REFCURSOR;
BEGIN
	OPEN cur FOR SELECT * FROM users ORDER BY id DESC;
	RETURN cur;
END;
$$ VOLATILE LANGUAGE plpgsql;
```

----
## Динамические запросы

🔗  https://www.youtube.com/watch?v=hXqvNW2pdcs

Текст SQL-команды формируется в момент выполнения.

Причины использования:
- дополнительная гибкость в приложении;
- формирование нескольких конкретных запросов вместо одного универсального для оптимизации.

Недостатки:
- операторы не подготавливаются БД;
- возрастает риск внедрения (инъекции) SQL-кода;
- возрастает сложность сопровождения.

Для выполнения запроса используется оператор `EXECUTE`.

```
DO $$
DECLARE
	cmd CONSTANT TEXT := 'CREATE TABLE IF NOT EXISTS city_msk(
		name TEXT,
		architect TEXT,
		built INTEGER
	)';
BEGIN
	EXECUTE cmd;
END;
$$;
```

Предложение `INTO` оператора `EXECUTE` позволяет вернуть одну (первую) строку результата в переменную составного типа или нескольких скалярных переменных.

Для проверки результата выполнения динамической команды можно использовать команду `GET DIAGNOSTICS`, как и в случае статических команд (но не переменную `FOUND`).

```
DO $$
DECLARE
	rec RECORD;
	cnt BIGINT;
BEGIN
	EXECUTE 'INSERT INTO city_msk (name, architect, built) VALUES
		(''Пашков дом'', ''Василий Баженов'', 1784),
		(''Музей Пушкина'', ''Роман Клейн'', 1898),
		(''ЦУМ'', ''Роман Клейн'', 1908)
	RETURNING name, architect, built'
	INTO rec;
	RAISE NOTICE 'rec = %', rec;
	GET DIAGNOSTICS cnt = ROW_COUNT;
	RAISE NOTICE 'Добавлено строк: %', cnt;
END;
$$;
```

Результат динамического запроса можно обработать в цикле `FOR`:

```
DO $$
DECLARE
	rec RECORD;
BEGIN
	FOR rec IN EXECUTE 'SELECT * FROM city_msk ORDER BY built'
	LOOP
		RAISE NOTICE 'rec = %', rec;
	END LOOP;
END;
$$;
```

----
## Массивы

🔗 15. Массивы https://www.youtube.com/watch?v=7iarp1dKnq8

Массивы используются без явного определения как *type-name[]*. Состоят из элементов одного типа. Можно брать срезы массива; производить операции сравнения, проверки вхождения, пересечения, конкатенации, использовать с ANY и ALL вместо подзапроса, и др.

```
DO $$
DECLARE
	arr INTEGER[]; -- в скобках ничего не надо указывать
BEGIN
	arr := ARRAY[10, 20, 30];
	RAISE NOTICE 'arr = %', arr;
	-- !!! по умолчанию элементы нумеруются с единицы
	RAISE NOTICE '% % %', arr[1], arr[2], arr[3];
	-- срезы массива
	RAISE NOTICE 'Slice [2:3] = %', arr[2:3];
END;
$$;
```

Можно создать массив, получив его из подзапроса:

```
DO $$
DECLARE
	arr INTEGER[]; -- в скобках ничего не надо указывать
BEGIN
	arr := ARRAY( SELECT n FROM generate_series(1,10) AS n );
	RAISE NOTICE 'arr = %', arr;
END;
$$;
```

Можно массив преобразовать в таблицу функцией `unnest()`:

```
SELECT unnest( ARRAY[1, 2, 3] );
```

Можно делать многомерные массивы.

### Массивы и циклы

Напечатаем все элементы одномерного массива:

```
DO $$
DECLARE
	arr INTEGER[] := ARRAY[10, 20, 30, 40, 50];
BEGIN
	-- для одномерных массивов в строке ниже указывается 1:
	FOR i IN array_lower(arr, 1)..array_upper(arr, 1) LOOP
		RAISE NOTICE 'arr[%] = %', i, arr[i];
	END LOOP;
END;
$$;
```

Если индексы не нужны, можно просто итерировать элементы:

```
DO $$
DECLARE
	arr INTEGER[] := ARRAY[10, 20, 30, 40, 50];
	x INTEGER;
BEGIN
	FOREACH x IN ARRAY arr LOOP
		RAISE NOTICE 'x = %', x;
	END LOOP;
END;
$$;
```

Итерация индексов в двумерном массиве:

```
DO $$
DECLARE
	arr INTEGER[] := ARRAY[
		ARRAY[ 1,  2,  3],
		ARRAY[10, 20, 30]
	];
BEGIN
	FOR i IN array_lower(arr, 1)..array_upper(arr, 1) LOOP -- по строкам
		FOR j IN array_lower(arr, 2)..array_upper(arr, 2) LOOP -- по столбцам
			RAISE NOTICE 'arr[%][%] = %', i, j, arr[i][j];
		END LOOP;
	END LOOP;
END;
$$;
```

Ключевое слово `VARIADIC` в языке PL/pgSQL позволяет объявлять функции, способные принимать переменное количество аргументов. Это означает, что функция может быть вызвана с любым количеством аргументов, и эти аргументы будут обработаны внутри функции как массив. Использование `VARIADIC` делает функции более гибкими и позволяет обрабатывать неопределенное количество аргументов без необходимости создавать множество перегруженных версий функции. 

```
CREATE FUNCTION maximum(VARIADIC a INTEGER[]) RETURNS integer
AS $$
DECLARE
	x INTEGER;
	maxsofar INTEGER;
BEGIN
	FOREACH x IN ARRAY a LOOP
		IF x IS NOT NULL AND (maxsofar IS NULL OR x > maxsofar) THEN
			maxsofar := x;
		END IF;
	END LOOP;
	RETURN maxsofar;
END;
$$ IMMUTABLE LANGUAGE plpgsql;
```

Пробуем: `SELECT maximum(12, 65, 47);`.

Данную функцию можно сделать полиморфной.

Конструкция `%TYPE` в PL/pgSQL используется для автоматического определения типа данных переменной на основе типа данных столбца таблицы или другого объекта базы данных.

```
CREATE FUNCTION poly_maximum(VARIADIC a ANYARRAY, maxsofar OUT ANYELEMENT)
AS $$
DECLARE
	-- PL/pgSQL про anyarray/anyelement ничего не знает. Когда выполняется
	-- тело функции, туда передаются конкретные параметры.
	-- следующая строка означает: x будет иметь такой же тип, как maxsofar
	x maxsofar%TYPE;
BEGIN
	FOREACH x IN ARRAY a LOOP
		IF x IS NOT NULL AND (maxsofar IS NULL OR x > maxsofar) THEN
			maxsofar := x;
		END IF;
	END LOOP;
END;
$$ IMMUTABLE LANGUAGE plpgsql;
```

Пробуем: `SELECT maximum(12, 65, 47); SELECT poly_maximum(12.1, 65.2, 47.3);`.

----
## Обработка ошибок

🔗 Обработка ошибок https://www.youtube.com/watch?v=dpY9xkC8P-k

Обработка выполняется, если есть секция `EXCEPTION`.

```
DECLARE
	...
BEGIN
	...
	-- что-то делаем...
EXCEPTION
	WHEN no_data_found THEN
		RAISE NOTICE 'Нет данных';
	WHEN too_many_rows THEN
		...
END;
```

В PL/pgSQL обработка ошибок в блоке `EXCEPTION` позволяет вам перехватывать и обрабатывать ошибки, возникающие во время выполнения кода. Синтаксис секции `EXCEPTION` выглядит следующим образом:

```
BEGIN
 -- Операторы
 EXCEPTION WHEN условие THEN
 -- Обработчик ошибок
END;
```

Условие может быть именем ошибки, например `division_by_zero`, или кодом `SQLSTATE`, например `22012`. Если ошибка не соответствует ни одному из указанных условий, она передается наружу. В обработчике ошибок вы можете выполнять необходимые действия, такие как вывод сообщения об ошибке, изменение хода выполнения программы или даже повтор попытки выполнения операции. Важно помнить, что изменения, внесенные в базу данных до возникновения ошибки, будут отменены, но изменения, внесенные до начала блока, останутся неизменными. Пример обработки ошибки `division_by_zero`:

```
BEGIN
	INSERT INTO mytab(firstname, lastname) VALUES('Tom', 'Jones');
	UPDATE mytab SET firstname = 'Joe' WHERE lastname = 'Jones';
	x:= x + 1;
	y:= x / 0;
	EXCEPTION WHEN division_by_zero THEN
		RAISE NOTICE 'Перехватили ошибку division_by_zero';
		 RETURN x;
END;
```

В этом примере, если при выполнении `y := x / 0` произойдет ошибка деления на ноль, будет выполнено сообщение об ошибке и возвращено значение x, увеличенное на единицу.    

Тонкий момент: если ошибка произойдёт в секции `DECLARE`, или в самом обработчике внутри `EXCEPTION`, то в этом блоке её перехватить не получится.

В обработчике можно также указывать код ошибки. Например:

```
...
EXCEPTION
	WHEN SQLSTATE 'P0003' OR no_data_found THEN -- можно несколько
		...
END;
```

----
## Триггеры

🔗 Триггеры https://www.youtube.com/watch?v=F3jQRbsDXVE

**Триггер**: объект базы данных – список обрабатываемых событий; при возникновении события вызывается триггерная функция и ей передаётся контекст.

**Триггерная функция**: объект базы данных – код обработки события; выполняется в той же транзакции, что и основная операция. Соглашение: функция не принимает параметры, возвращает значение псевдотипа `trigger` (фактически `record`). Может использоваться в нескольких триггерах.

С помощью триггера можно отменить операцию, изменить её результат или выполнить дополнительные действия. Триггер выполняется как часть транзакции: ошибка в триггере приводит к откату транзакции.

События: `INSERT`, `UPDATE`, `DELETE`, `TRUNCATE`, условие `WHEN` устанавливает дополнительный фильтр.

**Before Statement**:
- Срабатывает: до операции.
- Возвращаемое значение: игнорируется.
- Контекст: TG-переменные.

**Before Row** (таблица) / **Instead of Row** (представления):
- Срабатывает: перед действием со строкой в процессе выполнения операции.
- Возвращаемое значение: строка (возможно измененная) или `NULL` (отменяет действие для данной строки).
- Контекст:
	- `OLD` (update, delete)
	- `NEW` (insert, update)
	- TG-переменные.

**After Row**
- Срабатывает: после выполнения операции; очередь из прошедших условие `WHEN`.
- Возвращаемое значение: игнорируется.
- Контекст:
	- `OLD`, `OLD TABLE` – update, delete
	- `NEW`, `NEW TABLE` – insert, update
	- TG-переменные

**After Statement**
- Срабатывает: после операции (даже если не затронута ни одна строка).
- Возвращаемое значение: игнорируется.
- Контекст:
	- `OLD TABLE` – update, delete
	- `NEW TABLE` – insert, update
	- TG-переменные

### Порядок вызова триггеров

Создадим "универсальную" триггерную функцию, которая описывает контекст, в котором она вызвана. Контекст передается в различных `TG_...`-переменных.

```
CREATE FUNCTION describe_tg() RETURNS TRIGGER
AS $$
DECLARE 
	rec RECORD;
	str TEXT := '';
BEGIN
	IF TG_LEVEL = 'ROW' THEN
		CASE TG_OP
			WHEN 'DELETE' THEN rec := OLD; str := OLD::text;
			WHEN 'UPDATE' THEN rec := NEW; str := OLD || ' -> ' || NEW;
			WHEN 'INSERT' THEN rec := NEW; str := NEW::text;
		END CASE;
	END IF;

	RAISE NOTICE '% % % %: %', TG_TABLE_NAME, TG_WHEN, TG_OP, TG_LEVEL, str;
	return rec;
END;
$$ LANGUAGE plpgsql;
```

Установим созданный триггер на некоторые события:

```
CREATE TRIGGER t_before_stmt
BEFORE INSERT OR UPDATE OR DELETE 	-- события
ON users							-- таблица
FOR EACH STATEMENT					-- уровень
EXECUTE FUNCTION describe_tg();		-- триггерная функция для вызова
```

Установив четыре триггера на BEFORE/AFTER STATEMENT, ROW при вставке увидим примерно такое:

```
NOTICE: users BEFORE INSERT STATEMENT: 
NOTICE: users BEFORE INSERT ROW: (11,Alex,,,f,,) 
NOTICE: users AFTER INSERT ROW: (11,Alex,,,f,,) 
NOTICE: users AFTER INSERT STATEMENT: 
INSERT 0 1
```

### Переходные таблицы

Переходные таблицы `old_table` и `new_table` "выглядят" настоящими, но не присутствуют в системном каталоге и располагаются в оперативной памяти.

> [!info] 
> Переходные таблицы содержать только те строки, которые были затронуты операцией.

Напишем триггерную функцию, которая показывает содержимое этих таблиц.

```
CREATE OR REPLACE FUNCTION transition_tg() RETURNS TRIGGER
AS $$
DECLARE 
	rec RECORD;
BEGIN
	IF TG_OP = 'DELETE' OR TG_OP = 'UPDATE' THEN
		RAISE NOTICE 'Старое состояние:';
		FOR rec IN SELECT * FROM old_table LOOP
			RAISE NOTICE '%', rec;
		END LOOP;
	END IF;

	IF TG_OP = 'UPDATE' OR TG_OP = 'INSERT' THEN
		RAISE NOTICE 'Новое состояние:';
		FOR rec IN SELECT * FROM new_table LOOP
			RAISE NOTICE '%', rec;
		END LOOP;
	END IF;

	RETURN NULL;
END;
$$ LANGUAGE plpgsql;
```

Теперь установим этот триггер с указанием имён таблиц:

```
CREATE TRIGGER t_after_upd_trans
AFTER UPDATE ON users
REFERENCING
	OLD TABLE AS old_table
	NEW TABLE AS new_table
FOR EACH STATEMENT
EXECUTE FUNCTION transition_tg();
```

После обновления строки, выведет примерно такое:

```
NOTICE: Старое состояние: 
NOTICE: (11,Alex,,,f,,) 
NOTICE: Новое состояние: 
NOTICE: (11,Alex,,,f,Gold,) 
UPDATE 1
```

### Особенности триггеров

- Сложную логику на триггерах почти невозможно отладить: код вызывается неявно, трудно проследить зависимости, крайне усложняется поддержка приложения.
- Нельзя полагаться на порядок выполнения триггеров для одного события, т.к. они выполняются в алфавитном порядке, и например добавление нового триггера может порядок изменить.

### Примеры использования триггеров

#### Пример 1: сохранение истории изменения строк

Поддержку "исторической" таблицы можно было бы возложить на приложение, но на уровне БД это надежнее. [Этот момент в видео](https://youtu.be/F3jQRbsDXVE?si=t5wD0NVKe5ObXyDN&t=2078).

#### Пример 2: обновляемое представление

[Видео](https://youtu.be/F3jQRbsDXVE?si=dOKqW3fEjDdbhsyB&t=2563)

### Событийные триггеры

Похожи на обычные "табличные" триггеры, но другой объект. Срабатывают на DDL-операции: `CREATE`, `ALTER`, `DROP`, etc. Инструмент больше для администратора, чем разработчика.

Триггерная функция: не принимает параметры, возвращает  значение псевдотипа `event_trigger`. Для получения контекста служат специальные функции.

События:
- `DDL_COMMAND_START` – перед выполнением команды
- `DDL_COMMAND_END` – после выполнения команды
- `TABLE_REWRITE` – перед перезаписью таблицы
- `SQL_DROP` – после удаления объектов

----
## Отладка

🔗 [Видео](https://www.youtube.com/watch?v=zoHn5zOiKio)

### Проверка корректности

Оператор `ASSERT` с двумя параметрами: первый – логический, должен вернуть истину, если всё хорошо; второй – текст ошибки. Например, `ASSERT X > 0, 'Х должен быть больше нуля';`.

### Debugger

Есть расширение `pldbgapi`. Поддержка его встроена в pgAdmin.

### Служебные сообщения

Это не только отладка кода: мониторинг долго выполняющихся процессов; ведение журнала приложения.

Подходы к реализации:
- вывод на консоль или в журнал сервера;
- запись в таблицу или в файл;
- передача информации другим процессам.

Команда `RAISE` имеет параметры: `DEBUG`, `LOG`, `NOTICE`, `INFO`, `WARNING`.

### Запись в таблицу: расширение `dblink`

Установим расширение (есть по умолчанию):

```
CREATE EXTENSION dblink;
```

Создадим таблицу для записи сообщений:

```
CREATE TABLE log (
	id 			INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
	username	TEXT,
	ts			TIMESTAMPTZ,
	message		TEXT
);
```

Теперь создадим процедуру для удобного добавления записей в таблицу `log`. Процедура открывает новый сеанс, выполняет вставку в отдельной транзакции и закрывает сеанс.

```
CREATE PROCEDURE write_log(message TEXT)
AS $$
DECLARE 
	cmd TEXT;
BEGIN
	cmd := format(
		'INSERT INTO log(username, ts, message)
		VALUES (%L, %L::timestamptz, %L)',
		user, clock_timestamp()::text, write_log.message
	);
	PERFORM dblink('dbname=' || current_database(), cmd);
END;
$$ LANGUAGE plpgsql;
```

### Запись в файл: расширение `adminpack`

Это расширение есть по умолчанию, установим его:

```
CREATE EXTENSION adminpack;
```

Сама функция для записи в файл:

```
CREATE PROCEDURE write_file(message TEXT)
AS $$
DECLARE
	filename CONSTANT text := '/var/lib/postgresql/data/log/user_log.txt';
	message TEXT;
BEGIN
	message := format(
		E'%s, %s, %s\n',
		session_user, clock_timestamp()::text, write_file.message
	);
	PERFORM pg_file_write(filename, message, /*append*/ true);
END;
$$ LANGUAGE plpgsql;
```

https://youtu.be/zoHn5zOiKio?si=0dIH7qu5YneKSbXd&t=2435 закончил смотреть 12 мая 2024 г.