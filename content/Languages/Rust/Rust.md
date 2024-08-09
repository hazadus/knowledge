Rust Features
Data types
Functions
Expressions
Functions
Functions with Return Values
Control Flow
if Expressions
Using if in a let Statement
Loops
Returning Values from Loops
Loop Labels to Disambiguate Between Multiple Loops
Looping Through a Collection with for
---
# Rust Features
- Rust compiles sources to byte code, then LLVM compiles it to machine code.
- Rust compiles down to binary code with no garbage collection invoked at runtime. This gives you C-like speed. In contrast to C, however, the Rust compiler enforces memory safety at compile time.
- Iterators, although a high-level abstraction, get compiled down to roughly the same code as if you’d written the lower-level code yourself. Iterators are one of Rust’s _zero-cost abstractions_, by which we mean using the abstraction imposes no additional runtime overhead.
# Data types
[https://doc.rust-lang.org/book/ch03-02-data-types.html#data-types](https://doc.rust-lang.org/book/ch03-02-data-types.html#data-types)
# Functions
### Expressions
Expressions evaluate to a value and make up most of the rest of the code that you’ll write in Rust. Consider a math operation, such as `5 + 6`, which is an expression that evaluates to the value `11`. Expressions can be part of statements: in Listing 3-1, the `6` in the statement `let y = 6;` is an expression that evaluates to the value `6`. Calling a function is an expression. Calling a macro is an expression. A new scope block created with curly brackets is an expression, for example:
![[attachments/Untitled 19.png|Untitled 19.png]]
**Source**: [Functions - The Rust Programming Language (rust-lang.org)](https://doc.rust-lang.org/book/ch03-03-how-functions-work.html)
## Functions
### Functions with Return Values
Functions can return values to the code that calls them. We don’t name return values, but we must declare their type after an arrow (->). In Rust, the return value of the function is synonymous with the value of the final expression in the block of the body of a function. You can return early from a function by using the return keyword and specifying a value, but most functions return the last expression implicitly. Here’s an example of a function that returns a value:
![[attachments/Untitled 1 8.png|Untitled 1 8.png]]
Source: [Functions - The Rust Programming Language (rust-lang.org)](https://doc.rust-lang.org/book/ch03-03-how-functions-work.html)
**But if we place a semicolon at the end of the line containing** **`5`****, changing it from an expression to a statement, we’ll get an error!**
# Control Flow
## `if` Expressions
It’s also worth noting that the condition in this code must be a `bool`. If the condition isn’t a `bool`, we’ll get an error. For example, try running the following code:
![[attachments/Untitled 2 7.png|Untitled 2 7.png]]
**Source**: [Control Flow - The Rust Programming Language (rust-lang.org)](https://doc.rust-lang.org/book/ch03-05-control-flow.html)
### Using `if` in a `let` Statement
Because `if` is an expression, we can use it on the right side of a `let` statement to assign the outcome to a variable, as in Listing 3-2.
![[attachments/Untitled 3 6.png|Untitled 3 6.png]]
**Source**: [Control Flow - The Rust Programming Language (rust-lang.org)](https://doc.rust-lang.org/book/ch03-05-control-flow.html)
## Loops
### Returning Values from Loops
One of the uses of a `loop` is to retry an operation you know might fail, such as checking whether a thread has completed its job. You might also need to pass the result of that operation out of the loop to the rest of your code. To do this, you can add the value you want returned after the `break` expression you use to stop the loop; that value will be returned out of the loop so you can use it, as shown here:
![[attachments/Untitled 4 5.png|Untitled 4 5.png]]
**Source**: [Control Flow - The Rust Programming Language (rust-lang.org)](https://doc.rust-lang.org/book/ch03-05-control-flow.html)
### Loop Labels to Disambiguate Between Multiple Loops
If you have loops within loops, `break` and `continue` apply to the innermost loop at that point. You can optionally specify a loop label on a loop that you can then use with `break` or `continue` to specify that those keywords apply to the labeled loop instead of the innermost loop. Loop labels must begin with a single quote. Here’s an example with two nested loops:
![[attachments/Untitled 5 5.png|Untitled 5 5.png]]
**Source**: [Control Flow - The Rust Programming Language (rust-lang.org)](https://doc.rust-lang.org/book/ch03-05-control-flow.html)
### Looping Through a Collection with `for`
![[attachments/Untitled 6 5.png|Untitled 6 5.png]]
![[attachments/Untitled 7 4.png|Untitled 7 4.png]]
**Source**: [Control Flow - The Rust Programming Language (rust-lang.org)](https://doc.rust-lang.org/book/ch03-05-control-flow.html)