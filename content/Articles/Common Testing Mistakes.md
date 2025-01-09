# Common Testing Mistakes

![rw-book-cover](https://kentcdodds.com/static/d6c0c04e06b7423b8f70aad624ec2318/7e402/banner.jpg)

## Metadata
- Author: [[kentcdodds.com]]
- Full Title: Common Testing Mistakes
- Category: #articles
- Document Tags: [[testing]] 
- Summary: The text discusses common testing mistakes, such as testing implementation details and aiming for 100% code coverage, which may not necessarily increase confidence in the codebase. The author emphasizes the importance of writing tests that focus on critical parts of the application to ensure confidence, rather than just increasing code coverage. Additionally, the text highlights the need for efficient end-to-end testing strategies to enhance test reliability and speed.
- URL: https://kentcdodds.com/blog/common-testing-mistakes

## Highlights
- Mistake Number 1: Testing Implementation Details ([View Highlight](https://read.readwise.io/read/01jdc0dr4phe0qws1kerdn9x6r))

- Mistake Number 2: 100% code coverage ([View Highlight](https://read.readwise.io/read/01jdc0dr8g5p17pebkwaqqrwex))

- What code coverage is telling you: ([View Highlight](https://read.readwise.io/read/01jdc0dreay8x9a73d1tjj5tmz))

- Mistake Number 3: Repeat Testing ([View Highlight](https://read.readwise.io/read/01jdc0drv2wffj0w5gh3cvs5br))

- I mean, we already established that your tests should work in isolation so you shouldn't be sharing a user between them. Here's what you do: make the same HTTP calls in your tests that your application makes when you register and log in a new user! Those requests will be MUCH faster than clicking and typing around the page and there's less of a chance for false negative failures. And as long as you keep one test around that actually _does_test the registration/login flow you haven't lost any confidence that this flow works. ([View Highlight](https://read.readwise.io/read/01jdc0ds0qzg1mz1wk0gbpxr1m))



----
📂 [[Articles]] | Последнее изменение: 23.11.2024 16:34