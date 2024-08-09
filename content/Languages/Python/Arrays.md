📂 [[Python]]

Examples: [python-learn](https://github.com/hazadus/python-learn)

```python
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

----

## Cartesian product using list comprehension
```python
from keyword import kwlist  
  
DOMAINS = ["dev", "io"]  
  
# Build list of Python keywords with each suffix in DOMAINS list:  
site_domains = [f"{kw}.{domain}" for kw in kwlist for domain in DOMAINS]  
  
print(site_domains)
```
