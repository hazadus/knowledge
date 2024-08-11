🔖 #API #REST 

----

**REST** (Representational State Transfer) refers to a group of software architecture design constraints that bring about efficient, reliable and scalable distributed systems.

The basic idea of REST is that a resource, e.g. a document, is transferred via well-recognized, language-agnostic, and reliably standardized client/server interactions. Services are deemed RESTful when they adhere to these constraints.

HTTP APIs in general are sometimes colloquially referred to as RESTful APIs, RESTful services, or REST services, although they don't necessarily adhere to all REST constraints. Beginners can assume a REST API means an HTTP service that can be called using standard web libraries and tools.

----
## Highlights
```dataview
TABLE FROM #API and #Omnivore 
```
----
## Требования к REST-архитектуре
1. *Клиент-серверная архитектура*.
2. *Отсутствие состояния (stateless)*. Пока клиент не обращается к серверу, тот может и не подозревать о существовании клиента. Всё что нужно серверу, чтобы понять, что от него хотят, должно содержаться в запросе.
3. *Единообразие интерфейса*.
	- Идентицикация ресурсов. Каждый ресурс (файл, страница, и т.п.) должен быть обозначен постоянным идентификатором, то есть URL, по которому можно получить ресурс. Пример: `/{collection}/{document}/{collection}/{document}/`, e.g. `/countries/{countryCode}/cities/{cityCode}/`
	- Управление ресурсами через представление. Как правило, это JSON, отправляемый клиентом в том виде, в котором он хочет видеть финальный результат изменения ресурса. То есть, клиент "даёт свои предложения" серверу по результатам изменения ресурса (каким от должен быть), но весь контроль по изменению ресурса находится только у сервера.
	- Самодостаточные сообщения. В сообщении должна быть вся информация, необходимая для выполнения запрашиваемого действия над ресурсом.
	- Гипермедиа (HATEOAS).
1. *Кэширование*. Все сообщения от сервера должны быть помечены как кэшируемые, или некэшируемые.
2. *Система слоёв*. Каждый слой может взаимодействовать только с соседним.
	- Схема: ![[Pasted image 20240131190045.png]]
1. *Код по требованию*. В ответе сервера может содержаться выполняймый код. Но обычно там просто JSON.

----
📂 [[Web]]