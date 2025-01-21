Ниже перечислены недостатки или особенности языка, на которые часто жалуются разработчики. Эти мнения субъективны, но на них стоит обратить внимание, и сделать свои выводы.

- Очень многих раздражает постоянно повторяющийся паттерн обработки ошибок `if err != nil {}`.

----
- Go not having sum types — making it really awkward to have a type that is "either an IPv4 address or an IPv6 address"
- Go choosing which data structures you need — in this case, it's the one-size-fits-all slice, for which you pay 24 bytes on 64-bit machines.
- Go not letting you do operator overloading, harkening back to the Java days where `a == b` isn't the same as `a.equals(b)`
- Go's lack of support for immutable data — the only way to prevent something from being mutated is to only hand out copies of it, and to _be very careful_ to not mutate it in the code that actually has access to the inner bits.
- Go's unwillingness to let you make an opaque "newtype". The only way to do it is to make a separate package and use interfaces for indirection, which is costly _and_ awkward.

Making Go play nice with another language (any other language) is really hard.

Because it has been decided that abstractions are for academics and fools, and all you _really_ need is slices and maps and channels and funcs and structs, it becomes extremely hard to follow what any program is doing at a high level, because everywhere you look, you get bogged down in imperative code doing trivial data manipulation or error propagation.

Because function signatures don't tell you much of anything (does this mutate data? does it hold onto it? is a zero value there okay? does it start a goroutine? can that channel be nil? what types can I really pass for this `interface{}` param?), you rely on documentation, which is costly to update, and costlier still _not_ to update, resulting in more and more bugs.

*Reference:* https://fasterthanli.me/articles/lies-we-tell-ourselves-to-keep-using-golang

----
- Отсутствие в стандартной библиотеке типовых инструментов вроде `map`, `filter`, `reduce`, которые есть в большинстве современных языков. Необходимость устанавливать сторонние библиотеки, чтобы получить эти возможности. 
- Отсутствие мощных ORM.
- Неудобный дебаггер. 

*Reference*: https://brainbaking.com/post/2024/12/why-go-should-sometimes-be-a-no-go/

----
📂 [[Go]] | Последнее изменение: 21.01.2025 08:29