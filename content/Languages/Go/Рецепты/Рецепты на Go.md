## CLI

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

----
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
**NB:** by convention, semicolons are omitted in Go code, althought might be used.## Работа со строками

...

----
## Слайсы
### Объединение слайсов

Чтобы соединить два слайса, нужно распаковать слайс `append(a,b...)`. Функция принимает некоторое количество отдельных элементов и преобразует слайс в список через распаковку.

### Сортировка

```go
 s := []int{5, 4, 1, 3, 2}
    sort.Ints(s)
    fmt.Println(s) // [1 2 3 4 5] 
```

Функция `sort.Ints` сортирует полученный слайс целых чисел по возрастанию. Она не меняет размер и ёмкость слайса, поэтому может спокойно работать с ним.

### Копирование слайсов

Для копирования элементов из одного слайса в другой применяется функция `copy([]T dest, []T src)`, где `dest` — это слайс-приёмник, а `src` — слайс-источник. Эта функция только перезаписывает элементы, поэтому количество скопированных элементов будет равно меньшей длине из двух слайсов.

```go
var dest []int
dest2, dest3 := make([]int, 3),  make([]int, 5)
src := []int{1, 2, 3, 4}
copy(dest, src)
copy(dest2, src)
copy(dest3, src)
fmt.Println(dest, dest2, dest3, src ) // [] [1 2 3] [1 2 3 4 0] [1 2 3 4] 
```

### Удаление последнего элемента слайса

```go
    s := []int{1, 2, 3}
    if len(s) != 0 { // защищаемся от паники
        s = s[:len(s)-1]
    }
    fmt.Println(s) // [1 2] 
```

### Удаление первого элемента слайса

```go
    s := []int{1,2,3}
    if len(s) != 0 { // защищаемся от паники
        s = s[1:]
    } 
    fmt.Println(s) // [2 3] 
```

### Удаление элемента слайса с индексом `i`

```go
    s := []int{1,2,3,4,5}
    i := 2
    
    if len(s) != 0 && i < len(s) { // защищаемся от паники
        s = append(s[:i], s[i+1:]...)
    } 
    fmt.Println(s) // [1 2 4 5] 
```

### Сравнение двух слайсов

```go
    
  s1 := []int{1,2,3}
    s2 := []int{1,2,4}
    s3 := []string{"1","2","3"}
    s4 := []int{1,2,3}

    fmt.Println(reflect.DeepEqual(s1,s2)) // false
    fmt.Println(reflect.DeepEqual(s1,s3)) // false
    fmt.Println(reflect.DeepEqual(s1,s4)) // true 
```

### Misc

https://ueokande.github.io/go-slice-tricks/

![[Pasted image 20240818092837.png]]

----
## Работа со строками
### Удаление пробелов в начале и конце строки

```go
import (
    "bytes"
    "fmt"
)

func main() {
    bSlice := []byte(" \t\n a lone gopher \n\t\r\n")
    fmt.Printf("%s", bytes.TrimSpace(bSlice)) // a lone gopher
    fmt.Printf("%s", bSlice)  // \t\n a lone gopher \n\t\r\n 
    
} 
```

Функция `bytes.TrimSpace` принимает слайс байт и возвращает новый слайс байт, откуда были удалены начальные и конечные пробельные символы. Размер слайса должен измениться, а значит, `bSlice` останется нетронутым. В итоге `bytes.TrimSpace` подарит нам новый слайс.

----
## Взаимодействие с ОС
### Чтение переменных окружения

...

----
## Работа с файлами

...

----
## CI/CD pipeline

```yaml
name: Go CI/CD Pipeline

on:
  push:
    branches:
      - main

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout repository
      uses: actions/checkout@v2
      
    - name: Set up Go
      uses: actions/setup-go@v2
      with:
        go-version: 1.17

    - name: Build
      run: go build -v ./...

    - name: Test
      run: go test -v ./...

  deploy:
    runs-on: ubuntu-latest
    needs: build
    if: github.ref == 'refs/heads/main'

    steps:
    - name: Deploy to server
      run: |
        # Add deployment script here        
```


----
📂 [[Рецепты]]