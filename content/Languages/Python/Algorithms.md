Search
Is Prime Number?
Factorial
Расстояние между двумя точками на плоскости
Модель круга
### Search
```Python
def sort_list(source_list):
    sorted_list = source_list[:]
    for i in range(len(sorted_list)):
        for j in range(i+1, len(sorted_list)):
            if sorted_list[j] < sorted_list[i]:
                sorted_list[j], sorted_list[i] = sorted_list[i], sorted_list[j]
    return sorted_list
```
### Is Prime Number?

> [!info] Primality test - Wikipedia  
> A primality test is an algorithm for determining whether an input number is prime.  
> [https://en.wikipedia.org/wiki/Primality_test#Python](https://en.wikipedia.org/wiki/Primality_test#Python)  
```Python
def is_prime(n: int) -> bool:
    """Primality test using 6k+-1 optimization."""
    if n <= 3:
        return n > 1
    if not n%2 or not n%3:
        return False
    i = 5
    stop = int(n**0.5)
    while i <= stop:
        if not n%i or not n%(i + 2):
            return False
        i += 6
    return True
```
```Python
def is_prime(n: int) -> bool:
    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(4, n):
        if n % i == 0:
            return False
    return True
```
### Factorial
![[attachments/Untitled 32.png|Untitled 32.png]]
![[attachments/Untitled 1 12.png|Untitled 1 12.png]]
### Расстояние между двумя точками на плоскости
![[attachments/Untitled 2 10.png|Untitled 2 10.png]]
### Модель круга
```Python
import math
from math import pi

class Circle:
    def __init__(self, x=0, y=0, r=1):
        self.x = x
        self.y = y
        self.r = r
    def area(self):
        return pi * (self.r**2)
    def perimeter(self):
        return 2*pi*self.r
    def grow(self, k):
        self.r *= k
    def intersects(self, other):
        dist = math.sqrt((self.x-other.x)**2 + (self.y-other.y)**2)
        return dist < self.r + other.r
```

----
📂 [[Python]] | Последнее изменение: 07.02.2024 14:50