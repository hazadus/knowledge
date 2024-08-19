### Inline if…else statement
```Python
# expression_if_true if condition else expression_if_false
print('Победил {}'.format(warrior1.name if warrior1.health else warrior2.name))
```
### Walrus operator
[https://realpython.com/python38-new-features/#the-walrus-in-the-room-assignment-expressions](https://realpython.com/python38-new-features/#the-walrus-in-the-room-assignment-expressions)
```Python
print(walrus := True)
inputs = list()
while (current := input("Write something: ")) != "quit":
    inputs.append(current)
```
### Ellipsis

> [!info] When Do You Use an Ellipsis in Python? - Real Python  
> While you can use .  
> [https://realpython.com/python-ellipsis/](https://realpython.com/python-ellipsis/)

----
📂 [[Python]] | Последнее изменение: 07.02.2024 15:09