## Цели и задачи

**Цель по #Go**:
- сравнить его с Питоном и понять для себя, для каких задач он предпочтителен.
- получить практику разработки в тех сферах, где язык актуален (CLI tools, API).

**Для этого**:
- ✅ Пройти бесплатный курс "Основы Go" от Яндекса.
- ✅ Выписать вопросы для изучения из [[1f_vs_2f.pdf|плана курсов Яндекса]] *(см. ниже)*.
- Параллельно:
	- Делать REST API [[go-anvlink]] и изучать необходимое для этого.
		- ✅ Проработать *Let's Go Further* by Alex Edwards.
		- Проработать *Let's Go* by Alex Edwards.
		- Проработать 📖 *Shipping Go*.
	- Дочитать 📖 [[Learning Go (Bodner)]] (Гл. 7-14, стр. 129-324).
	- Проработать [Learn Go with Tests](https://quii.gitbook.io/learn-go-with-tests) (онлайн-учебник)
- Проработать оставшиеся главы из 📖 *Powerful Command-Line Applications in Go*.
	- со стр.110 *расписать, что сделано, и что осталось*
- Доработать 🔑 **go-lockbox** до конца – [Issues](https://github.com/hazadus/go-lockbox/issues).
- gRPC
	- [Introduction to gRPC in Go](https://mail.google.com/mail/u/0/#inbox/WhctKLbMzLTkLCTTfSNbLlJtQvQLLWfxjnnchQwPQFZVLZcxGFrhMkCMPwGjWQsZhMtkqXQ) (рассылка от Jon Calhoun)
	- Видео *gRPC сервис (Тузов)* (скачано)
	- См. книгу *gRPC: запуск и эксплуатация облачных приложений* (скачана).
- Видео туториалы по разработке мини-проектов (скачаны):
	- *gRPC сервис (Тузов)*
	- *Simple Redis Server From Scratch In Golang*
	- *Distributed File Storage In Go*
- Реализовать [[Идеи проектов на Go]].
- Проверить по [[1f_vs_2f.pdf|плану курсов Яндекса]], какие вопросы осталось проработать.

----
## 📚 Книги

### 📖 Обязательно читать

- 📖 *Let's Go*
- ✅ *Let's Go Further*
- 📖 *Powerful Command-Line Applications in Go* – подробное описание процесса создания интересных мини-проектов.
- *Shipping Go* – настройка процесса CI/CD с примерами для проектов на Go.
- John Arundel – *The Power of Go – Tools* – практика написания простых CLI-tool, пример простойшей shell.
- *100 Go Mistakes and How to Avoid Them* – есть также в виде сайта.

### Претенденты

- **Рассмотреть**: *gRPC: запуск и эксплуатация облачных приложений* – скачана. Тема важная.
- **Рассмотреть**: *Go Cookbook* – скачана. Сборник рецептов, может быть что-то полезное.
- John Arundel – *Know Go Generics* – скачана. С дженериками нужно разобраться.
- John Arundel – *The Power of Go Tests* – найти, если нужны будут дополнительные книги по тестам.
- **Рассмотреть**: Simion A. - *Test-Driven Development in Go* - 2023 – про тесты, тема важная. Должно быть интересно!
- [[Matthew A. Titmus - Cloud Native Go_ Building Reliable Services in Unreliable Environments-O'Reilly Media (2021).pdf]]: рассматривает особенности и принципы разработки "под облако". Любопытный пример проекта key-value storage.
- [[Katherine Cox-Buday - Concurrency in Go_ Tools and Techniques for Developers-O’Reilly Media (2017).pdf]]: рекомендует Боднер в конце главы 10. Компактная книга (230 стр.).
- *Learn Concurrent Programming with Go* (James Cutajar, Manning) – тема интересная, книга свежая. Просмотрел: рассматриваются разные аспекты конкуррентности. Минусы – не увидел интересных примеров, всё какие-то очень схематичные.
- *Writing an Interpreter in Go* – тематика кайфовая, книга серьёзная. Пролистать!
- *Distributed_Services_with_Go* – случайно попалась, выглядит интересно, пролистать!

----
## Темы для изучения из большого курса Яндекса

- ✅ `net/http`
- ✅ `flag`
- ✅ Пакет `os`. Работа с переменными окружения.
- Пакет `log`
	- Стандартные и сторонние пакеты для логирования
	- Логирование через middleware
- Пакет `encoding`. Сериализация и десериализация данных
	- Структурные теги
	- Стандартные сериализаторы
	- Сторонние сериализаторы
- Пакет `compress`. Сжатие данных
	- Код умеет сжимать данные ответа с помощью `gzip`
- Пакет `os`. Чтение и запись в файл
- Пакет `time`
	- Время: даты, интервалы, таймеры
- Пакет `context`. Отмена операций и управление временем выполнения
	- Контекст: отмена операций
- ✅ Пакет `database/sql`. Взаимодействие с SQL БД
	- Пакет `gomock`: имитация БД
	- Абстрактный интерфейс и SQL-драйверы
	- Запросы к БД
	- Запись в БД
- Пакет `errors`. Обработка ошибок
	- Интроспекция ошибок (код умеет определять типы ошибок)
- Пакеты `hash`, `crypto`. Безопасность информации
	- Хеширование и шифрование
	- Авторизация: JSON Web Token
- Многопоточность в Go
	- Каналы
	- Паттерны многопоточности
- Паттерны проектирования на Go
	- Порождающие паттерны
	- Структурные паттерны
	- Поведенческие паттерны
- Антипаттерны программирования на Go
	- Постулаты Go
	- Лучшие практики, антипаттерны
- Тулинг
	- Бенчмарки
	- Инструмент `pprof`
	- Форматирование с `go fmt`, `goimports`
	- `godoc`, Swagger
- Статический анализ кода
	- Команда `go vet`
	- Пакет `go/ast`
	- Пакет `x/analysis`
	- Пакет `staticcheck`
- Дженерики и кодогенерация
	- Кодогенерация
	- Дженерики
- Флаги сборки и компиляции
	- Build constraints
	- ✅ Код добавляет версию и другие метаданные при компиляции
- Расширенная стандартная библиотека
	- Расширенная стандартная библиотека (golang.org/x)
	- Генерация случайных чисел
		- Пакеты `math/rand`, `crypto/rand`
	- Чтение данных и буфер
		- Пакет `bytes`
		- Пакет `bufio`
	- Пакет `os`. Работа с директориями и процессами
		- ✅ Код умеет работать с файлами конфигов
	- Вызов внешних приложений, сигналы
		- ✅ Код умеет реагировать на сигналы ОС
	- Примитивы синхронизации
		- Пакеты `sync` и `x/sync`
	- Работа с сетью
		- Пакет `net`. Работа с TCP, UDP
		- IP-адреса
	- Protocol buffers и gRPC
		- Разработка gRPC клиента (агента?) и сервера

----
📂 [[Go]] | Последнее изменение: 16.10.2024 08:58