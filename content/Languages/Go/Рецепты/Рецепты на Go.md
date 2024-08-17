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