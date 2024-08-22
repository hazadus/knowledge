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

### Сборка для конкретной ОС

Список поддерживаемых ОС: https://go.dev/src/go/build/syslist.go

```bash
# Указать целевую систему в переменной окружения и выполнить сборку:
GOOS=windows go build
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

### Рекурсивный обход всех файлов и директорий

```go
package main

import (
    "fmt"
    "os"
    "path/filepath"
)

func main() {
    PrintAllFiles(".")
}

func PrintAllFiles(path string) {
    // получаем список всех элементов в папке (и файлов, и директорий)
    files, err := os.ReadDir(path)
    if err != nil {
        fmt.Println("unable to get list of files", err)
        return
    }
    //  проходим по списку
    for _, f := range files {
        // получаем имя элемента
        // filepath.Join — функция, которая собирает путь к элементу с разделителями
        filename := filepath.Join(path, f.Name())
        // печатаем имя элемента
        fmt.Println(filename)
        // если элемент — директория, то вызываем для него рекурсивно ту же функцию
        if f.IsDir() {
            PrintAllFiles(filename)
        }
    }
} 
```

## Замыкания (closures)

### Итератор на замыканиях

```go
func Generate(seed int) func() {
    return func() {
        fmt.Println(seed) // замыкание получает внешнюю переменную seed
        seed += 2 // переменная модифицируется
    }
    
}

func main() {
    iterator := Generate(0)
    iterator()
    iterator()
    iterator()
    iterator()
    iterator()
} 
```

----
## Работа с файлами

...

----
## Работа с JSON
### Marshal `struct` to JSON

```go
type Person struct {
    Name        string    `json:"Имя"`
    Email       string    `json:"Почта"`
    DateOfBirth time.Time `json:"-"` // - означает, что это поле не будет сериализовано
}

func main() {
    man := Person{
        Name:        "Alex",
        Email:       "alex@yandex.ru",
        DateOfBirth: time.Now(),
    }
    jsMan, err := json.Marshal(man)
    if err != nil {
        log.Fatalln("unable marshal to json")
    }
    fmt.Printf("Man %v", string(jsMan)) // Man {"Имя":"Alex","Почта":"alex@yandex.ru"}
}
```

### Unmarshal JSON string to `struct`

```go
package main

import (
    "encoding/json"
    "fmt"
)

const rawResp = `
{
    "header": {
        "code": 0,
        "message": ""
    },
    "data": [{
        "type": "user",
        "id": 100,
        "attributes": {
            "email": "bob@yandex.ru",
            "article_ids": [10, 11, 12]
        }
    }]
}
`

type (
    Response struct {
        Header ResponseHeader `json:"header"`
        Data   ResponseData   `json:"data,omitempty"`
    }

    ResponseHeader struct {
        Code    int    `json:"code"`
        Message string `json:"message,omitempty"`
    }

    ResponseData []ResponseDataItem

    ResponseDataItem struct {
        Type       string                `json:"type"`
        Id         int                   `json:"id"`
        Attributes ResponseDataItemAttrs `json:"attributes"`
    }

    ResponseDataItemAttrs struct {
        Email      string `json:"email"`
        ArticleIds []int  `json:"article_ids"`
    }
)

func ReadResponse(rawResp string) (Response, error) {
    resp := Response{}
    if err := json.Unmarshal([]byte(rawResp), &resp); err != nil {
        return Response{}, fmt.Errorf("JSON unmarshal: %w", err)
    }

    return resp, nil
}

func main() {
    resp, err := ReadResponse(rawResp)
    if err != nil {
        panic(err)
    }
    fmt.Printf("%+v\n", resp)
}
```

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
## Алгоритмы

Примеры реализации популярных алгоритмов на Go.

### Quicksort

Пример мой, возможно – не лучший.

```go
// Quicksort algorithm demo
package main

import "fmt"

// SortNumbers ...
// Sort `numbers` using quicksort algorithm
func SortNumbers(numbers []int) []int {
	if numbers == nil {
		return []int{}
	}

	if len(numbers) < 2 {
		return numbers
	}

	pivot := numbers[0]
	var less []int
	var more []int

	for _, i := range numbers[1:] {
		if i <= pivot {
			less = append(less, i)
		} else {
			more = append(more, i)
		}
	}

	return append(append(SortNumbers(less), pivot), SortNumbers(more)...)
}

func main() {
	array := []int{99, 88, 77, 66, 55, 44, 33, 22, 11}
	fmt.Println(SortNumbers(array))
}
```

### Пример рекурсивного вычисления `n!`, факториала числа

```go
func fact(n int) int {
    if n == 0 {    // терминальная ветка — то есть условие выхода из рекурсии
        return 1
    } else {    // рекурсивная ветка 
        return n * fact(n-1)
    }
} 
```

### Числа Фибоначчи

```go
func Fib(n int) int {
    switch {
    case n <= 1:    // терминальная ветка 
        return n
    default:        // рекурсивная ветка
        return Fib(n-1) + Fib(n-2)
    }
} 
```


----
📂 [[Рецепты]] | Последнее изменение: 21.08.2024 07:42