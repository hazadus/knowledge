# Unexpected python traps for beginners - Bite code!

![rw-book-cover](https://substackcdn.com/image/fetch/f_auto,q_auto:best,fl_progressive:steep/https%3A%2F%2Fbitecode.substack.com%2Ftwitter%2Fsubscribe-card.jpg%3Fv%3D1150877578%26version%3D9)

## Metadata
- Author: [[Bite Code!]]
- Full Title: Unexpected python traps for beginners - Bite code!
- Category: #articles
- Document Tags: [[python]] 
- Summary: The document highlights common traps beginners may encounter when coding in Python. It discusses issues like string concatenation, the difference between returning values in functions, the peculiarities of tuples, and the misconceptions around using "is" for equality comparisons. It also addresses pitfalls related to mutable default values in functions and class attributes, providing insights on how to avoid these traps. The article emphasizes the importance of understanding Python's unique features to prevent unexpected errors and behavior in code.
- URL: https://www.bitecode.dev/p/unexpected-python-traps-for-beginners

## Highlights
- No, Python didn't magically apply the `+1` to all lists. It's just that when you do `*3`, you don't create a tuple of 3 lists. You create a tuple of 3 references, each of them to the same single list. It's the same list 3 times, but referenced in 3 difference places in the tuple. There is only one list, so when you modify it, you see it modified, and it's in 3 places, so you see it 3 times. ([View Highlight](https://read.readwise.io/read/01jdc0dh3wc24ygsxtwph53zkp))

- zeros = tuple([0] for _ in range(3)) ([View Highlight](https://read.readwise.io/read/01jdc0dhdqnkaz08ygb6cfznh5))



----
📂 [[Articles]] | Последнее изменение: 23.11.2024 16:34