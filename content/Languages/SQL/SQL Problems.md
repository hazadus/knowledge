[[SQL]]

----

Интересные задачки по SQL, варианты решения мои и те что понравились. Для более детального изучения интересных решений.

----
## 596. Classes More Than 5 Students

🔗 [Leetcode](https://leetcode.com/problems/classes-more-than-5-students/?envType=study-plan-v2&envId=top-sql-50)

My solution:

```sql
SELECT t.class AS class
FROM (
    SELECT class, COUNT(DISTINCT student) AS count
    FROM Courses
    GROUP BY class
) AS t
where t.count >= 5;
```

Other solutions:

```sql
with g as (select class, count(student) c from courses group by 1)
select class from g where c > 4
```

```sql
select class from courses group by class having count(*) >= 5
```

----



----
📂 [[SQL]] | Последнее изменение: 09.04.2024 16:43