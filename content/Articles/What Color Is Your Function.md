![rw-book-cover](https://readwise-assets.s3.amazonaws.com/static/images/article1.be68295a7e40.png)

## Metadata
- Author: [[stuffwithstuff.com]]
- Full Title: What Color Is Your Function?
- Category: #articles
- Document Note: Автор с юмором разбирает проблемы конкурентности в разных языках. Модель, использованная в Go, приведена в качестве положительного примера.
- Document Tags: [[Go]] 
- Summary: In this programming language, every function is either red or blue, affecting how they can be called. Red functions are asynchronous and more complicated to use, while blue functions are simpler and synchronous. The challenge arises when trying to reuse code that involves red functions, leading to frustration in managing asynchronous operations.
- URL: https://journal.stuffwithstuff.com/2015/02/01/what-color-is-your-function/

## Highlights
- When calling a function, you need to use the call that corresponds to its color. If you get it wrong—call a red function with `blue` after the parentheses or vice versa—it does something bad. Dredge up some long-forgotten nightmare from your childhood like a clown with snakes for arms hiding under your bed. That jumps out of your monitor and sucks out your vitreous humour.
  Annoying rule, right? ([View Highlight](https://read.readwise.io/read/01jj3vvyf2zd2g4jyx0f8f04pd))

- Go is the language that does this most beautifully in my opinion. As soon as you do any IO operation, it just parks that goroutine and resumes any other ones that aren’t blocked on IO.
  If you look at the IO operations in the standard library, they seem synchronous. In other words, they just do work and then return a result when they are done. But it’s not that they’re synchronous in the sense that it would mean in JavaScript. Other Go code can run while one of these operations is pending. It’s that Go has *eliminated the distinction between synchronous and asynchronous code*.
  Concurrency in Go is a facet of how *you* choose to model your program, and not a color seared into each function in the standard library. This means all of the pain of the five rules I mentioned above is completely and totally eliminated. ([View Highlight](https://read.readwise.io/read/01jj3x0n2sdzw2tznfnp8z45bg))



----
📂 [[Articles]] | Последнее изменение: 21.01.2025 10:44