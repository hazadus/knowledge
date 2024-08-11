> [!info] The Twelve-Factor App  
> An app's config is everything that is likely to vary between deploys (staging, production, developer environments, etc).  
> [https://12factor.net/config](https://12factor.net/config)  
### Sort various objects
```Python
sorted(create_students_list(), key=lambda student: student.average_marks())
```
![[main.py]]
### Iterate over two variables
```Python
list1 = [1, 3, 6, 2, 5]
list2 = [0, 4, 1, 9, 7]
for i, j in zip(list1, list2):
    print("value1 =", i, "value2 =", j, sep = " ")
```
### Reverse a list
```Python
input_list  = [1, 2, 3, 4, 5]
output_list = input_list[::-1]
print(output_list)
```
### **Generate all combinations of two lists**
```Python
from itertools import product
list1 = ["A", "B", "C"]
list2 = [1, 2]
combinations = list(product(list1, list2))
print(combinations)
# [('A', 1), ('A', 2), ('B', 1), ('B', 2), ('C', 1), ('C', 2)]
```

----
📂 [[Python]]