🔗 [[SOLID Principles]]

----
## ISP — Interface Segregation Principle

![](https://api.selcdn.ru/v1/SEL_72086/prodLMS/files/share/5_DoN17jD.png)

Четвёртый принцип проектирования классов в ООП — принцип разделения интерфейса. Звучит он так:

- Создавайте узкоспециализированные интерфейсы, предназначенные для конкретного клиента.

Узкоспециализированные интерфейсы — интерфейсы с небольшим количеством методов. Предназначенные для конкретного клиента — интерфейсы должны определять методы, которые имеют смысл с точки зрения клиента, использующего интерфейс.

Чтобы понять этот принцип, рассмотрим пример его нарушения.

Представим, что была задача — создать класс `Smartphone`. Мы создали для него и будущих устройств интерфейс `Device` с методами для функций смартфона, которые позволяют звонить, отправлять файл и выходить в интернет. Потом появилась задача дописать класс `Laptop`, который не умеет звонить. Здесь мы должны понять, что интерфейс `Device` противоречит ISP, и его следует разделить. Если бы мы не знали об ISP, то могли бы написать класс `Laptop` как в примере ниже. И после появления задачи дописать класс `Phone` тоже нарушили бы принцип. Получился бы следующий код:

```python
from abc import ABC, abstractmethod  
  
class Device(ABC):  
   @abstractmethod  
   def call(self):  
       pass  
  
   @abstractmethod  
   def send_file(self):  
       pass  
  
   @abstractmethod  
   def browse_internet(self):  
       pass  
  
  
class Smartphone(Device):  
   def call(self):  
       ...  
   def send_file(self):  
       ...  
   def browse_internet(self):  
       ...  
  
  
class Laptop(Device):  
   def call(self):  
       raise BadOperation("Ноутбук не может звонить.")  
  
   def send_file(self):  
       ...  
   def browse_internet(self):  
       ...  
  
class Phone(Device):  
   def call(self):  
       ...  
  
   def send_file(self):  
       raise BadOperation("Телефон не может отправлять файлы.")  
  
   def browse_internet(self):  
       raise BadOperation("Телефон не может выходить в интернет.")
```

Это чёткая иллюстрация зависимости клиентов `Laptop` и `Phone` от интерфейса `Device`, который они реализуют лишь частично.

Приятный трюк заключается в том, что при необходимости в нашей бизнес-логике отдельный класс может реализовать несколько интерфейсов. Таким образом, мы можем предоставить устройствам единую реализацию для всех общих методов между интерфейсами. В Python это легко решается множественным наследованием:

```python
from abc import ABC, abstractmethod  
  
class CallDevice(ABC):  
   @abstractmethod  
   def call(self):  
       pass  
  
class FileTransferDevice(ABC):  
   @abstractmethod  
   def send_file(self):  
       pass  
  
class InternetDevice(ABC):  
   @abstractmethod  
   def send_file(self):  
       pass  
  
class Smartphone(CallDevice, FileTransferDevice, InternetDevice):  
   def call(self):  
       ...  
  
   def send_file(self):  
       ...  
  
   def browse_internet(self):  
       ...  
  
class Laptop(FileTransferDevice, InternetDevice):  
   def send_file(self):  
       ...  
  
   def browse_internet(self):  
       ...  
  
class Phone(CallDevice):  
   def call(self):  
       ...
```

Теперь мы видим тонкие интерфейсы и избавляем программные сущности от методов, которые они не используют. Код становится более предсказуемым и менее связанным.

Сегрегированные интерфейсы заставляют нас больше думать о коде с точки зрения клиента, что приводит к меньшей зависимости и более лёгкому тестированию. Таким образом, мы не только сделали код лучше для клиента, но и облегчили его понимание, тестирование и реализацию для самих себя.


----
📂 [[SOLID]] | Последнее изменение: 26.04.2024 10:04