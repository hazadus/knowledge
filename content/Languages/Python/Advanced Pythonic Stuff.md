### Python Source Code

> [!info] Your Guide to the CPython Source Code - Real Python  
> Are there certain parts of Python that just seem magic?  
> [https://realpython.com/cpython-source-code-guide/](https://realpython.com/cpython-source-code-guide/)  
### Async / Await / asyncio

> [!info] Async IO in Python: A Complete Walkthrough - Real Python  
> Here's what you'll cover: You'll need Python 3.  
> [https://realpython.com/async-io-python/](https://realpython.com/async-io-python/)  

> [!info] Speeding Up Python with Concurrency, Parallelism, and asyncio  
> There are many reasons your applications can be slow.  
> [https://testdriven.io/blog/concurrency-parallelism-asyncio/](https://testdriven.io/blog/concurrency-parallelism-asyncio/)  

> [!info] Асинхронность в Python  
> Asyncio - Python библиотека, которая отвечает за асинхронную работу.  
> [https://botfather.dev/blog/async-in-python](https://botfather.dev/blog/async-in-python)  

> [!info] Мини-урок по AsyncIO  
> Для того, чтобы лучше понять асинхронную работу в Python, я подготовил это видео.  
> [https://www.youtube.com/watch?v=5BVdOs3nVKk](https://www.youtube.com/watch?v=5BVdOs3nVKk)  
```Python
import asyncio

async def count(counter):
    print(f"Количество записей в списке {len(counter)}")
    while True:
        await asyncio.sleep(1 / 1000)
        counter.append(1)

async def print_every_sec(counter):
    while True:
        await asyncio.sleep(1)
        print(f'- 1 секунда прошла. '
              f'Количество записей в списке: {len(counter)}')

async def print_every_5_sec():
    while True:
        await asyncio.sleep(5)
        print(f'---- 5 секунд прошло')

async def print_every_10_sec():
    while True:
        await asyncio.sleep(10)
        print(f'---------- 10 секунд прошло')

async def main():
    counter = list()
    tasks = [
        count(counter),
        print_every_sec(counter),
        print_every_5_sec(),
        print_every_10_sec()
    ]
    await asyncio.gather(*tasks)

asyncio.run(main())
```
### Threads / Parallelism

> [!info] Speeding Up Python with Concurrency, Parallelism, and asyncio  
> There are many reasons your applications can be slow.  
> [https://testdriven.io/blog/concurrency-parallelism-asyncio/](https://testdriven.io/blog/concurrency-parallelism-asyncio/)  

> [!info] Speed Up Your Python Program With Concurrency - Real Python  
> Watch Now This tutorial has a related video course created by the Real Python team.  
> [https://realpython.com/python-concurrency/#how-to-speed-up-an-io-bound-program](https://realpython.com/python-concurrency/#how-to-speed-up-an-io-bound-program)  
### WSGI

> [!info] Building Your Own Python Web Framework - WSGI  
> Home Building Your Own Python Web Framework Part 1 WSGI Part 1, Chapter 2 Before we dive into the details of WSGI, let's look at what happens when a user uses a web application from a bird-eye's view.  
> [https://testdriven.io/courses/python-web-framework/wsgi/#H-5-middleware](https://testdriven.io/courses/python-web-framework/wsgi/#H-5-middleware)

----
📂 [[Python]] | Последнее изменение: 07.02.2024 15:09