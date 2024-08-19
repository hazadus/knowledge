📂 [[Базы Данных]] 

----
## Using `sqlite3`
==Reference: https://www.sqlitetutorial.net ==

### Connect to database
```python
import sqlite3  
  
with sqlite3.connect("hw_4_database.db") as conn:  
    cursor = conn.cursor()  
  
    # Question 1:  
    cursor.execute("SELECT COUNT(*) FROM salaries WHERE salary < 5000")  
    result = cursor.fetchone()  
    print("1.", result[0])
```
### Create new tables
https://www.sqlitetutorial.net/sqlite-python/creating-tables/
```python
def reset_database() -> None:  
    if os.path.exists(DATABASE_FILENAME):  
        os.remove(DATABASE_FILENAME)  
  
    with sqlite3.connect(DATABASE_FILENAME) as conn:  
        cursor = conn.cursor()  
        cursor.execute(  
            """  
            CREATE TABLE characters (                
	            id integer PRIMARY KEY,                
	            name text,                
	            gender text,                
	            birth_year text            
	        );            
	        """  
        )
```


----
📂 [[Базы данных]] | Последнее изменение: 11.08.2024 10:40