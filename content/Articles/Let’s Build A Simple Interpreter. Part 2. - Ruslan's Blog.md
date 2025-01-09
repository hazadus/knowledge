# Let’s Build A Simple Interpreter. Part 2. - Ruslan's Blog

![rw-book-cover](https://readwise-assets.s3.amazonaws.com/static/images/article4.6bc1851654a0.png)

## Metadata
- Author: [[Ruslan Spivak]]
- Full Title: Let’s Build A Simple Interpreter. Part 2. - Ruslan's Blog
- Category: #articles
- Document Tags: [[diy]] 
- Summary: The article discusses the importance of mastering simple concepts in music and software development, emphasizing that understanding basic principles leads to greater skill. It introduces an updated calculator interpreter that can handle whitespace, multi-digit integers, and both addition and subtraction. The text highlights the roles of tokens, lexemes, and parsing in interpreting arithmetic expressions, while also suggesting exercises to extend the calculator's capabilities.
- URL: https://ruslanspivak.com/lsbasi-part2/

## Highlights
- In their amazing book “The 5 Elements of Effective Thinking” the authors Burger and Starbird share a story about how they observed Tony Plog, an internationally acclaimed trumpet virtuoso, conduct a master class for accomplished trumpet players. The students first played complex music phrases, which they played perfectly well. But then they were asked to play very basic, simple notes. When they played the notes, the notes sounded childish compared to the previously played complex phrases. After they finished playing, the master teacher also played the same notes, but when he played them, they did not sound childish. The difference was stunning. Tony explained that mastering the performance of simple notes allows one to play complex pieces with greater control. The lesson was clear - to build true virtuosity one must focus on mastering simple, basic ideas.[1](#fn-1) ([View Highlight](https://read.readwise.io/read/01jdc0cvv7pgdqxb0knkmn93rf))

- While it is important to be proficient with a tool or framework you use, it is also extremely important to know the principles behind them. As Ralph Waldo Emerson said: ([View Highlight](https://read.readwise.io/read/01jdc0cw48czjqde5hxkythz0p))

- _“If you learn only methods, you’ll be tied to your methods. But if you learn principles, you can devise your own methods.”_ ([View Highlight](https://read.readwise.io/read/01jdc0cwdbp9msn592d4wsvs4v))

- A **lexeme** is a sequence of characters that form a token. ([View Highlight](https://read.readwise.io/read/01jdc0cwgwvw5j2rfrj6p7mrp7))

- That’s what the _expr_ method essentially does: it finds the structure in the stream of tokens it gets from the _get\_next\_token_ method and then it interprets the phrase that is has recognized, generating the result of the arithmetic expression. ([View Highlight](https://read.readwise.io/read/01jdc0cwm8qk6v20p8ct5dbesc))

- The process of finding the structure in the stream of tokens, or put differently, the process of recognizing a phrase in the stream of tokens is called **parsing**. The part of an interpreter or compiler that performs that job is called a **parser**. ([View Highlight](https://read.readwise.io/read/01jdc0cwt48g8hc5hthwb37c86))



----
📂 [[Articles]] | Последнее изменение: 23.11.2024 16:34