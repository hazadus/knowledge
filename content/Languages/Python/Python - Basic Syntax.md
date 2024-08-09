## Операторы
Возведение в степень: `**`.
### match / case
```Bash
def likes(names):
    match names:
        case []: return 'no one likes this'
        case [a]: return f'{a} likes this'
        case [a, b]: return f'{a} and {b} like this'
        case [a, b, c]: return f'{a}, {b} and {c} like this'
        case [a, b, *rest]: return f'{a}, {b} and {len(rest)} others like this'
# https://www.codewars.com/kata/reviews/564425cc55d0e45b8c000087/groups/6287deb8c864c80001d0e16b
```
## Типы данных
### Lists = Списки

> [!info] 5. Data Structures - Python 3.10.7 documentation  
> This chapter describes some things you've learned about already in more detail, and adds some new things as well.  
> [https://docs.python.org/3/tutorial/datastructures.html](https://docs.python.org/3/tutorial/datastructures.html)  
- **Примеры**
    
    ```Python
    new_list = list()  # объявление по уму
    
    book_IDs = [1, 2, 3, 4, 5]  # Declare dictionary
    book_IDs.append(6)  # append
    book_IDs[0] *= 5  # access 
    
    len(book_IDs)  # get size of dictionary
    
    new_nums = nums[:]  # create copy
    
    word = list("word")  # convert string to list
    
    for id in book_IDs:  # iterate
        pass
    
    if 1 in book_IDs:  # check if number is there
       pass
    
    members = list(range(1, 6))  # = [1, 2, 3, 4, 5]
    
    some_list = [12, 34, 56, 3.14, "abc"]
    print(some_list)
    print('List length: {}'.format(len(some_list)))
    print(some_list[1])
    print(some_list[1:3])
    
    nums[:3] = [1, 1, 1]  # replace first three elements with 1s
    nums[:3] = [1]  # replace first three elements with ONE 1
    
    some_list[2] = "def"  # lists are mutable unlike strings
    
    # Concatenate lists
    another_list = [27, 63, "mtg", 36.6, "abc"]
    new_list = some_list + another_list  # SLOW, do not use! Use extend instead
    
    # Extend
    some_list.extend(another_list)  # Extend the list by appending all the items from the iterable. Equivalent to a[len(a):] = iterable.
    
    # Adding items to lists
    new_list.append("appended item")
    new_list.insert(0, "inserted item")
    
    # Removing items from list
    new_list.pop()  # = pop(-1) - remove last item. NB! pop returns deleted item
    new_list.pop(0)  # remove first item
    
    new_list.remove("abc")  # remove first entry of passed value
    
    # Sorting
    number_list = [9, 8, 7, 6, 5, 4, 1]
    number_list.sort()
    
    number_list.reverse()
    ```
    
### List comprehensions / Представление списков

> [!info] 5. Data Structures - Python 3.10.7 documentation  
> This chapter describes some things you've learned about already in more detail, and adds some new things as well.  
> [https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions)  
- **Примеры**
    
    ```Python
    squares = [x**2 for x in range(10)]
    
    import random
    squad = [random.randint(30, 80) for _ in range(10)]
    ```
    
    ![[attachments/Untitled 24.png|Untitled 24.png]]
    
    ```Python
    squares_odd = [x**2 for x in range(10) if x % 2 != 0]  # if
    squares_cubes = = [(x**2 if x % 2 != 0 else x**3) for x in range(10)]  # if-else
    ```
    
    ![[attachments/Untitled 1 10.png|Untitled 1 10.png]]
    
    ```Python
    nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
                 [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]
    
    print([nice_list[i][j][k] for i in range(len(nice_list))
           for j in range(len(nice_list[i]))
           for k in range(len(nice_list[i][j]))
           ])
    #
    # == equals to:
    #
    print([k for i in nice_list for j in i for k in j])
    
    # Output:
    # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
    # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
    ```
    
### Strings

> [!info] Built-in Types - Python 3.10.7 documentation  
> The following sections describe the standard types that are built into the interpreter.  
> [https://docs.python.org/3/library/stdtypes.html?highlight=strip#text-sequence-type-str](https://docs.python.org/3/library/stdtypes.html?highlight=strip#text-sequence-type-str)  

> [!info] string - Common string operations - Python 3.10.7 documentation  
> Source code: Lib/string.  
> [https://docs.python.org/3/library/string.html#format-specification-mini-language](https://docs.python.org/3/library/string.html#format-specification-mini-language)  

> [!info] How to Replace a String in Python - Real Python  
> support_tom] 2022-08-24T10:02:23+00:00 : What can I help you with?  
> [https://realpython.com/replace-string-python/](https://realpython.com/replace-string-python/)  
- **Примеры**
    
    ```Python
    len("string")  # length of string
    
    # Formatting
    #
    # https://docs.python.org/3/library/string.html\#format-specification-mini-language
    #
    print("/usr/{user}/projects/{filename}".format(
    	user=user_name,
    	filename=filename
    ))
    
    # Float formatting
    print("Float format: {0:1.3f}".format(1000 / 7))
    print("Float format: {0:10.3f}".format(1000 / 7))
    print("Цена {:.2f} рублей".format(price))
    print("Рост на {:.1%} рублей".format(percent))
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")
    
    # Int formatting
    print('Word count: {:,d}'.format(len(all_words)))  # Word count: 9,352
    print('Quantity: {:.0e}'.format(qty))  # 4e+08
    print("{} — {} штук, стоимость {:_d} рублей".format(prod_name, qty, cost).replace('_', ' '))  # Стул — 105 штук, стоимость 10 311 рублей
    
    # More Formatting
    f"{name = :>10}" # The >10 format specifier says that name should be right-aligned within a 10 character string.
    
    # *** Debug ***
    # You can now add = at the end of an expression, and it will print both the expression and its value:
    >>> python = 3.8
    >>> f"{python=}"
    'python=3.8'
    
    # You can add spaces around =, and use format specifiers as usual:
    >>> name = "Eric"
    >>> f"{name = }"
    "name = 'Eric'"
    
    >>> f"{name = :>10}"
    'name =       Eric'
    
    def create_phone_number(n):
    	return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)
    
    # Indexing
    print(text_string[1])
    print(text_string[5])
    print(text_string[-1])  # last character
    
    # Slicing
    print(text_string[7:14])  # от начала
    print(text_string[-8:-1])  # от конца
    print(text_string[-8:])  # от позиции и до конца
    print(text_string[:6])  # от начала и до позиции
    print(text_string[::2])  # выводит каждый второй символ
    print(text_string[::-1])  # reverse order
    print('10:', alphabet[3:5][::-1])  # reverse part of string
    
    # Splitting
    location = "ПАРК ПРИЕМА/03"
    park, track = location.split("/")
    print(f"Парк - {park}, путь - {track}")
    
    # Join
    str_1 = "I love "
    str_2 = "Python."
    print(''.join([str_1, str_2]))
    
    # Multiplication
    print(text_string * 2)
    
    #
    # Methods
    #
    print(text_string.upper())
    print(text_string.lower())  # NB: strings are immutable!
    
    # Split
    print(text_string.split())
    print(text_string.split('и'))
    
    # Strip / split
    user_list_str = user_str.strip('[]').split(',')
    
    # Remove punctuation symbols
    temp_str = source_str.translate(str.maketrans('', '', string.punctuation))
    ```
    
### Dictionaries

> [!info] 5. Data Structures - Python 3.10.7 documentation  
> This chapter describes some things you've learned about already in more detail, and adds some new things as well.  
> [https://docs.python.org/3/tutorial/datastructures.html#dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)  

> [!info] Обзор возможностей словаря dict в Python.  
> Словари встречаются и в других языках как, только называются по разному, например "ассоциативная память" или "ассоциативные массивы".  
> [https://docs-python.ru/tutorial/ispolzovanie-slovarej-dict-python/](https://docs-python.ru/tutorial/ispolzovanie-slovarej-dict-python/)  
- **Примеры**
    
    ```Python
    new_dict = dict()  # создание по уму
    
    car_prices = {"Kia": 3000, "Mazda": 5000, "Volvo": 7000}
    print(car_prices)
    print(f"Kia price is: {car_prices['Kia']}")
    car_prices['Hyundai'] = 3100  # add item
    del car_prices['Volvo']  # delete item
    print(car_prices)
    car_prices.clear()  # clear dictionary
    print(car_prices)
    
    # Check if there's a nested dict there
    # {} is the default returned value if there's no such key in dict
    if data.get('config', {}).get('param', {}).get('param1', {}):
    		print('param1 is there...')
    
    # Advanced
    person = {
        'first name': 'Alex',
        'last name': 'Gold',
        'nickname': 'Hazadus',
        'age': 38,
        'hobbies': ['mtg', 'vinyl', 'coding'],
        'children': {
            'son1': 'Michael',
            'son2': 'Vladimir',
            'son3': 'Dmitry'
        }
    }
    
    for key in person:
    	print(key, person[key])
    
    for key in sorted(person.keys()):  # sort keys
    
    max(dictionary.values())  # get max value
    
    dict1.update(dict2)  # add + update
    dict1.pop("key")  # delete + return dict1["key"] value
    
    print(person['age'])
    print(person['hobbies'])
    print(person['hobbies'][1])
    print(person['children']['son2'])
    
    person['car'] = "Kia"  # add item
    person['hobbies'][1] = "music"
    
    print(person.keys())
    print(person.values())
    print(person.items())
    
    # Get key by value in dict
    my_dict ={"Java":100, "Python":112, "C":11}
     
    # one-liner
    print("One line Code Key by value: ", 
    			list(my_dict.keys())[list(my_dict.values()).index(100)]  # "Java"
    )
    ```
    
    ```Python
    cities = {'London': '2', 'Tokyo': '3', 'New York': '1'}
    print(sorted(cities.items(),key=lambda d:d[1]))
    # [('New York', '1'), ('London', '2'), ('Tokyo', '3')]
    ```
    
### Set / множество

> [!info] 5. Data Structures - Python 3.10.7 documentation  
> This chapter describes some things you've learned about already in more detail, and adds some new things as well.  
> [https://docs.python.org/3/tutorial/datastructures.html#sets](https://docs.python.org/3/tutorial/datastructures.html#sets)  

> [!info] Теория множеств: основы и базовые операции над множествами  
> Сегодня поговорим о структуре данных, которая в теории очень догматична, а на практике очень популярна.  
> [https://ru.hexlet.io/blog/posts/teoriya-mnozhestv-osnovy-i-bazovye-operatsii-nad-mnozhestvami](https://ru.hexlet.io/blog/posts/teoriya-mnozhestv-osnovy-i-bazovye-operatsii-nad-mnozhestvami)  

> [!info] Использование множеств set.  
> Примечание: для создания пустого множества вы должны использовать встроенный класс set(), а не '{}'.  
> [https://docs-python.ru/tutorial/ispolzovanie-mnozhestv-set-python/](https://docs-python.ru/tutorial/ispolzovanie-mnozhestv-set-python/)  
### Tuple / кортеж
```Python
# Tuples are immutable
tuple1 = (1, 2, 3)
tuple2 = ('one', 'two', 'three')
tuple3 = (1, "word", 3.14, 1)
tuple_person = ("Alex", "Gold")
name, last_name = tuple_person
print(tuple3[1])
print(tuple3.count(1))  # = 2
```
## Enumerate
![[attachments/Untitled 2 9.png|Untitled 2 9.png]]
## Generators

> [!info] Glossary - Python 3.10.7 documentation  
> The default Python prompt of the interactive shell.  
> [https://docs.python.org/3/glossary.html#term-generator-iterator](https://docs.python.org/3/glossary.html#term-generator-iterator)  
```Python
my_string = 'abcd'
my_tuple = (10, 20, 30, 40, 50)
zipped = ((my_string[i], my_tuple[i])
          for i in range(min(len(my_string), len(my_tuple))))
print(zipped)
# <generator object <genexpr> at 0x102c3c200>
```
## **Аргументы *args и **kwargs**
![[attachments/Untitled 3 8.png|Untitled 3 8.png]]
## Exceptions
![[attachments/Untitled 4 7.png|Untitled 4 7.png]]
## Библиотеки
### collections
[https://proglib.io/p/ne-izobretat-velosiped-ili-obzor-modulya-collections-v-python-2019-12-15](https://proglib.io/p/ne-izobretat-velosiped-ili-obzor-modulya-collections-v-python-2019-12-15)
Основные составляющие модуля collections:
1. [Counter](https://docs.python.org/3/library/collections.html#counter-objects) – инструмент подсчёта неизменяемых объектов. Используйте, если нужно определить количество вхождений или число наиболее (наименее) часто встречающихся элементов.
2. [defaultdict](https://docs.python.org/3/library/collections.html#defaultdict-objects) – словарь, умеющий при вызове отсутствующего ключа вместо вызова исключения `KeyError` записывать значение по умолчанию (работает быстрее, чем метод `setdefault()`).
3. [OrderedDict](https://docs.python.org/3/library/collections.html#ordereddict-objects) – словарь с памятью порядка добавления элементов, умеющий переупорядочивать элементы лучше, чем `dict`.
4. [ChainMap](https://docs.python.org/3/library/collections.html#collections.ChainMap) – контейнер комбинаций словарей с поиском, обобщением ключей и элементов.
5. [namedtuple()](https://docs.python.org/3/library/collections.html#namedtuple-factory-function-for-tuples-with-named-fields) – функция-фабрика для создания именованного кортежа. Это один из простейших способов сделать код более ясным: использовать вместо индексов имена.
6. [deque](https://docs.python.org/3/library/collections.html#deque-objects) – двусторонняя очередь – список, оптимизированный для вставки и удаления элементов с обоих концов с методом подсчёта вхождений
7. [UserDict](https://docs.python.org/3/library/collections.html#userdict-objects), [UserList](https://docs.python.org/3/library/collections.html#userlist-objects), [UserString](https://docs.python.org/3/library/collections.html#userstring-objects) – не заслуживающие развёрнутого описания обертки над стандартными объектами словарей, списков и строк для беспроблемного наследования (прямое наследование встроенным типам `dict`, `list`, `str` чревато ошибками, связанными с игнорированием переопределения методов).
Также у модуля collections имеется наследованный модуль коллекции абстрактных базовых классов `сollections.abc`.
### Regular Expressions / regexp

> [!info] re - Regular expression operations - Python 3.10.7 documentation  
> This module provides regular expression matching operations similar to those found in Perl.  
> [https://docs.python.org/3/library/re.html?highlight=re#module-re](https://docs.python.org/3/library/re.html?highlight=re#module-re)  

> [!info] How to Replace a String in Python - Real Python  
> support_tom] 2022-08-24T10:02:23+00:00 : What can I help you with?  
> [https://realpython.com/replace-string-python/](https://realpython.com/replace-string-python/)  

> [!info] Regular Expressions: Regexes in Python (Part 1) - Real Python  
> In this tutorial, you'll explore regular expressions, also known as regexes, in Python.  
> [https://realpython.com/regex-python/](https://realpython.com/regex-python/)  

> [!info] RegExr: Learn, Build, & Test RegEx  
> Regular expression tester with syntax highlighting, PHP / PCRE & JS Support, contextual help, cheat sheet, reference, and searchable community patterns.  
> [https://regexr.com/](https://regexr.com/)  
```Python
import re
message = re.sub(r'[\W\d]', r' ', message)  # remove all digits and non-word characters from string
re.sub(r'[euioaEUIOA]', r'', string_)  # remove all vowels from string_
```
### random

> [!info] random - Generate pseudo-random numbers - Python 3.10.7 documentation  
> Source code: Lib/random.  
> [https://docs.python.org/3/library/random.html#examples](https://docs.python.org/3/library/random.html#examples)  
- **Примеры**
    
    ```Python
    import random
    
    >>> random()                             # Random float:  0.0 <= x < 1.0
    0.37444887175646646
    
    >>> uniform(2.5, 10.0)                   # Random float:  2.5 <= x <= 10.0
    3.1800146073117523
    
    >>> expovariate(1 / 5)                   # Interval between arrivals averaging 5 seconds
    5.148957571865031
    
    >>> randrange(10)                        # Integer from 0 to 9 inclusive
    7
    
    >>> randrange(0, 101, 2)                 # Even integer from 0 to 100 inclusive
    26
    
    >>> choice(['win', 'lose', 'draw'])      # Single random element from a sequence
    'draw'
    
    #
    # My examples:
    #
    squad1 = [round(random.uniform(5.0, 10.0), 2) for _ in range(20)]
    # [6.95, 7.99, 6.57, 7.25, 7.33, 7.84, 8.77, 6.69, 9.13, 7.21, 6.91, 6.53, 5.6, 6.28, 6.67, 6.24, 6.56, 5.02, 8.81, 9.2]
    ```
    
    ```Python
    from random import choices
    
    # Return a list with 14 items.
    # The list should contain a randomly selection of the values from a specified list, 
    # and there should be 10 times higher possibility to select "apple" than the other two:
    
    mylist = ["apple", "banana", "cherry"]
    
    print(choices(mylist, weights = [10, 1, 1], k = 14))
    
    # https://www.w3schools.com/python/ref_random_choices.asp
    ```
    
### os, sys
```Python
uploads_dir = os.path.dirname(app.instance_path) + '/static/uploads'
uploads = [[file, os.stat(os.path.join(uploads_dir, file)).st_size] for file in os.listdir(uploads_dir)]
```
```Python
import os
rel_path = os.path.join('folder', folder_name, file_name)
```
```Python
abs_path = os.path.abspath(file_name)
abs_path = os.path.abspath(os.path.join(os.path.sep, file_name))  # file in system root dir; os.path.sep = '/' or '\'
```
```Python
os.path.exists(path)  # check if dir or file exists
```
## File read / write
- **Примеры**
    
    ![[attachments/Untitled 5 7.png|Untitled 5 7.png]]
    
    ![[attachments/Untitled 6 7.png|Untitled 6 7.png]]
    
    ![[attachments/Untitled 7 5.png|Untitled 7 5.png]]
    
## Classes

> [!info] Providing Multiple Constructors in Your Python Classes - Real Python  
> Sometimes you need to write a Python class that provides multiple ways to construct objects.  
> [https://realpython.com/python-multiple-constructors/](https://realpython.com/python-multiple-constructors/)  

> [!info] Python's Instance, Class, and Static Methods Demystified - Real Python  
> Let's begin by writing a (Python 3) class that contains simple examples for all three method types: NOTE: For Python 2 users: The @staticmethod and @classmethod decorators are available as of Python 2.  
> [https://realpython.com/instance-class-and-static-methods-demystified/#class-methods](https://realpython.com/instance-class-and-static-methods-demystified/#class-methods)  
### Принципы ООП
- Основные принципы ООП
    
    ![[attachments/Untitled 8 3.png|Untitled 8 3.png]]
    
    ![[attachments/Untitled 9 3.png|Untitled 9 3.png]]
    
    ![[attachments/Untitled 10 3.png|Untitled 10 3.png]]
    
    ![[attachments/Untitled 11 3.png|Untitled 11 3.png]]
    
### MRO (Method Resolution Order)

> [!info] Введение в множественное наследование и super()  
> Введение в множественное наследование и super() для Python-разработчиков.  
> [https://pythonist.ru/vvedenie-v-mnozhestvennoe-nasledovanie-i-super/](https://pythonist.ru/vvedenie-v-mnozhestvennoe-nasledovanie-i-super/)  
- **Проблема алмаза**
    
    ![[attachments/Untitled 12 3.png|Untitled 12 3.png]]
    
    ![[attachments/Untitled 13 3.png|Untitled 13 3.png]]
    
## Decorators
![[attachments/Untitled 14 2.png|Untitled 14 2.png]]
Функция первого класса / Функция высшего порядка

> [!info] Путь к пониманию декораторов в Python  
> Прим.  
> [https://habr.com/ru/company/wunderfund/blog/657355/](https://habr.com/ru/company/wunderfund/blog/657355/)  
![[attachments/Untitled 15 2.png|Untitled 15 2.png]]
![[attachments/Untitled 16 2.png|Untitled 16 2.png]]
### Abstract Base Class (ABC), abstract method
```Python
from abc import ABC, abstractmethod
class Figure(ABC):
...
@abstractmethod
def move(self):
...
```
### Context Manager
![[attachments/Untitled 17 2.png|Untitled 17 2.png]]
![[attachments/Untitled 18 2.png|Untitled 18 2.png]]
Exception handling in **exit**
![[attachments/Untitled 19 2.png|Untitled 19 2.png]]
### Setter / getter
[https://realpython.com/python-getter-setter/](https://realpython.com/python-getter-setter/)
![[attachments/Untitled 20 2.png|Untitled 20 2.png]]
### @classmethod / @staticmethod
static method – without self as parameter – deprecated, use class method insted
class method – with cls as first parameter
### @contextmanager
Функция как менеджер контекста
![[attachments/Untitled 21 2.png|Untitled 21 2.png]]
### Декоратор с параметром
![[attachments/Untitled 22 2.png|Untitled 22 2.png]]
![[attachments/Untitled 23 2.png|Untitled 23 2.png]]

> [!info] Понимаем декораторы в Python'e, шаг за шагом. Шаг 2  
> И снова доброго времени суток всем читателям!  
> [https://habr.com/ru/post/141501/](https://habr.com/ru/post/141501/)  
Тут есть про декорирование декораторов
![[attachments/Untitled 24 2.png|Untitled 24 2.png]]
### Декорирование класса
![[Untitled 25.png]]
### Декорирование всех методов класса
![[Untitled 26.png]]
![[Untitled 27.png]]
### Класс как декоратор
![[Untitled 28.png]]
## **Пространство имён и области видимости (17.2 )**
![[Untitled 29.png]]
![[Untitled 30.png]]
## Функциональное программирование

> [!info] Python и функциональное программирование  
> Функциональное программирование - это одна из парадигм программирования.  
> [https://pythonchik.ru/osnovy/funkcionalnoe-programmirovanie-v-python](https://pythonchik.ru/osnovy/funkcionalnoe-programmirovanie-v-python)  

> [!info] Функциональное программирование в Python. Генераторы, как питонячий декларативный стиль  
> Общее введение ФП Введение в ФП Основные принципы ФП Основные термины Встроенное ФП поведение в Python Библиотека Xoltar Toolkit Библиотека returns Литература Генераторы Введение в итераторы Введение в генераторы Генераторы vs итераторы Генераторы как пайплайн Концепт yield from Маршрутизация данных на генераторах (мультиплексирование, броадкастинг) Пример трейсинга генератора Стандартные инструменты генераторы Литература Итоги Говоря о Python, обычно используется процедурный и ООП стиль программирования, однако это не значит, что другие стили невозможны.  
> [https://habr.com/ru/post/517438/](https://habr.com/ru/post/517438/)  
### itertools
[https://all-python.ru/osnovy/itertools.html#kombinatsiya-znachenij](https://all-python.ru/osnovy/itertools.html#kombinatsiya-znachenij)
[https://proglib.io/p/iteriruemsya-pravilno-20-priemov-ispolzovaniya-v-python-modulya-itertools-2020-01-03](https://proglib.io/p/iteriruemsya-pravilno-20-priemov-ispolzovaniya-v-python-modulya-itertools-2020-01-03)
- **Размещение с повторениями**
    
    Размещение с повторениями (выборка с возвращением) – это комбинаторное размещение объектов, в котором каждый объект может участвовать в размещении несколько раз. Например, есть пин-код из четырех цифр. На каждой позиции стоит цифра от `0` до `9`. Позиции не зависят друг от друга. Переберем все возможные коды:
    
    ```Python
    digits = range(10)
    pincode_vars = itertools.product(digits, repeat=4)
    for var in pincode_vars:
        print(var)
    
    # (0, 0, 0, 0)
    # (0, 0, 0, 1)
    # (0, 0, 0, 2)
    # ...
    # (9, 9, 9, 8)
    # (9, 9, 9, 9)
    ```