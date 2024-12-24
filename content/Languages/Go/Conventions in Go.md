
- Functions that panic should have “Must” in their name
- In multi-value returns, put the error value last
- **Don't use naked returns**. If you name return arguments, you don't need to use them in the return directive. Do it anyway!
- **Return early**. Implement error handling as `if err != nil` rather than `if err == nil`.
- **Avoid stutter**. If your package name is `vectordb`, don't create functions like `NewVectorDB` or `OpenVectorDB`. Remember they will be used along with the package name: `vectordb.NewVectorDB()`, `vectordb.OpenVectorDB()`. Avoid this stutter! `New()` or `Open()` is perfectly fine.
- **Interfaces are Doers, and they are small**. Interface names are kind of special in Go. Where other languages prepend a capital I to the name, Go chooses names ending in -er, such as Reader, Writer, or Closer. Besides that, interfaces are also small—a single function per interface is quite common.
- **Getters without Get**. Methods that read a value should not be prepended with “Get”. For example, if your method returns a URL, name it `URL()` rather than `GetURL()`.

## References

- https://appliedgo.net/spotlight/conventions-in-go/

----
📂 [[Go]] | Последнее изменение: 24.12.2024 14:22