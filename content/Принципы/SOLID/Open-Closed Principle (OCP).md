🔗 [[SOLID Principles]]

----
## OCP — Open/Closed Principle

![](https://api.selcdn.ru/v1/SEL_72086/prodLMS/files/share/3_LsLQ3Kk.png)

Принцип открытости/закрытости гласит:

- Вы должны иметь возможность расширять поведение класса, не изменяя его.

Единица кода считается открытой для расширения, если её поведение можно легко изменить, не изменяя сам код. Тот факт, что для изменения поведения единицы кода не требуется никакой реальной модификации, делает её закрытой для модификации.

Возможность расширять поведение класса не означает, что вы действительно должны расширить этот класс, создав для него подкласс. Расширение класса означает, что вы можете влиять на его поведение извне, не касаясь класса или иерархии классов.

Рассмотрим класс `GenericEncoder`. Обратите внимание на ветвление внутри метода `encode_to_format()`, которое необходимо для выбора правильного кодировщика на основе значения аргумента format.

```python
class GenericEncoder:  
   def encode_to_format(self, data: Any, format: str) -> str:  
       if format == 'json':  
           encoder = JsonEncoder()  
       elif format == 'xml':  
           encoder = XmlEncoder()  
       else:  
           raise ValueError('Unknown format')  
  
       data = self.prepare_data(data, format)  
       return encoder.encode(data)  
  
   def prepare_data(self, data: Any, format: str) -> Any:  
       # Implement your logic to prepare the data for encoding based on the format  
       # This method can be overridden in derived classes if needed  
       return data
```

Допустим, вы хотите использовать класс `GenericEncoder` для кодирования данных в формате YAML, который в настоящее время не поддерживается кодировщиком. Очевидное решение — создать для этой цели класс `YamlEncoder`, а затем добавить в существующий метод `encode_to_format()` дополнительное условие по аналогии с JSON и XML.

```python
class GenericEncoder:  
   def encode_to_format(self, data: Any, format: str) -> str:  
       if format == 'json':  
           encoder = JsonEncoder()  
       elif format == 'xml':  
           encoder = XmlEncoder()  
       elif format == 'yaml':  
           encoder = YamlEncoder()  
       else:  
       #...
```

Каждый раз, когда вы хотите добавить ещё один кодировщик для конкретного формата, необходимо менять сам класс `GenericEncoder`: нельзя изменить его поведение, не изменив код. Вот почему этот класс нельзя рассматривать как открытый для расширения и закрытый для модификации.

Посмотрим на метод `prepare_data()` из того же класса. Как и метод `encode_to_format()`, он содержит более специфичную для формата логику.

```python
class GenericEncoder:  
  def encode_to_format(self, data: Any, format: str) -> str:  
     # ...  
     data = self.prepare_data(data, format)  
     # ...  
  
  def prepare_data(self, data: Any, format: str) -> Any:  
     if format == 'json':  
         # some operations with data  
         data = ...  
     elif format == 'xml':  
         # some operations with data  
         data = ...  
     else:  
         raise ValueError('Format not supported')  
     return data
```

Метод `prepare_data()` — ещё один хороший пример закрытого для расширения кода, поскольку добавить поддержку другого формата без изменения самого кода невозможно. Если вам придётся изменить этот код, например при вводе нового формата, вполне вероятно, что вы либо продублируете код, либо просто сделаете ошибку, потому что пропустите условие `elif`.

### Классы, нарушающие принцип открытости/закрытости

Характеристики класса, который не может быть открыт для расширения:

- условия, использующие одни и те же переменные или константы, повторяются внутри класса или связанных классов;
- класс содержит жёстко запрограммированные ссылки на другие классы или имена классов;
- у класса есть защищённые свойства или методы, позволяющие изменять его поведение путём переопределения состояния или поведения.

Хотелось бы исправить этот неудачный дизайн, который требует от нас постоянного погружения в класс `GenericEncoder` для изменения поведения, ориентированного на формат.

Сначала мы должны делегировать ответственность за выбор правильного кодировщика формата другому классу. Когда вы рассматриваете ответственности как причины для изменения (вспомним предыдущий принцип), это имеет смысл: логика поиска правильного кодировщика может измениться, поэтому неплохо было бы перенести эту ответственность в другой класс.

Новый класс также может быть реализацией шаблона проектирования «Абстрактная фабрика». Абстрактность означает, что метод `create()` обязан возвращать экземпляр данного интерфейса. Нас не интересует его фактический класс, мы только хотим получить объект с помощью метода `encode(data)`, поэтому нам нужен интерфейс для таких кодировщиков. Затем мы удостоверимся, что каждый существующий кодировщик, ориентированный на конкретный формат, реализует этот интерфейс.

```python
from abc import ABC  
  
class EncoderInterface(ABC):  
   ...  
  
class JsonEncoder(EncoderInterface):  
   ...  
  
class XmlEncoder(EncoderInterface):  
   ...  
  
class YamlEncoder(EncoderInterface):  
   ...
```

Теперь можно переместить логику создания кодировщиков, ориентированных на конкретный формат, в класс именно с этой ответственностью. Назовём его `EncoderFactory`.

```python
class EncoderFactory:  
   def create_for_format(self, format: str) -> Any:  
       if format == 'json':  
           return JsonEncoder()  
       elif format == 'xml':  
           return XmlEncoder()  
       elif ...:  
       # ...  
       raise ValueError('Unknown format')
```

Теперь мы должны убедиться, что класс `GenericEncoder` больше не создаёт кодировщики, ориентированные на конкретный формат. Вместо этого он должен делегировать такую задачу классу `EncoderFactory`, который класс `GenericEncoder` получает в качестве аргумента конструктора.

```python
class GenericEncoder:  
   def __init__(self, encoderFactory: EncoderFactory):  
       self.encoderFactory = encoderFactory  
  
   def encode_to_format(self, data: Any, format: str) -> str:  
       encoder = self.encoderFactory.create_for_format(format)  
       data = self.prepare_data(data, format)  
       return encoder.encode(data)  
  
   def prepare_data(self, data: Any, format: str) -> Any:  
       # Implement your logic to prepare the data for encoding based on the format  
       # This method can be overridden in derived classes if needed  
       return data
```

Оставляя ответственность за создание правильного кодировщика `encoderFactory`, `GenericEncoder` теперь соответствует принципу единственной ответственности. Использование фабрики кодировщиков для получения правильного кодировщика заданного формата означает, что добавление дополнительного кодировщика больше не требует изменения класса `GenericEncoder`. Вместо этого нужно изменить класс `EncoderFactory`. Но в классе `EncoderFactory` всё ещё находится жёстко закодированный список поддерживаемых форматов и соответствующих кодировщиков. Что ещё хуже, имена классов по-прежнему также жёстко закодированы. Это означает, что теперь `EncoderFactory` закрыт для расширения. То есть его поведение нельзя расширить без изменения кода, а значит, класс нарушает принцип открытости/закрытости.

Первое, что можно сделать, — применить принцип инверсии зависимостей (об этом вы узнаете позже), определив интерфейс для фабрик кодировщиков. Класс `EncoderFactory`, который у нас уже есть, должен реализовывать новый интерфейс, а аргумент конструктора `GenericEncoder` — иметь интерфейс в качестве своего типа.

```python
from abc import abstractmethod, ABC  
  
class EncoderFactoryInterface(ABC):  
   @abstractmethod  
   def create_for_format(self, format: str) -> Any:  
       pass  
  
class EncoderFactory(EncoderFactoryInterface):  
   def create_for_format(self, format: str) -> Any:  
       # ...  
  
class GenericEncoder:  
   def __init__(self, encoderFactory: EncoderFactoryInterface):  
       # ...
```

Сделав класс `GenericEncoder` зависимым от интерфейса, а не от другого класса, мы добавили к нему первую точку расширения. Пользователям этого класса будет легко полностью заменить фабрику кодировщика. Теперь `encoderFactory` представляет собой правильную зависимость, которая вставляется в качестве аргумента конструктора типа `EncoderFactoryInterface`.

Внедрив интерфейс, мы предоставили пользователям ещё одну мощную опцию. Возможно, они хотят не полностью заменить существующий класс `EncoderFactory`, а только улучшить его. Предположим, пользователи желают получить кодировщик для заданного формата из локатора служб и вернуться к стандартному классу `EncoderFactory`, если формат окажется неизвестен. Используя этот интерфейс, они могут составить новую фабрику, которая реализует требуемый интерфейс и получает исходный класс `EncoderFactory` в качестве аргумента конструктора.

Хорошо, что теперь пользователи могут реализовать собственный экземпляр `EncoderFactoryInterface`. Однако принуждение пользователя к повторной реализации класса `EncoderFactoryInterface`, просто чтобы добавить поддержку другого формата, кажется несколько неэффективным. Когда появляется новый формат, мы хотим продолжать использовать старый класс `EncoderFactory`, но нам нужно поддерживать новый формат, не затрагивая код самого класса. Кроме того, если одному из кодировщиков для выполнения задачи потребуется другой объект, предоставить этот объект в качестве аргумента конструктора будет пока невозможно, поскольку логика создания каждого из кодировщиков жёстко закодирована в классе `EncoderFactory`.

Другими словами, расширить или изменить поведение класса `EncoderFactory`, не модифицируя его, невозможно: логику, с помощью которой фабрика кодировщиков решает, какой кодировщик она должна создать и как она должна это сделать для заданного формата, нельзя изменить извне. Однако вывести эту логику из класса `EncoderFactory` довольно легко, что делает его открытым для расширения.

Есть несколько способов сделать фабрику вроде `EncoderFactory` открытой для расширения. Например, можно добавить в класс `EncoderFactory` специальные фабрики.

```python
class EncoderFactory(EncoderFactoryInterface):  
   def __init__(self):  
       self.factories = {}  
  
   def add_encoder_factory(self, format: str, factory: Callable) -> None:  
       self.factories[format] = factory  
  
   def create_for_format(self, format: str) -> Any:  
       factory = self.factories[format]  
       encoder = factory()  
       return encoder
```

Для каждого формата можно ввести псевдотип `Сallable`. Метод `create_for_format() `принимает этот псевдотип, вызывает его и использует возвращаемое значение в качестве фактического кодировщика для этого формата. Такая полностью динамическая и расширяемая реализация позволяет разработчикам добавлять столько кодировщиков, сколько им захочется.

Внедрив фабрики с использованием типа `Callable`, мы освободили класс `EncoderFactory` от ответственности за предоставление правильных аргументов конструктора для каждого кодировщика. Другими словами, мы поместили знания о логике создания кодировщиков за пределами класса `EncoderFactory`, благодаря чему в ней одновременно соблюдается принцип единственной ответственности и принцип открытости/закрытости.


----
📂 [[SOLID]] | Последнее изменение: 26.04.2024 09:53