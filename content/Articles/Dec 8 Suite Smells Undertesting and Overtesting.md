# Dec 8 Suite Smells: Undertesting and Overtesting

![rw-book-cover](http://static1.squarespace.com/static/5e10bdc20efb8f0d169f85f9/5e949913434baa2223121b85/67235ab71afdf1290f8f21fa/1733678014950/bug.png?format=1500w)

## Metadata
- Author: [[John Arundel]]
- Full Title: Dec 8 Suite Smells: Undertesting and Overtesting
- Category: #articles
- Document Tags: [[go]] [[Outline]] [[testing]] 
- Summary: The author discusses the importance of testing not just if code works, but also ensuring it doesn't produce unwanted results. He highlights that tests should check both preconditions and postconditions to avoid misleading outcomes. Additionally, he warns against overtesting, which can make tests unnecessarily complex and fragile.
- URL: https://bitfieldconsulting.com/posts/undertesting-overtesting

## Highlights
- Even when a certain piece of code is nominally *covered* by some test, is it really tested? That’s not always a given. In other words, just because a test causes some function to be executed, that doesn’t mean it shows that the function *does* the right thing. ([View Highlight](https://read.readwise.io/read/01jex9kpb2dmebdp8sn7sm8p15))

- It’s always worth asking of any test whether it rigorously checks its *preconditions* as well as its postconditions. The developer’s focus, naturally enough, tends to be on the state of the world *after* the operation under test, but that can result in some risky assumptions about its *prior* state. ([View Highlight](https://read.readwise.io/read/01jex9t0wghteejm6k3r3pea64))

- We need to pay attention to preconditions as well as postconditions, according to the contract that the system under test is supposed to fulfil. ([View Highlight](https://read.readwise.io/read/01jex9vma0h9jzktfbft6hxd8a))

- In any non-trivial codebase, you’re pretty much guaranteed to find at least a few tests that are optimistically feeble in this way. Look for any test that doesn’t properly establish its preconditions, and fix it. This will add a lot of value to the test suite overall. ([View Highlight](https://read.readwise.io/read/01jex9y3ta5d1c0xpt9p51x8wf))

- We create *two* users in the test, but delete only one of them. Then we check that the one we deleted doesn’t exist, and the one we didn’t delete still exists ([View Highlight](https://read.readwise.io/read/01jexa20qs2wrvy2cwk9ay336c))





----
📂 [[Articles]] | Последнее изменение: 19.12.2024 14:22