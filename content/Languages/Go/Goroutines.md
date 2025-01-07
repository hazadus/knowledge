> [!NOTE]
> If you're familiar with concurrency in Python, JavaScript, or other languages with async/await, don't try to apply that experience to Go. Go has a very different approach to concurrency. Try to look at it with fresh eyes.

Functions that run with `go` are called _goroutines_. The Go runtime juggles these goroutines and distributes them among operating system threads running on CPU cores. Compared to OS threads, goroutines are lightweight, so you can create hundreds or thousands of them.

> [!NOTE]
> В отличие от Python, так как горутины больше похожи на потоки, выполнение синхронного кода в них не блокирует выполнение всей программы.

При запуске программы единственной горутиной является та, которая вызывает `main()`.

Goroutines are completely independent. When we call `go say()`, the function runs on its own. `main` doesn't wait for it.

Для ожидания окончания выполнения горутин, используют [[Wait Groups]]:

```go
func main() {
    var wg sync.WaitGroup // (1)

    wg.Add(1)             // (2)
    go say(&wg, 1, "go is awesome")

    wg.Add(1)             // (2)
    go say(&wg, 2, "cats are cute")

    wg.Wait()             // (3)
}

// say prints each word of a phrase.
func say(wg *sync.WaitGroup, id int, phrase string) {
    for _, word := range strings.Fields(phrase) {
        fmt.Printf("Worker #%d says: %s...\n", id, word)
        dur := time.Duration(rand.Intn(100)) * time.Millisecond
        time.Sleep(dur)
    }
    wg.Done()             // (4)
}
```

`wg` ➊ has a counter inside. Calling `wg.Add(1)` ➋ increments it by one, while `wg.Done()` ➍ decrements it. `wg.Wait()` ➌ blocks the goroutine (in this case, `main`) until the counter reaches zero. This way, `main` waits for `say(1)` and `say(2)` to finish before it exits.

Нежелательно смешивать бизнес-логику с конкурентной логикой, иначе функцию будет нельзя использовать в синхронном коде. Лучше их разделить, например при помощи анонимных горутин:

```go
func main() {
    var wg sync.WaitGroup
    wg.Add(2)

    go func() {
        defer wg.Done()
        say(1, "go is awesome")
    }()

    go func() {
        defer wg.Done()
        say(2, "cats are cute")
    }()

    wg.Wait()
}
```

![[Wait Groups#Неправильная работа с `sync.WaitGroup`]]

----
## References

- https://antonz.org/go-concurrency/goroutines/
- [[Язык программирования Go (Донован, Керниган)]], глава 8.
- [[Learning Go (Bodner)]], chapter 10 "Concurrency"
- https://habr.com/ru/companies/beget/articles/870138/

----
📂 [[Go]] | Последнее изменение: 02.01.2025 19:20