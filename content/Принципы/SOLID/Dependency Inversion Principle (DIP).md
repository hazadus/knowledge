🔗 [[SOLID Principles]]

----
## Dependency Inversion Principle (DIP)

In object-oriented design, the **dependency inversion principle** is a specific methodology for loosely coupled software modules. When following this principle, the conventional dependency relationships established from high-level, policy-setting modules to low-level, dependency modules are reversed, thus rendering high-level modules independent of the low-level module implementation details. The principle states:

- High-level modules should not import anything from low-level modules. Both should depend on abstractions (e.g., interfaces).
- Abstractions should not depend on details. Details (concrete implementations) should depend on abstractions.

By dictating that _both_ high-level and low-level objects must depend on the same abstraction, this design principle _inverts_ the way some people may think about object-oriented programming.

----
  
![](https://api.selcdn.ru/v1/SEL_72086/prodLMS/files/share/6_lozmsln.png)

Последний из принципов разработки классов SOLID фокусируется на зависимостях классов. Он гласит:

- Класс должен зависеть от абстракций, а не от конкретных реализаций.

Название этого принципа содержит слово «инверсия», из чего можно сделать вывод, что без следования этому принципу мы бы зависели от конкретных реализаций, а не от абстракций. Принцип велит изменить это направление: мы всегда должны зависеть от абстракций.

Существует известное задание по программированию, которое служит хорошим примером инверсии зависимостей. Оно называется `FizzBuzz` и часто используется в качестве небольшого теста на собеседовании, который помогает увидеть, сможет ли кандидат, претендующий на должность программиста, выполнить ряд требований.

Как выглядят эти требования:

- необходимо создать список чисел от 1 до n;
- числа, которые делятся на 3, следует заменить на `Fizz`; 
- числа, которые делятся на 5, следует заменить на `Buzz`; 
- числа, которые делятся на 3 и 5, следует заменить на `FizzBuzz`.

Если применить эти правила, мы получим следующий список:

`1, 2, Fizz, 4, Buzz … 13, 14, FizzBuzz, 16, 17 … `

Поскольку не все элементы списка — целые числа, получившийся список должен быть списком строк. Простая реализация может выглядеть так:

```python
class FizzBuzz:  
   def generate_list(self, limit: int) -> list:  
       fizz_buzz_list = []  
       for number in range(1, limit + 1):  
           fizz_buzz_list.append(self.generate_element(number))  
       return fizz_buzz_list  
  
   def generate_element(self, number: int) -> str:  
       if number % 3 == 0 and number % 5 == 0:  
           return 'FizzBuzz'  
       if number % 3 == 0:  
           return 'Fizz'  
       if number % 5 == 0:  
           return 'Buzz'  
       return str(number)  
  
fizzBuzz = FizzBuzz()  
list = fizzBuzz.generate_list(100)
```

Учитывая задание, это очень точная реализация требований. Читая код, мы можем распознать в нём каждое требование: правила о делимости чисел, требование, чтобы список чисел начинался с 1, и так далее. Когда код готов, интервьюер добавляет ещё одно требование: должна быть возможность добавить дополнительное правило без изменения класса `FizzBuzz`.

Пока класс `FizzBuzz` закрыт для расширения и открыт для модификации. Если числа, делимые на 7, заменить на `Whiz`, это изменение невозможно будет реализовать без фактического изменения кода класса `FizzBuzz`.

Размышляя о дизайне класса `FizzBuzz` и о том, как можно сделать его более гибким, отметим, что метод `generate_element()` содержит много деталей. Однако в рамках того же класса метод `generate_list()` довольно универсален — он просто генерирует список увеличивающихся чисел, начиная с 1 (что несколько специфично) и заканчивая данным числом.

Таким образом, у класса `FizzBuzz` есть две ответственности: он генерирует списки чисел и заменяет определённые числа чем-то другим, основываясь на правилах `FizzBuzz`. Эти правила `FizzBuzz` подлежат изменению. И требование заключается в том, что при изменении правил нам не нужно изменять сам класс `FizzBuzz`.

Применим то, что мы узнали о принципах SOLID ранее, в частности принцип открытости/закрытости. Для начала мы можем поместить правила в их собственные классы и использовать их в методе `generate_element()`.

```python
class FizzBuzz:  
  
   def generate_list(self, limit: int) -> list:  
       fizz_buzz_list = []  
       for number in range(1, limit + 1):  
           fizz_buzz_list.append(self.generate_element(number))  
       return fizz_buzz_list  
  
   def generate_element(self, number: int) -> str:  
       fizz_buzz_rule = FizzBuzzRule()  
       if fizz_buzz_rule.matches(number):  
           return fizz_buzz_rule.get_replacement()  
  
       fizz_rule = FizzRule()  
       if fizz_rule.matches(number):  
           return fizz_rule.get_replacement()  
  
       buzz_rule = BuzzRule()  
       if buzz_rule.matches(number):  
           return buzz_rule.get_replacement()  
  
       return str(number)
```

Подробности о правилах можно найти в конкретных классах правил. Ниже — пример правила `Fizz`, реализованного в классе `FizzRule`.

```python
class FizzRule:  
   def matches(self, number) -> bool:  
       return number % 3 == 0  
  
   def get_replacement(self) -> str:  
       return 'Fizz'
```

Это один из шагов в правильном направлении. Несмотря на то что сведения о правилах (числа, которые делятся на 3, 5, 3 и 5 и их замещающие значения) были перенесены в конкретные классы правил, код в методе `generate_element()` остаётся специфичным. Правила по-прежнему представлены специфическими именами классов, и добавление нового правила потребует модификации метода `generate_element()`, поэтому мы ещё не сделали класс открытым для расширения.

Можно убрать эту специфичность из класса `FizzBuzz`, используя интерфейс для классов правил и допуская внедрение нескольких правил в экземпляр `FizzBuzz`, а также создав интерфейс для реализации новых правил.

```python
from abc import ABC, abstractmethod  
  
  
class RuleInterface(ABC):  
   @abstractmethod  
   def matches(self, number) -> bool:  
       pass  
  
   @abstractmethod  
   def get_replacement(self) -> str:  
       pass  
  
class FizzBuzzRule(RuleInterface):  
   def matches(self, number) -> bool:  
       return number % 3 == 0 and number % 5 == 0  
  
   def get_replacement(self) -> str:  
       return 'FizzBuzz'  
  
  
class BuzzRule(RuleInterface):  
   def matches(self, number) -> bool:  
       return number % 5 == 0  
  
   def get_replacement(self) -> str:  
       return 'Buzz'  
  
  
class FizzRule(RuleInterface):  
   def matches(self, number) -> bool:  
       return number % 3 == 0  
  
   def get_replacement(self) -> str:  
       return 'Fizz'  
  
  
class FizzBuzz:  
   def __init__(self):  
       self.rules = []  
  
   def addRule(self, rule: RuleInterface) -> None:  
       self.rules.append(rule)  
  
   def generate_list(self, limit: int) -> list:  
       fizz_buzz_list = []  
       for number in range(1, limit + 1):  
           fizz_buzz_list.append(self.generate_element(number))  
       return fizz_buzz_list  
  
   def generate_element(self, number: int) -> str:  
       for rule in self.rules:  
           if rule.matches(number):  
               return rule.get_replacement()  
       return str(number)  
  
  
fizzBuzz = FizzBuzz()  
fizzBuzz.addRule(FizzBuzzRule())  
fizzBuzz.addRule(FizzRule())  
fizzBuzz.addRule(BuzzRule())  
  
lst = fizzBuzz.generate_list(100)
```

Глядя на первоначальную реализацию класса `FizzBuzz`, становится ясно, что у класса с самого начала была абстрактная задача — создать список чисел. Только правила были очень подробными (число должно делиться на 3, на 5 и так далее). Говоря словами из принципа инверсии зависимостей: абстракция зависит от конкретных вещей. Это привело к закрытию класса `FizzBuzz` для расширения, поскольку добавить другое правило без изменения класса было невозможно.

Введя класс `RuleInterface` и добавив конкретные классы правил, которые реализовали этот интерфейс, мы исправили направление зависимости. Класс `FizzBuzz` начал зависеть от более абстрактных вещей, называемых правилами. При создании нового экземпляра `FizzBuzz` конкретные реализации класса `RuleInterface` должны внедряться в правильном порядке. Это приведёт к корректному выполнению алгоритма `FizzBuzz`. Сам класс `FizzBuzz` больше не заботится об этом, поэтому он становится более гибким относительно меняющихся требований. Именно так и должно быть в соответствии с принципом инверсии зависимостей:

- Абстракции не должны зависеть от деталей. Детали должны зависеть от абстракций.

Применение принципа инверсии зависимостей в коде облегчит пользователям замену определённых частей кода другими частями, адаптированными к конкретной ситуации. В то же время код остаётся общим и абстрактным, и поэтому его можно будет использовать повторно.

Следуя принципам SOLID, некоторые забывают об альтернативных стандартах написания кода. Не нужно впадать в крайности — необходимо соблюдать баланс и помнить о других важных принципах разработки, таких как [[DRY]] и [[KISS]]. Эти принципы тесно связаны с принципами SOLID и в некотором роде предостерегают разработчика от тех самых крайностей.

----
### Related
- [[Dependency Injection]]
### References
- [[The Dependency Inversion Principle. Robert Martin.pdf]]
- [Dependency inversion principle](https://en.wikipedia.org/wiki/Dependency_inversion_principle) on Wikipedia
- [[Learning Go (Bodner)]], Chapter 7, *Implicit Interfaces Make Dependency Injection Easier*.



----
📂 [[SOLID]]