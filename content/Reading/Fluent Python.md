## Fluent Python. Lucian Ramalho

#book #programming #python 

[[Books Reading]] | [[Идеи для Hazadus.ru]] | [[Books About Concurrency In Python]]

[[Luciano Ramalho. Fluent Python. Clear, Concise, and Effective Programming.pdf]]

----
## Материалы
- https://www.fluentpython.com
- https://ciberlandia.pt/@LR
- [Комментарии Ботаним к "Python. К вершинам мастерства"](https://www.youtube.com/playlist?list=PLAk6CfuV7hyoUuogKEElfagQk2fRkjnxJ).

----
- [x] 1. The Python Data Model (09.12.2023)
- [x] 2. An Array of Sequences (10.12.2023)
- [x] 3. Dictionaries and Sets
- [ ] 4. Unicode Text Versus Bytes
- [ ] 5. Data Class Builders
- [ ] 6. Object References, Mutability, and Recycling
- [ ] 7. Functions as First-Class Objects
- [ ] 8. Type Hints in Functions
- [ ] 9. Decorators and Closures
- [ ] 10. Design Patterns with First-Class Functions
- [ ] 11. A Pythonic Object
- [ ] 12. Special Methods for Sequences
- [ ] 13. Interfaces, Protocols, and ABCs
- [ ] 14. Inheritance: For Better or for Worse
- [ ] 15. More About Type Hints
- [ ] 16. Operator Overloading
- [ ] 17. Iterators, Generators, and Classic Coroutines
- [ ] 18. `with`, `match`, and `else` Blocks
- [x] 19. Concurrency Models in Python (09.12.2023)
- [x] 20. Concurrent Executors (10.12.2023)
- [ ] 21. Asynchronous Programming
- [ ] 22. Dynamic Attributes and Properties
- [ ] 23. Attribute Descriptors
- [ ] 24. Class Metaprogramming
----
## 1. The Python Data Model
Понравилось пояснение, что такое питонический объект: он должен быть пригоден для работы со стандартными средствами языка, такими как `len()`, итерирование, и т.п.

Интересная мысль по поводу "языка как фреймворка".

----
## 19. Concurrency Models in Python
Оценка: ⭐️⭐️⭐️⭐️⭐️

Даны хорошие определения всем основным понятиями и терминам по теме (стр. 697).

В десяти пунктах коротко описано, как применяются перечисленные концепции к программированию на Python (стр. 699).

Классный раздел от том, почему GIL не такая уж проблема для Python.

Шикарный список для дальнейшего чтения в конце главы.

Прикольная цитата (p.732):
>[!note]
>The main point: all of these application servers can potentially use all CPU cores on the server by forking multiple Python processes to run traditional web apps written in good old sequential code in *Django*, *Flask*, *Pyramid*, etc. This explains why it’s been possible to earn a living as a Python web developer without ever studying the `threading`, `multiprocessing`, or `asyncio` modules: the application server handles concurrency transparently.

----
## 20. Concurrent Executors



----
📂 [[Reading]]