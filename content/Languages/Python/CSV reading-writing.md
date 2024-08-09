> [!info] csv - CSV File Reading and Writing - Python 3.10.7 documentation  
> The so-called CSV (Comma Separated Values) format is the most common import and export format for spreadsheets and databases.  
> [https://docs.python.org/3/library/csv.html](https://docs.python.org/3/library/csv.html)  

> [!info] csv - CSV File Reading and Writing - Python 3.10.7 documentation  
> The so-called CSV (Comma Separated Values) format is the most common import and export format for spreadsheets and databases.  
> [https://docs.python.org/3/library/csv.html#examples](https://docs.python.org/3/library/csv.html#examples)  
```Python
import csv
with open('names.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['first_name'], row['last_name'])

>>> print(row)
{'first_name': 'John', 'last_name': 'Cleese'}

with open(OUTPUT_CSV_FILE, 'w', newline='') as output_file:
    writer = csv.writer(output_file)
    writer.writerows(sorted_words)
```

> [!info] medium-automation/word_count.py at master · hazadus/medium-automation  
> This file contains bidirectional Unicode text that may be interpreted or compiled differently than what appears below.  
> [https://github.com/hazadus/medium-automation/blob/master/word_count.py](https://github.com/hazadus/medium-automation/blob/master/word_count.py)