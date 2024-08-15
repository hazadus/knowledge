## Оглавление

Материалы о языке #Go .

- [[План изучения языка Go]]
- [[Идеи проектов на Go]]
- Материалы книги [[Learning Go (Bodner)]]
- [[Почему Go?]]
- [[Общие сведения о Go]]
	- [[Многопоточность в Go]]
	- [[Go Proverbs]]
- [[Особенности языка Go]]
- [[Настройка окружения]]
- [[Система типов]]
	- [[Базовые типы в Go]]
	- [[Переменные и константы]]
	- [[Область видимости]]: локальные, глобальные, экспортируемые переменные.
- Управление потоком выполнения
	- [[Операторы ветвления]]

----
## References

- [Официальный сайт](https://go.dev/)
- [The Go Playground](https://go.dev/play/)
- [Robert Griesemer. Go for C programmers](https://talks.golang.org/2012/goforc.slide#1)
- [Effective Go - The Go Programming Language](https://go.dev/doc/effective_go)
- [CodeReviewComments · golang/go Wiki (github.com)](https://github.com/golang/go/wiki/CodeReviewComments)

----
### CLI
```Bash
go version
# Build or run single file:
go build main.go
go clean main.go
go run main.go
# Init Go module in the current directory:
go mod init tools
# Run project in current directory:
go run .
go doc
go fmt
go get
go install
go help
go test
# Detect problems:
go vet
```
## Basic program structure

```Go
// Each code file has to declare package to which its contents belong:
package main
// Declare dependency on built-in package
import "fmt"
// `main()` in the main package is the program's entry point
func main() {
	fmt.Println("Hello, Go world!")
	for i := 0; i < 5; i++ {
		fmt.Println(i)
	}
}
```
**NB:** by convention, semicolons are omitted in Go code, althought might be used.
## Packages
Built-in Go packages: [Standard library - Go Packages](https://pkg.go.dev/std)

----
📂 [[Go]]