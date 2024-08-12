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
## Приложения #go
### Building a Chat Application with WebSockets

See [10 Project Ideas To Learn Golang In 2024](https://golang.withcodeexample.com/blog/golang-project-ideas/)

### Image Processing and Computer Vision with Golang

See [10 Project Ideas To Learn Golang In 2024](https://golang.withcodeexample.com/blog/golang-project-ideas/)

----
## Справочные материалы
- [10 Project Ideas To Learn Golang In 2024](https://golang.withcodeexample.com/blog/golang-project-ideas/)


----
📂 [[Go]]