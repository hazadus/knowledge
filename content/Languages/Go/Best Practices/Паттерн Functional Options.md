**Источник**: [пост в Телеграм-канале](https://t.me/ntuzov/461)
См. также [[Функции#Конструктор с опциями (funcopts)]]

----
Этот подход также порой может называться Option Pattern, OptFunc, Config Fucation, funcopts и т.п., зависит от фантазии ваших коллег.

Да, как мы знаем, опциональные аргументы Go не поддерживает, но можно делать так:

```go
func SendNotification(userID string, msg string, opts ...OptionFunc)
```

Вместо добавления множества параметров, мы передаем один или несколько опциональных параметров (опций), в виде variadic-аргументов — opts.

Ниже мы ещё разберёмся как это работает, но давайте сначала посмотрим как этим пользоваться. Теперь вызовы будут выглядеть таким образом:

```go
// С отправкой СМС, но без Email и без указания приоритета
SendNotification(userID, myMessage, WithSMS())

// С отправкой Email и с указанным приоритетом6
SendNotification(userID, myMessage, WithEmail(), WithPriority(HighPriority))

// И без всего этого:
SendNotification(userID, myMessage)
```

**Что нам это даёт:**

- Не надо рефакторить уже имеющиеся вызовы, они останутся без изменений
- Вызовы функций менее громоздкие, когда весь набор опций требуется очень редко, либо никогда
- Этот подход популярный и узнаваемый, а значит ваш опытный коллега сразу поймёт суть, лишь окинув ваш код быстрым взглядом.
- Моё субъективное мнение — это удобно, красиво и интуитивно понятно. Но тут вы можете со мной не согласиться, это нормально
- Параметры становятся будто бы именованными, сравните: 
	```go
	(true, false, "high", "important", ...)
	```
	и
	```go
	(WithSMS(), WithEmail(), WithPriority("high"), WithTitle("important"), ...)
	```

В первом случае вы можете лишь догадываться, какой параметр что означает, во втором сразу видите что есть что

Но есть и минусы — нужно написать чуть больше кода, и когда таких With() становится много, выглядит это даже более громоздко, чем раньше. То есть, если в большинстве вызовов вам приходится передавать много подобных опций, то, скорее всего, это не ваш вариант.

Если вам это не подходит, есть и другие варианты, например: 

- Передавать вместо набора параметров одну структуру (такой подход используется в aws-sdk-go)
- Использовать отдельные функции для разных типов вызовов и др.

**Реализация**

Сначала описываем тип OptionFunc и несколько функций, которые задают определенные параметры:

```go
type OptionFunc func(*Notification)  
  
func WithEmail() OptionFunc {  
    return func(n *Notification) {  
       n.SendEmail = true  
    }  
}  
  
func WithSMS() OptionFunc {  
    return func(n *Notification) {  
       n.SendSMS = true  
    }  
}  
  
func WithPriority(priority string) OptionFunc {  
    return func(n *Notification) {  
       n.Priority = priority  
    }  
}
```

Теперь учим нашу функцию `SendNotification()` применять всё это:

```go
func SendNotification(userID string, msg string, opts ...OptionFunc) {
  // Создаем уведомление с базовыми параметрами
  notification := &Notification{
    UserID:  userID,
    Message: message,
  }

  // Применяем опции
  for _, opt := range opts {
    opt(notification)
  }

  // Отправляем уведомление
  send(notification)
}
```

Я встречал этот паттерн во всех компаниях, в которых писал код на Go, и мне он очень хорошо зашел. И даже если он вам не нравится, сталкиваться вы с ним будете часто, поэтому понимать что это и зачем точно стоит.

## Полный код примера

```go
package main

import (
  "fmt"
)

type Notification struct {
  UserID    string
  Message   string
  SendEmail bool
  SendSMS   bool
  Priority  string
}

type OptionFunc func(*Notification)

func WithEmail() OptionFunc {
  return func(n *Notification) {
    n.SendEmail = true
  }
}

func WithSMS() OptionFunc {
  return func(n *Notification) {
    n.SendSMS = true
  }
}

func WithPriority(priority string) OptionFunc {
  return func(n *Notification) {
    n.Priority = priority
  }
}

func SendNotification(userID string, msg string, opts ...OptionFunc) {
  // Создаем уведомление с базовыми параметрами
  notification := &Notification{
    UserID:  userID,
    Message: msg,
  }

  // Применяем опции
  for _, opt := range opts {
    opt(notification)
  }

  // Демонстрация логики отправки уведомления
  printNotification(notification)
}

func printNotification(notification *Notification) {
  fmt.Printf("Sending notification to user: %s\n", notification.UserID)
  fmt.Printf("Message: %s\n", notification.Message)

  if notification.SendEmail {
    fmt.Println("Sending Email...")
  }
  if notification.SendSMS {
    fmt.Println("Sending SMS...")
  }
  if notification.Priority != "" {
    fmt.Printf("Priority: %s\n", notification.Priority)
  }

  fmt.Println("Notification sent successfully!")
  fmt.Println("--------")
}

func main() {
  // Вызов без дополнительных опций
  SendNotification("user123", "Hello, world!")

  // Вызов с отправкой Email
  SendNotification("user456", "Important update!", WithEmail())

  // Вызов с отправкой SMS и высоким приоритетом
  SendNotification("user789", "Urgent update!", WithSMS(), WithPriority("high"))
}
```

----
📂 [[Best Practices]] | Последнее изменение: 27.11.2024 14:34