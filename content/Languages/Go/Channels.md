Для обмена данными между [[Goroutines|горутинами]] используются **каналы**.

## Создание каналов, передача значений

В примере ниже показан порядок создания канала, записи данных в него и чтения данных из него:

```go
func main() {
    // To create a channel, use `make(chan type)`.
    // Channel can only accept values of the specified type:
    messages := make(chan string)

    // To send a value to a channel,
    // use the `channel <-` syntax.
    // Let's send "ping":
    go func() { messages <- "ping" }()

    // To receive a value from a channel,
    // use the `<-channel` syntax.
    // Let's receive "ping" and print it:
    msg := <-messages
    fmt.Println(msg)
}
```

Отправка значения через канал является синхронной операцией. `messages <- "ping"` блокирует выполнение, пока где-то не будет получено значение при помощи `<-messages`. Таким образом, каналы позволяют не только обмениваться данными между горутинами, но и синхронизировать их работу.

```go
func main() {
    messages := make(chan string)

    go func() {
        fmt.Println("B: Sending message...")
        messages <- "ping"                    // (1)
        fmt.Println("B: Message sent!")       // (2)
    }()

    fmt.Println("A: Doing some work...")
    time.Sleep(500 * time.Millisecond)
    fmt.Println("A: Ready to receive a message...")

    <-messages                               //  (3)

    fmt.Println("A: Messege received!")
    time.Sleep(100 * time.Millisecond)
}
```

After sending the message to the channel ➊, goroutine B gets blocked. Only when goroutine A receives the message ➌ does goroutine B continue and print "message sent" ➋.

## Закрытие каналов

The writer can _close_ the channel. The reader can detect that the channel is closed.

The writer closes the channel using the `close()` function:

```go
str := "one,two,,four"
in := make(chan string)

go func() {
    words := strings.Split(str, ",")
    for _, word := range words {
        in <- word
    }
    close(in)
}()
```

The reader checks the channel's status with a second value ("comma OK") when reading:

```go
for {
    word, ok := <-in
    if !ok {
        break
    }
    if word != "" {
        fmt.Printf("%s ", word)
    }
}
```

While the channel is open, the reader receives the next value and a `true` status. If the channel is closed, the reader gets a zero value ("" for strings) and a `false` status.

You can read from a closed channel as much as you want — it always returns a zero value and a `false` status.

A channel can only be closed once. Closing it again will cause a panic. You also can't write to a closed channel.

Here are two important rules:

1. _Only the writer can close the channel, not the reader_. If the reader closes it, the writer will encounter a panic on the next write.
2. _A writer can only close the channel if they are the sole owner_. If there are multiple writers and one closes the channel, the others will face a panic on their next write or attempt to close the channel.

> [!NOTE] **Should I always close a channel?**
> If you've ever worked with external resources (such as files or database connections), you know they should always be closed to prevent leaks. But a channel isn't an external resource. When a channel is no longer used, Go's garbage collector will free its resources, whether it's closed or not.
> 
>  The only reason to close a channel is to signal to its readers that all data has been sent. If this isn't important to the readers, then you don't need to close it.

## Итерация по каналу

`range` automatically reads the next value from the channel and checks if it's closed. If the channel is closed, it exits the loop. Note that range over a channel returns a single value, not a pair, unlike range over a slice.

```go
word := make(chan string)
go func() {
    word <- "uno"
    word <- "dos"
    word <- "tres"
    close(word)
}()

for val := range word {
    fmt.Println(val)
}
```

## Направленные каналы

Для исключения ошибок, можно указывать направления работы каналов:

- `chan` (bidirectional): for reading and writing (default);
- `chan<-` (send-only): for writing only;
- `<-chan` (receive-only): for reading only.

The `submit()` function needs a send-only channel:

```go
func submit(str string, stream chan<- string) {  // (1)
    words := strings.Split(str, ",")
    for _, word := range words {
        stream <- word
    }
    // <-stream                                  // (2)
    close(stream)
}
```

In the function signature ➊, we've specified that it's send-only, so you can't read from it. Uncomment line ➋, and you'll get a compile error.

The `print()` function needs a receive-only channel:

```go
func print(stream <-chan string) {  // (1)
    for word := range stream {
        if word != "" {
            fmt.Printf("%s ", word)
        }
    }
    // stream <- "oops"             // (2)
    // close(stream)                // (3)
    fmt.Println()
}
```

In the function signature ➊, we've specified that it's receive-only. You can't write to it. Uncomment lines ➋,➌, and you'll get a compile error.

You can set the channel direction during initialization, but it's not very helpful. So, channels are usually initialized for both reading and writing, and specified as directional in function parameters. Go automatically converts a regular channel to a directional one:

```go
stream := make(chan int)

go func(in chan<- int) {
    in <- 42
}(stream)

func(out <-chan int) {
    fmt.Println(<-out)
}(stream)
// 42
```

> [!NOTE]
> Always specify the channel direction in function parameters to avoid runtime errors.

----
## References

- https://antonz.org/go-concurrency/channels/
- [[Learning Go (Bodner)]], chapter 10 "Concurrency"
- [[Язык программирования Go (Донован, Керниган)]], глава 8.
- https://habr.com/ru/companies/beget/articles/870138/
- http://golangtutorials.blogspot.co.uk/2011/06/channels-in-go.html
- https://appliedgo.net/futures/

----
📂 [[Go]] | Последнее изменение: 02.01.2025 21:33