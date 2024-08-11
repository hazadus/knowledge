## Learning Go
### Jon Bodner · O'Reilly · 2021 · 374 p.

#go #programming #book  

[[Go]] | [[Books Reading]]

https://www.oreilly.com/library/view/learning-go/9781492077206/
[[Jon Bodner - Learning Go_ An Idiomatic Approach to Real-World Go Programming-O'Reilly Media (2021).pdf]]

>[!abstract]
>Go is rapidly becoming the preferred language for building web services. While there are plenty of tutorials available that teach Go's syntax to developers with experience in other programming languages, tutorials aren't enough. They don't teach Go's idioms, so developers end up recreating patterns that don't make sense in a Go context. This practical guide provides the essential background you need to write clear and idiomatic Go.
>
No matter your level of experience, you'll learn how to think like a Go developer. Author Jon Bodner introduces the design patterns experienced Go developers have adopted and explores the rationale for using them. You'll also get a preview of Go's upcoming generics support and how it fits into the language.
>
>- Learn how to write idiomatic code in Go and design a Go project
>- Understand the reasons for the design decisions in Go
>- Set up a Go development environment for a solo developer or team
>- Learn how and when to use reflection, unsafe, and cgo
>- Discover how Go's features allow the language to run efficiently
>- Know which Go features you should use sparingly or not at all

----
## Go Features

- There's no inheritance, ~~no generics~~, no aspect-oriented programming, no function overloading, no operator overloading. No pattern matching, no named parameters, no exceptions.
- No built-in map, filter, reduce functions.
- In Go single quotes and double quotes are *not* interchangeable.
- Go doesn’t allow automatic type promotion between variables. You must use a type conversion when variable types do not match.
- Go has garbage collector.
- You cannot treat another Go type as a boolean.
- Constants in Go are a way to give names to literals. There is no way in Go to declare that a variable is immutable.
- Go requirement is that *every declared local variable must be read*. It is a compile-time error to declare a local variable and to not read its value.
- Any Unicode character that is considered a letter or digit is allowed in variable names.
- In Go, `nil` is an identifier that represents the lack of a value for some types.
- Go is a *call by value* language. Every time you pass a parameter to a function, Go makes a copy of the value that’s passed in.
- According to the language specification, Go source code is always written in UTF-8. Unless you use hexadecimal escapes in a string literal, your string literals are written in UTF-8.
- Built-in embedding support (see *Use Embedding for Composition* in Chapter 7).
- *Channels* are one of the two things that set apart Go’s concurrency model.
- The `select` statement is the other thing that sets apart Go’s concurrency model.

## Go Facts
- Created in 2009.
- Docker, Kubernetes, Prometheus are written in Go.
- Just 25 keywords and 1 loop type (35 keywords in Python).
- Fun fact: UTF-8 was invented in 1992 by Ken Thompson and Rob Pike, two of the creators of Go.
## References
- Плейлист [Ботаним «Go: идиомы и паттерны проектирования», Джон Боднер](https://www.youtube.com/watch?v=YxV58FrR5ZY&list=PLAk6CfuV7hyoOF7rHcHsGg3Sv-ex7Bg10)
- https://gobyexample.com/
----
- [x] 1. Setting Up Your Go Environment (21)
- [x] 2. Primitive Types and Declarations (37)
- [x] 3. Composite Types (55) (01.12)
- [x] 4. Blocks, Shadows, and Control Structures (81) (01.12)
- [x] 5. Functions (107) (01.12)
- [x] 6. Pointers (127) (02.12)
- [x] 7. Types, Methods, and Interfaces (149) (04.12)
- [x] 8. Errors (181) (06.12)
- [x] 9. Modules, Packages, and Imports (197) (08.12)
- [x] 10. Concurrency in Go (223) (11.12)
- [ ] 11. The Standard Library (253)
- [ ] 12. The Context (275)
- [ ] 13. Writing Tests (291)
- [ ] 14. Here There Be Dragons: Reflect, Unsafe, and Cgo (319)
- [ ] 15. A Look at the Future: Generics in Go (345)

### ToDos
- [ ] Watch [GopherCon 2018: Kat Zien - How Do You Structure Your Go Apps](https://www.youtube.com/watch?v=oL6JBUk6tj0)
- [ ] Написать пост [[Впечатления от Learning Go Джона Боднера]] для своего сайта.

----
## Chapter 1. Setting Up Your Go Environment

```bash
go version

go run hello.go
go build hello.go

go install golang.org/x/tools/cmd/goimports@latest
goimports -l -w .
```

----
## Chapter 2. Primitive Types and Declarations

### Literals
Unlike many other languages, in Go single quotes and double quotes are *not* interchangeable. Rune literals represent characters and are surrounded by single quotes.

String literals:
- interpreted string literal – `"Greetings and\n\"Salutations\""`.
- raw string literal:
```go
`Greetings and
"Salutations"`
```
### Booleans
```go
var flag bool // no value assigned, set to false
var isAwesome = true
```
### Numeric Types
#### Integers
- `int8` `int16` `int32` `int64` `uint8` `uint16` `uint32` `uint64`
- A `byte` is an alias for `uint8`
- On most 64-bit CPUs, ==`int`== is a 64-bit signed integer, just like an `int64`.
- The third special name is `uint`. It follows the same rules as `int`, only it is unsigned.
#### Floating point types
- `float32` ==`float64`==

>[!important]
>A floating point number cannot represent a decimal value exactly. Do not use them to represent money or any other value that must have an exact decimal representation!

>[!important]
>While Go lets you use `==` and `!=` to compare floats, don’t do it. Due to the inexact nature of floats, two floating point values might not be equal when you think they should be. Instead, define a maximum allowed variance and see if the difference between two floats is less than that.
#### Complex types (you’re probably not going to use these)
- `complex64` `complex128`
#### Strings
- Strings in Go are immutable; you can reassign the value of a string variable, but you cannot change the value of the string that is assigned to it.
#### Runes
The `rune` type is an alias for the `int32` type, just like `byte` is an alias for `uint8`. As you could probably guess, a rune literal’s default type is a `rune`, and a string literal’s default type is a `string`.

Rune literals represent characters and are surrounded by single quotes. Unlike many other languages, in Go single quotes and double quotes are not interchangeable.
### Explicit Type Conversion
Go doesn’t allow automatic type promotion between variables. You must use a type conversion when variable types do not match.
```go
var x int = 10  
var y float64 = 30.2  
var z float64 = float64(x) + y
var d int = x + int(y)
```
Since all type conversions in Go are explicit, you cannot treat another Go type as a boolean.
If you want to convert from another data type to boolean, you must use one of the comparison operators (`==`, !=, >, <, <=, or >=). For example, to check if variable x is equal to 0, the code would be `x == 0`. If you want to check if string s is empty, use `s == ""`.
### Variable Declaration
```go
var x int = 10
var x = 10
var x int  // Initialized with zero
var x, y int = 10, 20
var x, y int  // Initialized with zero
var x, y = 10, "hello"

// Using :=
var x = 10
// ^^ same as:
x := 10

var x, y = 10, "hello"
// ^^ same as:
x, y := 10, "hello"

```

>[!important]
>There is one limitation on `:=`. If you are declaring a variable at package level, you must use `var` because `:=` is not legal outside of functions.
### Using `const`
`const` in Go is very limited. Constants in Go are a way to give names to literals. They can only hold values that the compiler can figure out at compile time. This means that they can be assigned:
- Numeric literals.
- true and false.
- Strings.
- Runes.
- The built-in functions `complex`, `real`, `imag`, len`,` and `cap` .
- Expressions that consist of operators and the preceding values.

>[!info]
>Constants in Go are a way to give names to literals. There is no way in Go to declare that a variable is immutable.

----
## Chapter 3. Composite Types

### Arrays

```go
var x [3]int  // all three elements initialized with 0

var x = [3]int{10, 20, 30}
// ...or:
var x = [...]int{10, 20, 30}

var x = [12]int{1, 5: 4, 6, 10: 100, 15}  // = [1, 0, 0, 0, 0, 4, 6, 0, 0, 0, 100, 15]

var x [2][3]int

x[0] = 10
fmt.Println(x[2])
fmt.Println(len(x))
```

You can use `==` and `!=` to compare arrays.

Go considers the size of the array to be part of the type of the array. This makes an array that’s declared to be `[3]int` a different type from an array that’s declared to be `[4]int`. This also means that you cannot use a variable to specify the size of an array, because types must be resolved at compile time, not at runtime.
### Slices

```go
var x = []int{10, 20, 30}
```

>[!important]
>Using `[...]` makes an array. Using `[]` makes a slice.

```go
var x = []int{1, 5: 4, 6, 10: 100, 15} // = [1, 0, 0, 0, 0, 4, 6, 0, 0, 0, 100, 15]

var x [][]int

var x []int  // = nil
```

A slice is the first type we’ve seen that isn’t comparable. It is a compile-time error to use `==` to see if two slices are identical or `!=` to see if they are different. The only thing you can compare a slice with is `nil`.

```go
len(x)

var x []int
x = append(x, 10)

var x = []int{1, 2, 3}
x = append(x, 4)
x = append(x, 5, 6, 7)

y := []int{20, 30, 40}
x = append(x, y...) // Similar to "spread" operator in JS!

x := make([]int, 5) // Create slice of size 5, initialized with 0s
x := make([]int, 5, 10) // creates an int slice with a length of 5 and a capacity of 10
```
#### Slicing slices
```go
x := []int{1, 2, 3, 4} // x: [1 2 3 4]
y := x[:2] // y: [1 2]
z := x[1:] // z: [2 3 4]
d := x[1:3] // d: [2 3]
e := x[:] // e: [1 2 3 4]
```

>[!important]
>Note that `e := x[:]` ==does not make the copy== of the original slice! Changing `e` in this example will change `x`, `y`, too! Use built-in `copy()` instead!
#### Slices share storage sometimes
When you take a slice from a slice, you are not making a copy of the data. Instead, you now have two variables that are sharing memory. This means that changes to an element in a slice affect all slices that share that element.

>[!important]
>Be very careful when taking a slice of a slice! Both slices share the same memory and changes to one are reflected in the other. Avoid modifying slices after they have been sliced or if they were produced by slicing. Use a three-part slice expression to prevent append from sharing capacity between slices.

#### `copy()`
See example in `example_3_6a.go`:
```go
x := []int{1, 2, 3, 4}
y := make([]int, 4)
// copy() returns number of elements copied
num := copy(y, x)
```
#### Strings and Runes and Bytes
Under the covers, Go uses a sequence of bytes to represent a string.

The slice expression notation that we used with arrays and slices also works with strings:
```go
var s string = "Hello there"
var s2 string = s[4:7]   // "o t"
var s3 string = s[:5]    // "Hello"
var s4 string = s[6:]    // "there"
```
>[!important]
>Even though Go allows you to use slicing and indexing syntax with strings, you should only use it when you know that your string only contains characters that take up one byte.
### Maps
```go
var nilMap map[string]int
totalWins := map[string]int{}

teams := map[string][]string {  
	"Orcas": []string{"Fred", "Ralph", "Bijou"},
	"Lions": []string{"Sarah", "Peter", "Billie"},
	"Kittens": []string{"Waldo", "Raul", "Ze"},
}

ages := make(map[int][]string, 10)

// Use this syntax to check whether map has the key:
v, ok := totalWins["Pinguins"]
fmt.Println(v, ok)
```

Maps are like slices in several ways:
- Maps automatically grow as you add key-value pairs to them.
- If you know how many key-value pairs you plan to insert into a map, you can use `make` to create a map with a specific initial size.
- Passing a map to the `len` function tells you the number of key-value pairs in a map.
- The zero value for a map is `nil`.
- Maps are not comparable. You can check if they are equal to `nil`, but you cannot check if two maps have identical keys and values using `==` or differ using `!=`.

>[!note]
>You can use the `++` operator to increment the numeric value for a map key. Because a map returns its zero value by default, this works even when there’s no existing value associated with the key.

Key-value pairs are removed from a map via the built-in `delete` function:
```go
m := map[string]int{ 
	"hello": 5,
    "world": 10,
}
delete(m, "hello")
```
The `delete` function takes a map and a key and then removes the key-value pair with the specified key. If the key isn’t present in the map or if the map is `nil`, nothing happens.
#### Using a map as a set
```go
intSet := map[int]bool{}
vals := []int{5, 10, 2, 5, 8, 7, 3, 9, 1, 2, 10}

for _, v := range vals {
	intSet[v] = true
}

if intSet[100] {
	fmt.Println("100 is in the set")
}
```
### Structs
```go
type person struct {
	name string
	age int
	pet string
}

// Both initialize all of the fields in the struct to their zero values:
var fred person
bob := person{}

julia := person {
	"Julia",
	40,
	"cat", 
}

beth := person {
	age:  30,
	name: "Beth",
}

// accessing fields:
bob.name = "Bob"
fmt.Println(beth.name)
```
#### Anonymous Structs
You can also declare that a variable implements a struct type without first giving the struct type a name. This is called an *anonymous struct*:
```go
var person struct { 
	name string
	age int
	pet string 
}

    person.name = "bob"
    person.age = 50
    person.pet = "dog"

pet := struct { 
		name string 
		kind string
    }{        
	    name: "Fido",
		kind: "dog",
    }
```

----
## Chapter 4. Blocks, Shadows, and Control Structures
*Universe Block* is the scope where things like types (e.g. `int`, `string`), constants (`true`, `false`), functions (`make`, `len`) and `nil` are living.
### `if`
```go
n := rand.Intn(10)
if n == 0 {
	fmt.Println("That's too low") 
} else if n > 5 {
	fmt.Println("That's too big:", n)
} else {
    fmt.Println("That's a good number:", n)
}
```
Go adds the ability to declare variables that are scoped to the condition and to both the `if` and else `blocks`.
```go
if n := rand.Intn(10); n == 0 {
	fmt.Println("That's too low")
} else if n > 5 {  
	fmt.Println("That's too big:", n)
} else {  
	fmt.Println("That's a good number:", n)
}
```
### `for`, Four Ways
`for` is the single statement to loop in Go, but it has four formats.
#### Complete `for` statement
```go
for i := 0; i < 10; i++ {
	fmt.Println(i)
}
```
#### The Condition-Only `for` Statement
Equals to `while` in other languages:
```go
i := 1  
for i < 100 {
    fmt.Println(i)
	i=i*2
}
```
#### Infinite Loop
```go
for {
	fmt.Println("Hello")
}
```
Use `break` to exit the loop, and `continue` to proceed to the next iteration.
#### `for`-`range` Statement
Used for iterating over elements in some of Go’s built-in types.

>[!important]
>You can only use a `for`-`range` loop to iterate over the built-in compound types and user-defined types that are based on them.

```go
evenVals := []int{2, 4, 6, 8, 10, 12, 14, 16}
for i, v := range evenVals {
	fmt.Println(i, v)
}
```
##### Iterating over strings
```go
samples := []string{"Hello!", "Emojis🤪🤨🤩"}

for _, sample := range samples {
	for i, r := range sample {
		fmt.Println(i, r, string(r))
	}
	fmt.Println()
}
```
>[!note]
>Use a `for`-`range` loop to access the runes in a string in order.

#### Labeling Your for Statements
Labels can be used with `continue` keyword. See page 96 (76 in the book).

### `switch` statement
```go
words := []string{"a", "cow", "smile", "gopher", "octopus", "anthropologist"}

for _, word := range words {
	switch size := len(word); size {
		case 1, 2, 3, 4:
			fmt.Println(word, "is a short word!")
		case 5:
			wordLen := len(word)
			fmt.Println(word, "is exactly the right length:", wordLen)
		case 6, 7, 8, 9:
		default:
			fmt.Println(word, "is a long word!")
	}
}
```

----
## Chapter 5. Functions

### Variadic Input Parameters and Slices
The variadic parameter *must* be the last (or only) parameter in the input parameter list. You indicate it with three dots (`...`) *before* the type. The variable that’s created within the function is a slice of the specified type. You use it just like any other slice.
```go
func addTo(base int, vals ...int) []int {
	out := make([]int, 0, len(vals))
	for _, v := range vals {
		out = append(out, base+v)
	}
	return out
}
```
### Multiple Return Values
When a Go function returns multiple values, the types of the return values are listed in parentheses, separated by commas. Also, if a function returns multiple values, you must return all of them, separated by commas. Don’t put parentheses around the returned values; that’s a compile-time error.
```go
func divAndRemainder(numerator int, denominator int) (int, int, error) {
	if denominator == 0 {
		return 0, 0, errors.New("can't divide by zero")
	}
	return numerator / denominator, numerator % denominator, nil
}
```
You must assign each value returned from a function. If you try to assign multiple return values to one variable, you get a compile-time error.

Go also allows you to specify *names* for your return values. When you supply names to your return values, what you are doing is pre-declaring variables that you use within the function to hold the return values. They are written as a comma-separated list within parentheses. You must surround named return values with parentheses, even if there is only a single return value. ==Named return values are initialized to their zero values when created.== This means that we can return them before any explicit use or assignment.

>[!important]
>If your function returns values, *never* use a blank return. It can make it very confusing to figure out what value is actually returned.

### Functions Are Values
```go
func add(i int, j int) int { return i + j }
func sub(i int, j int) int { return i - j }
func mul(i int, j int) int { return i * j }
func div(i int, j int) int { return i / j }

var opMap = map[string]func(int, int) int{
	"+": add,
	"-": sub,
	"*": mul,
	"/": div,
}
```
Just like you can use the `type` keyword to define a `struct`, you can use it to define a function type, too:
```go
type opFuncType func(int, int) int
var opMap = map[string]opFuncType{
	// snip...
}
```
### Anonymous Functions
```go
func main() {
	for i := 0; i < 5; i++ {
		func(j int) {
			fmt.Println("printing", j, "from inside of an anonymous function")
		}(i) // Call and pass i as parameter!
	}
}
```
### Closures
Functions declared inside of functions are special; they are *closures*. This is a computer science word that means that ==functions declared inside of functions are able to access and modify variables declared in the outer function==.
```go
people := []Person{
	{"Pat", "Patterson", 37},
	{"Tracy", "Bobbert", 23},
	{"Fred", "Fredson", 18},
}
// Inplace sort this stuff by LastName in ascending order:
sort.Slice(people, func(i int, j int) bool {
	return people[i].LastName < people[j].LastName
})
```
### Returning Functions from Functions
```go
func makeMult(base int) func(int) int {
	return func(factor int) int {
		return base * factor 
	}
}
```
### `defer`
Normally, a function call runs immediately, but `defer` delays the invocation until the surrounding function exits.

You can `defer` multiple closures in a Go function. They run in last-in-first-out order; the last `defer` registered runs first.

----
## Chapter 6. Pointers

The `&` is the *address* operator. It precedes a value type and returns the address of the memory location where the value is stored:
```go
x := "hello"
pointerToX := &x
```
The `*` is the *indirection* operator. It precedes a variable of pointer type and returns the pointed-to value. This is called *dereferencing*:
```go
x := 10
pointerToX := &x
fmt.Println(pointerToX) // prints a memory address
fmt.Println(*pointerToX) // prints 10
z := 5 + *pointerToX
fmt.Println(z) // prints 15
```
Before dereferencing a pointer, you must make sure that the pointer is non-nil. Your program will panic if you attempt to dereference a `nil` pointer:
```go
var x *int  
fmt.Println(x == nil) // prints true
fmt.Println(*x) // panics
```
A *pointer type* is a type that represents a pointer. It is written with a `*` before a type name. A pointer type can be based on any type:
```go
x := 10  
var pointerToX *int
pointerToX = &x
```
The built-in function `new` creates a pointer variable. It returns a pointer to a zero value instance of the provided type:
```go
var x = new(int)  
fmt.Println(x == nil) // prints false
fmt.Println(*x) // prints 0
```
The right way to update the value where the pointer points to:
```go
func update(px *int) {
	*px = 20
}

func main() {
	x := 10
	update(&x)
	fmt.Println(x) // prints 20
}
```

>[!important]
>You should be careful when using pointers in Go. The only time you should use pointer parameters to modify a variable is when the function expects an interface. You see this pattern when working with JSON. Because JSON integration is so common, this API is sometimes treated as a common case by new Go developers, instead of the exception that it should be.

>[!important]
>Рекомендуется умеренное использование указателей в коде, чтобы сократить объем работы сборщика мусора.

----
## Chapter 7. Types, Methods, and Interfaces
Defining concrete types:
```go
type Score int  
type Converter func(string)Score
type TeamScores map[string]Score
```
### Methods
Go supports methods on user-defined types.
```go
type Person struct {
	FirstName string
	LastName string
	Age int
}

func (p Person) String() string {
	return fmt.Sprintf("%s %s, age %d", p.FirstName, p.LastName, p.Age)
}

p := Person {
	FirstName: "Fred",
	LastName:"Fredson",
	Age: 52,
}
output := p.String()
```
Method declarations look just like function declarations, with one addition: the *receiver* specification. The receiver appears between the keyword func and the name of the method. Just like all other variable declarations, the receiver name appears before the type. ==By convention, the receiver name is a short abbreviation of the type’s name, usually its first letter. It is nonidiomatic to use `this` or `self`.==

Just like functions, ==method names cannot be overloaded==. You can use the same method names for different types, but you can’t use the same method name for two different methods on the same type.

Methods must be declared in the same package as their associated type; Go doesn’t allow you to add methods to types you don’t control. While you can define a method in a different file within the same package as the type declaration, it is best to keep your type definition and its associated methods together so that it’s easy to follow the implementation.
### Pointer Receivers and Value Receivers
```go
type Counter struct {
	total int
	lastUpdated time.Time
}

// Method changes the receiver -> use pointer:
func (c *Counter) Increment() {
		c.total++
        c.lastUpdated = time.Now()
    }

// Method does not change the receiver -> use value:
func (c Counter) String() string {  
	return fmt.Sprintf("total: %d, last updated: %v", c.total, c.lastUpdated)
}

var c Counter
fmt.Println(c.String())
// Automatically converted to (&c).Increment():
c.Increment()
fmt.Println(c.String())
```
==Do not write getter and setter methods for Go structs, unless you need them to meet an interface.== Go encourages you to directly access a field. Reserve methods for business logic. The exceptions are when you need to update multiple fields as a single operation or when the update isn’t a straightforward assignment of a new value.
### Methods Are Functions Too
```go
type Adder struct {
	start int
}

func (a Adder) AddTo(val int) int {
	return a.start + val
}

myAdder := Adder{start: 10}
fmt.Println(myAdder.AddTo(5)) // prints 15

f1 := myAdder.AddTo  
fmt.Println(f1(10)) // prints 20

f2 := Adder.AddTo
fmt.Println(f2(myAdder, 15)) // prints 25
```
### Functions Versus Methods
>[!info]
>Package-level state should be effectively immutable.
>
>Any time your logic depends on values that are configured at startup or changed while your program is running, those values should be stored in a struct and that logic should be implemented as a **method**.
>
>If your logic only depends on the input parameters, then it should be a **function**.

### `iota` Is for Enumerations—Sometimes
```go
type MailCategory int

const (  
	Uncategorized MailCategory = iota Personal  // 0
	Spam           // int, 1
	Social         // int, 2
	Advertisements // int, 3
)
```
### Use Embedding for Composition
```go
type Employee struct {
	Name string
	ID string
}

func (e Employee) Description() string {  
	return fmt.Sprintf("%s (%s)", e.Name, e.ID)
}

type Manager struct { 
		Employee  // sic!
        Reports []Employee
    }

func (m Manager) FindNewEmployees() []Employee {
	// do business logic
}
```
Note that `Manager` contains a field of type `Employee`, but no name is assigned to that field. This makes `Employee` an *embedded field*. Any fields or methods declared on an embedded field are *promoted* to the containing struct and can be invoked directly on it. That makes the following code valid:
```go
m := Manager{
	Employee: Employee {
		Name:         "Bob Bobson",
		ID:           "12345",
	},
	Reports: []Employee{},
}

fmt.Println(m.ID) // prints 12345
fmt.Println(m.Description()) // prints Bob Bobson (12345)
```
### A Quick Lesson on Interfaces
```go
type Stringer interface {
	String() string
}
```
It lists the methods that must be implemented by a concrete type to meet the interface. The methods defined by an interface are called the method set of the interface.

Interfaces are usually named with “er” endings. Examples: `io.Reader`, `io.Closer`, `io.ReadCloser`, `json.Marshaler`, and `http.Handler`.

What makes Go’s interfaces special is that they are implemented *implicitly*. A concrete type does not declare that it implements an interface. ==If the method set for a concrete type contains all of the methods in the method set for an interface, the concrete type implements the interface. This means that the concrete type can be assigned to a variable or field declared to be of the type of the interface==.

```go
type LogicProvider struct {}

func (lp LogicProvider) Process(data string) string {
	// business logic
}

type Logic interface {
	Process(data string) string
}

type Client struct{
	L Logic
}

func(c Client) Program() {  
	// get data from somewhere
	c.L.Process(data)
}

main() {
	c := Client{
		L: LogicProvider{},
	}
	c.Program()
}
```
In the Go code, there is an interface, but only the caller (`Client`) knows about it; there is nothing declared on `LogicProvider` to indicate that it meets the interface. This is sufficient to both allow a new logic provider in the future and provide executable documentation to ensure that any type passed into the client will match the client’s need.

>[!info]
>Interfaces specify what callers need. The client code defines the interface to specify what functionality it requires.

### Embedding and Interfaces
```go
type Reader interface {  
	Read(p []byte) (n int, err error)
}

type Closer interface {
	Close() error
}

type ReadCloser interface {
	Reader
	Closer
}
```
### The Empty Interface Says Nothing
Sometimes in a statically typed language, you need a way to say that a variable could store a value of any type. Go uses `interface{}` to represent this:
```go
var i interface{} i = 20  
i = "hello"  
i = struct {
	FirstName string
	LastName string  
} {"Fred", "Fredson"}
```
You should note that `interface{}` isn’t special case syntax. An empty interface type simply states that the variable can store any value whose type implements zero or more methods. This just happens to match every type in Go.
```go
// one set of braces for the interface{} type,  
// the other to instantiate an instance of the map  
data := map[string]interface{}{}  
contents, err := ioutil.ReadFile("testdata/sample.json")
if err != nil {
	return err
}
defer contents.Close()
json.Unmarshal(contents, &data)  
// the contents are now in the data map
```

>[!important]
>These situations should be relatively rare. Avoid using `interface{}`. As we’ve seen, Go is designed as a strongly typed language and attempts to work around this are unidiomatic.

----
## Chapter 8. Errors
### How to Handle Errors: The Basics
>[!info]
>Go handles errors by returning a value of type error as the last return value for a function. This is entirely ==by convention, but it is such a strong convention that it should never be breached==. When a function executes as expected, `nil` is returned for the error parameter. If something goes wrong, an error value is returned instead. The calling function then checks the error return value by comparing it to nil, handling the error, or returning an error of its own.
>
>Error messages should not be capitalized nor should they end with punctuation or a newline.

```go
func calcRemainderAndMod(numerator, denominator int) (int, int, error) {
	if denominator == 0 {
		return 0, 0, errors.New("denominator is 0")
	}
	return numerator / denominator, numerator % denominator, nil
}

func main() {
	numerator := 20
	denominator := 3  
	remainder, mod, err := calcRemainderAndMod(numerator, denominator)
	
	if err != nil {
		fmt.Println(err) // Calls err.Error()
		os.Exit(1) 
	}
	
	fmt.Println(remainder, mod)
}
```

`error` is a built-in interface that defines a single method:

```go
type error interface {
	Error() string
}
```

The second way is to use the `fmt.Errorf` function. This function allows you to use all of the formatting verbs for `fmt.Printf` to create an `error`. Like `errors.New`, this string is returned when you call the `Error` method on the returned `error` instance:

```go
func doubleEven(i int) (int, error) { 
	if i % 2 != 0 {
		return 0, fmt.Errorf("%d isn't an even number", i)
	}
	return i * 2, nil
}
```
### Wrapping Errors
When you preserve an error while adding additional information, it is called *wrapping* the error. When you have a series of wrapped errors, it is called an *error chain*.

There’s a function in the Go standard library that wraps errors, and we’ve already seen it. The `fmt.Errorf` function has a special verb, `%w`. Use this to create an error whose formatted string includes the formatted string of another error and which contains the original error as well. The convention is to write: `%w` at the end of the error format string and make the error to be wrapped the last parameter passed to `fmt.Errorf`.

The standard library also provides a function for unwrapping errors, the `Unwrap` function in the `errors` package. You pass it an error and it returns the wrapped error, if there is one. If there isn’t, it returns `nil`.

```go
func fileChecker(name string) error {
	f, err := os.Open(name)
	if err != nil {
		return fmt.Errorf("in fileChecker: %w", err)
	}
	f.Close()
	return nil
}

func main() {
	err := fileChecker("not_here.txt")
	if err != nil {
		fmt.Println(err)
		if wrappedErr := errors.Unwrap(err); wrappedErr != nil {
			fmt.Println(wrappedErr)
		}
	}
}
```
### Wrapping Errors with `defer`
```go
func DoSomeThings(val1 int, val2 string) (_ string, err error) {
	defer func() {
		if err != nil {  
			err = fmt.Errorf("in DoSomeThings: %w", err)
		}
	}()
	
	val3, err := doThing1(val1)
	if err != nil {
		return "", err
	}

	val4, err := doThing2(val2)
	if err != nil {
		return "", err
	}

	return doThing3(val3, val4)
}
```
This pattern works well when you are wrapping every error with the same message. If you want to customize the wrapping error to provide more context about what caused the error, then put both the specific and the general message in every `fmt.Errorf`.
### panic and recover
Go generates a panic whenever there is a situation where the Go runtime is unable to figure out what should happen next. This could be due to a programming error (like an attempt to read past the end of a slice) or environmental problem (like running out of memory). As soon as a panic happens, the current function exits immediately and any defers attached to the current function start running. When those defers complete, the defers attached to the calling function run, and so on, until main is reached. The program then exits with a message and a stack trace.

```go
func doPanic(msg string) {
	panic(msg)
}

func main() {
	doPanic(os.Args[0])
}
```

Go provides a way to capture a panic to provide a more graceful shutdown or to pre‐ vent shutdown at all. The built-in `recover` function is called from within a `defer` to check if a panic happened. If there was a panic, the value assigned to the panic is returned. Once a `recover` happens, execution continues normally.

```go
func div60(i int) {
	defer func() {
		if v := recover(); v != nil {
			fmt.Println(v) // "runtime error: integer divide by zero"
		}
	}()

	fmt.Println(60 / i)
}

func main() {
	for _, val := range []int{1, 2, 0, 6} {
		div60(val)
	}
}
```

>[!important]
>While `panic` and `recover` look a lot like exception handling in other languages, they are not intended to be used that way. Reserve panics for fatal situations and use `recover` as a way to gracefully handle these situations. If your program panics, be very careful about trying to continue executing after the panic. It’s very rare that you want to keep your program running after a panic occurs. If the panic was triggered because the computer is out of a resource like memory or disk space, the safest thing to do is use `recover` to log the situation to monitoring software and shut down with `os.Exit(1)`. If there’s a programming error that caused the panic, you can try to con‐ tinue, but you’ll likely hit the same problem again.

----
## Chapter 9. Modules, Packages, and Imports
Before we can use code from packages outside of the standard library, we need to make sure that we have declared that our project is a module. Every module has a globally unique identifier. This is not unique to Go.

### `go.mod`
```bash
go mod init github.com/hazadus/go-hello/bodner/ch9/package_example
```

### Imports and Exports
Go’s `import` statement allows you to access exported constants, variables, functions, and types in another package. A package’s exported identifiers (an *identifier* is the name of a variable, constant, type, function, method, or a field in a struct) cannot be accessed from another current package without an `import` statement.

Rather than use a special keyword, Go uses *capitalization* to determine if a package-level identifier is visible outside of the package where it is declared. ==An identifier whose name starts with an uppercase letter is *exported*==. Conversely, an identifier whose name starts with a lowercase letter or underscore can only be accessed from within the package where it is declared.

You must specify an *import path* when importing from anywhere besides the standard library. The import path is built by appending the path to the package within the module to the module path.

>[!important]
>While you can use a relative path to import a dependent package within the same module, don’t do this. Absolute import paths clar‐ ify what you are importing and make it easier to refactor your code.

[Example on how to create packages](https://github.com/hazadus/go-hello/tree/main/bodner/ch9/package-example) in Go program.

### Naming Packages
It’s better to create one function called `Names` in a package called `extract` and a second function called `Names` in a package called `format`. It’s OK for these two functions to have the same name, because they will always be disambiguated by their package names. The first will be referred to as `extract.Names` when imported, and the second will be referred to as `format.Names`.

### Overriding a Package’s Name
```go
import (  
	crand "crypto/rand"
	"encoding/binary"
	"fmt"  
	"math/rand"
)
```
The package name `.` places all the exported identifiers in the imported package into the current package’s namespace; you don’t need a prefix to refer to them. ==This is discouraged because it makes your source code less clear== as you no longer know whether something is defined in the current package or an imported one by simply looking at its name.

### Package Comments and godoc
Go has its own format for writing comments that are automatically converted into documentation. It’s called *godoc* format and it’s very simple. There are no special symbols in a godoc comment. They just follow a convention. Here are the rules:
- Place the comment directly before the item being documented with no blank lines between the comment and the declaration of the item.
- Start the comment with two forward slashes (`//`) followed by the name of the item.  
- Use a blank comment to break your comment into multiple paragraphs.
- Insert preformatted comments by indenting the lines.

Go includes a command-line tool called go doc that views godocs. The command `go doc PACKAGE_NAME` displays the package godocs for the specified package and a list of the identifiers in the package. Use `go doc PACKAGE_NAME.IDENTIFIER_NAME` to display the documentation for a specific identifier in the package.

### The `internal` Package
See [example from the book](https://github.com/learning-go-book/internal_example/blob/master/foo/foo.go).
### Circular Dependencies
Go does not allow you to have a circular dependency between packages.

If two packages depend on each other, there’s a good chance they should be merged into a single package.

If you have a good reason to keep your packages separated, it may be possible to move just the items that cause the circular dependency to one of the two packages or to a new package.

----
## Chapter 10. Concurrency in Go
### Goroutines

Goroutines are lightweight processes managed by the Go runtime. When a Go program starts, the Go runtime creates a number of threads and launches a single goroutine to run your program. All of the goroutines created by your program, including the initial one, are assigned to these threads automatically by the Go runtime scheduler, just as the operating system schedules threads across CPU cores. This might seem like extra work, since the underlying operating system already includes a scheduler that manages threads and processes, but it has several benefits:
- Goroutine creation is faster than thread creation, because you aren’t creating an operating system–level resource.
- Goroutine initial stack sizes are smaller than thread stack sizes and can grow as needed. This makes goroutines more memory efficient.
- Switching between goroutines is faster than switching between threads because it happens entirely within the process, avoiding operating system calls that are (relatively) slow.
- The scheduler is able to optimize its decisions because it is part of the Go process.

These advantages allow Go programs to spawn hundreds, thousands, even tens of thousands of simultaneous goroutines.

==Any function can be launched as a goroutine.== This is different from JavaScript, where a function only runs asynchronously if the author of the function declared it with the async keyword. However, ==it is customary in Go to launch goroutines with a closure that wraps business logic==. The closure takes care of the concurrent bookkeeping. For example, the closure reads values out of channels and passes them to the business logic, which is completely unaware that it is running in a goroutine. The result of the function is then written back to a different channel.
```go
func process(val int) int {
	// do something with val
}

func runThingConcurrently(in <-chan int, out chan<- int){
	go func() {
		for val := range in {
			result := process(val)
			out <- result
		}
	}()
}
```

### Channels
Channels are one of the two things that set apart Go’s concurrency model.

Goroutines communicate using *channels*. Like slices and maps, channels are a built-in type created using the `make` function:
```go
ch := make(chan int)
```
Like maps, channels are reference types. When you pass a channel to a function, you are really passing a pointer to the channel.

### Reading, Writing, and Buffering
```go
a := <-ch // reads a value from ch and assigns it to a
ch <- b   // write the value in b to ch
```

### `for`-`range` and Channels
```go
for v := range ch {
	fmt.Println(v)
}
```
The loop continues until the channel is closed, or until a `break` or `return` statement is reached.

### Closing a Channel
```go
close(ch)
```

```go
v, ok := <-ch
```
If `ok` is set to `true`, then the channel is open. If it is set to `false`, the channel is closed.

The responsibility for closing a channel lies with the goroutine that writes to the channel. Be aware that closing a channel is only required if there is a goroutine waiting for the channel to close (such as one using a `for`-`range` loop to read from the channel). Since a channel is just another variable, Go’s runtime can detect channels that are no longer used and garbage collect them.

### `select`
The `select` statement is the other thing that sets apart Go’s concurrency model. It is the control structure for concurrency in Go, and it elegantly solves a common problem: if you can perform two concurrent operations, which one do you do first? You can’t favor one operation over others, or you’ll never process some cases.

```go
select {  
case v := <-ch:
	fmt.Println(v)
case v := <-ch2:
	fmt.Println(v)
case ch3 <- x:
	fmt.Println("wrote", x)
case <-ch4:
    fmt.Println("got value on ch4, but ignored it")
}
```

```go
for {  
	select {
	case <-done:
		return
	case v := <-ch:
		fmt.Println(v)
	}
}
```

The following code does not wait if there’s no value to read in `ch`; it immediately executes the body of the `default`:
```go
select {  
case v := <-ch:
	fmt.Println("read from ch:", v)
default:
	fmt.Println("no value written to ch")
}
```

### Concurrency Practices and Patterns
#### Keep Your APIs Concurrency-Free
Concurrency is an implementation detail, and good API design should hide implementation details as much as possible. This allows you to change how your code works without changing how your code is invoked.

#### Goroutines, for Loops, and Varying Variables
Any time your goroutine uses a variable whose value might change, pass the current value of the variable into the goroutine.
```go
for _, v := range a {
	go func(val int) {
        ch <- val * 2
    }(v)
}
```
#### Always Clean Up Your Goroutines
Whenever you launch a goroutine function, you must make sure that it will eventually exit. Unlike variables, the Go runtime can’t detect that a goroutine will never be used again. If a goroutine doesn’t exit, the scheduler will still periodically give it time to do nothing, which slows down your program.

----
## Chapter 11. The Standard Library
### `time`
Reference: https://pkg.go.dev/time

There are two main types used to represent time, `time.Duration` and `time.Time`.
```go
d := 2 * time.Hour + 30 * time.Minute // d is of type time.Duration
```
An moment of time is represented with the `time.Time` type, complete with a time zone. You acquire a reference to the current time with the function `time.Now`. This returns a `time.Time` instance set to the current local time.

The `time.Parse` function converts from a string to a `time.Time`, while the `Format` method converts a `time.Time` to a `string`.

`time.Format` relies on the idea of formatting the date and time January 2, 2006 at 3:04:05PM MST (Mountain Standard Time) to specify your format.
```go
t, err := time.Parse("2006-02-01 15:04:05 -0700", "2016-13-03 00:00:00 +0000") if err != nil {
	return err
}
fmt.Println(t.Format("January 2, 2006 at 3:04:05PM MST"))
// March 13, 2016 at 12:00:00AM UTC
```
### `encoding/json`
Go’s standard library includes support for converting Go data types to and from JSON. The word ==*marshaling*== means converting from a Go data type to an encoding, and ==*unmarshaling*== means converting to a Go data type.
#### Use Struct Tags to Add Metadata
Let’s say that we have to read and write the following JSON:
```json
{        
	"id":"12345",
	"date_ordered":"2020-05-01T13:01:02Z",
	"customer_id":"3",
	"items":[{"id":"xyz123","name":"Thing 1"},{"id":"abc789","name":"Thing 2"}]
}
```
```go
type Order struct {  
	ID string `json:"id"`
	DateOrdered time.Time `json:"date_ordered"`
	CustomerID string `json:"customer_id"`
	Items []Item `json:"items"`
}

type Item struct {
	ID string `json:"id"`
	Name string `json:"name"`
}
```
#### Unmarshaling and Marshaling
```go
var o Order  
err := json.Unmarshal([]byte(data), &o)
if err != nil {
	return err
}
```

----
📂 [[Reading]]