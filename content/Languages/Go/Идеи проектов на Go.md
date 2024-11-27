## Справочные материалы

- [10 Project Ideas To Learn Golang In 2024](https://golang.withcodeexample.com/blog/golang-project-ideas/)
- 5 projects to learn Go https://youtu.be/gXmznGEW9vo
- [Rest API сервис на Go (Тузов)](https://youtu.be/rCJvW2xgnk0?si=hyIpCgBV-2mnqe_v) (скачано)
- [Сервис авторизации на Go (Тузов)](https://youtu.be/EURjTg5fw-E?si=XOf8p3zJj6L95l78) (скачано)
- [BugBytes Go Programming Playlist](https://www.youtube.com/playlist?list=PL-2EBeDYMIbR1ag15E2MonJOj_cCIjUnd)

----
## Приложения Go
### ✅ Менеджер паролей

CLI tool для удобного хранения и использования паролей.

**Фичи проекта**

- ✅ Хранение списка в файле в формате JSON.
- ✅ Настройка файла для хранения списка через env var.
- ✅ Тесты CLI.
- Флаги команды:
	- ✅ `-add <service> -pwd <password>`: добавить запись `service` с паролем `password`.
	- ✅ `-get <service>`: получить пароль от записи `service`.
	- ✅ `-delete <service>`: удалить запись `service` из списка.
	- ✅ `-list`: вывести перечень названий сервисов в списке.
      - ✅ `-v`: используется совместно с `-list` и выводить более подробную информацию.
- ✅ Шифровать файл с паролями.

#### References

- Моя реализация: [go-lockbox](https://github.com/hazadus/go-lockbox)
- [Encrypt a File using Go](https://medium.com/@mertkimyonsen/encrypt-a-file-using-go-f1fe3bc7c635)

----
### Поиск "битых" ссылок на сайте

Пригодится для своих сайтов. См. 5 projects to learn #Go https://youtu.be/gXmznGEW9vo.
Web Scraping tutorial https://youtu.be/NU4OlJVj1gs?si=CYnHox_NKWI-kmk0

----
### Shell

Простейшая оболочка командной строки. См. *The Power of Go – Tools* для референса.

----
### REST API с JWT Auth

- См. книгу *Let's Go Further*.
- [[Implementing JWT Authentication in Golang REST API - Detailed Guide - codewithmukesh]]

----
### Key-Value Storage

См. [[Matthew A. Titmus - Cloud Native Go_ Building Reliable Services in Unreliable Environments-O'Reilly Media (2021).pdf]].

----
### Помидор-таймер

См. 📖 *Powerful Command-Line Applications in Go*.

----
### File Browser

Простейший аналог Norton Commander.

----
### Трекер времени

Идея проекта `trackr`: упрощенный аналог Toggl Track для учёта затрат времени.

- Интерфейс, как у помидора из книги. Экраны:
	- основной: таймер, сегодняшние отрезки, статистика за день
	- "отчеты": статистика за неделю; фильтры по проектам, по клиентам, по тегам.
	- "проекты": список проектов; редактировать инфо о проектах
	- "клиенты": список клиентов; редактировать инфо о клиентах
- данные в sqlite3
- клиенты, проекты, задачи (с комментариями), теги к задаче
- из командной строки дублировать основные действия, например:
	- добавлять а ля `-add 15` (дело последние 15 минут с завершением сейчас) 
	- отчеты в файл, например в формате md, html

----
### Building a Chat Application with WebSockets

See [10 Project Ideas To Learn Golang In 2024](https://golang.withcodeexample.com/blog/golang-project-ideas/)

### Image Processing and Computer Vision with Golang

See [10 Project Ideas To Learn Golang In 2024](https://golang.withcodeexample.com/blog/golang-project-ideas/)

----
### gRPC Server / Client

- [Introduction to gRPC in Go](https://mail.google.com/mail/u/0/#inbox/WhctKLbMzLTkLCTTfSNbLlJtQvQLLWfxjnnchQwPQFZVLZcxGFrhMkCMPwGjWQsZhMtkqXQ) (рассылка от Jon Calhoun)
- Видео *gRPC сервис (Тузов)* (скачано)
- См. книгу *gRPC: запуск и эксплуатация облачных приложений* (скачана).

---
### SSE

Попробовать реализовать [[How to Implement Server-Sent Events in Go]].

----
### Simple Redis Server From Scratch In Golang

См. скачанное видео.

----
### Distributed File Storage In Go

См. скачанное видео.

---
## Video Streaming

...



----
📂 [[Go]] | Последнее изменение: 22.11.2024 15:20