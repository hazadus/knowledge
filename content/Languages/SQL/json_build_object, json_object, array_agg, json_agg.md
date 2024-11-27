## Пример 1

### Запрос к БД

Задача: хотим получить количество записей с разбивкой по датам (на основе поля `created_at` типа `TIMESTAMP`) в формате JSON.

```json
{
  "visits": {
    "2024-11-13": "250",
    "2024-11-14": "54",
    "2024-11-15": "263",
    "2024-11-16": "63",
    "2024-11-17": "26",
    "2024-11-18": "30",
    "2024-11-19": "14",
    "2024-11-20": "9",
    "2024-11-21": "4",
    "2024-11-22": "4"
  }
}
```

В результате запроса, из БД придёт одна строка с одним столбцом `json_build_object` с приведённым выше JSON.

Запрос:

```sql
SELECT
    json_build_object(
        'visits', visits
    )
FROM (
	select json_object(
		array_agg(v1.created_date::text),
		array_agg(v1.visits::text)
	) as visits
	from (
		select
			date(created_at) as created_date,
			COUNT(*) as visits
		from visits
		where link_id = 372
		group by created_date
		order by created_date asc
	) v1
)
```

В данном случае, `json_object` принимает два массива и попарно соединяет их элементы в качестве ключа и значения в объекте JSON.

### Работа из кода на Go

```go
type Visits struct {
	Visits map[string]string `json:"visits"`
}

func (s *Visits) Scan(value interface{}) error {
	b, ok := value.([]byte)
	if !ok {
		return errors.New("type assertion to []byte failed")
	}
	return json.Unmarshal(b, &s)
}

// ...

visitsQuery := fmt.Sprintf(`
	SELECT
	json_build_object(
		'visits', visits
	)
	FROM (
		SELECT json_object(
			array_agg(v1.created_date::text),
			array_agg(v1.visits::text)
		) AS visits
		FROM (
			SELECT
				date(created_at) AS created_date,
				COUNT(*) AS visits
			FROM visits
			GROUP BY created_date
			ORDER BY created_date ASC
		) v1
	)`,
)

ctx, cancel := context.WithTimeout(context.Background(), defaultQueryTimeout)
defer cancel()

rows, err := m.db.QueryContext(ctx, query)
if err != nil {
	return nil, err
}

rows.Next()
visits := Visits{}
err = rows.Scan(&visits)
if err != nil {
	return nil, err
}

```

## Пример 2

### Запрос к БД

Задача: хотим получить из БД список записей в формате JSON в таком виде:

```json
{
      "oses": [
        {
          "os": "iOS",
          "visit_count": 343
        },
        {
          "os": "Android",
          "visit_count": 290
        },
        {
          "os": "Windows",
          "visit_count": 32
        },
        {
          "os": "MacOS",
          "visit_count": 19
        },
        {
          "os": "",
          "visit_count": 18
        },
        {
          "os": "Linux",
          "visit_count": 15
        }
      ]
    }
```

Запрос:

```sql
SELECT
    json_build_object(
        'oses', oses
    )
FROM (
	select json_agg(v1) as oses
	from (
		select os, count(os) as visit_count
		from visits 
		where link_id = 372
		and (date(created_at) between '2024-11-13' and '2024-11-24')
		group by os
		order by visit_count desc
	) v1
)
```

В результате запроса, из БД придёт одна строка с одним столбцом `json_build_object` с приведённым выше JSON.

### Работа из кода на Go

Аналогично первому примеру, но нужно по другому определить тип.

```go
type OsStatsItem struct {
	OS         string `json:"os"`
	VisitCount int64  `json:"visit_count"`
}

type OsStats struct {
	Oses []*OsStatsItem `json:"oses"`
}

func (s *OsStats) Scan(value interface{}) error {
	b, ok := value.([]byte)
	if !ok {
		return errors.New("type assertion to []byte failed")
	}
	return json.Unmarshal(b, &s)
}
```

В остальном, получение этой записи из БД будет аналогично.

## Справочные материалы

- [json_build_object](https://www.postgresql.org/docs/17/functions-json.html)
- [json_object](https://www.postgresql.org/docs/17/functions-json.html)
- [array_agg](https://www.postgresql.org/docs/17/functions-json.html)
- [Using PostgreSQL JSONB with Go](https://www.alexedwards.net/blog/using-postgresql-jsonb)

----
📂 [[PostgreSQL]] | [[Go]]

----
📂 [[SQL]] | Последнее изменение: 27.11.2024 13:44