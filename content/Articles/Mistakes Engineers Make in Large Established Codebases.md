![rw-book-cover](https://readwise-assets.s3.amazonaws.com/static/images/article0.00998d930354.png)

## Metadata
- Author: [[seangoedecke.com]]
- Full Title: Mistakes Engineers Make in Large Established Codebases
- Category: #articles
- Document Tags: [[development]] [[Development]] [[outline]] [[Outline]] 
- Summary: Working in large established codebases is challenging, and the biggest mistake engineers make is ignoring consistency with existing code. It's crucial to follow existing patterns to avoid surprises and maintain the codebase's integrity. Understanding the codebase and its production impact is essential for successful feature implementation and long-term improvements.
- URL: https://www.seangoedecke.com/large-established-codebases/?utm_source=christophberger&utm_medium=email&utm_campaign=2025-01-05-unfamiliar

## Highlights
- Working in large established codebases is one of the hardest things to learn as a software engineer. You can’t practice it beforehand (no, open source does not give you the same experience). Personal projects can never teach you how to do it, because they’re necessarily small and from-scratch. ([View Highlight](https://read.readwise.io/read/01jj1cwzdnhr4dhejzdtbjayt2))

- There’s one mistake I see more often than anything else, and it’s absolutely deadly: ignoring the rest of the codebase and just implementing your feature in the most sensible way. ([View Highlight](https://read.readwise.io/read/01jj1cx8b430z0753p36rt33my))

- In fact, you must sink as deeply into the legacy codebase as possible, **in order to maintain consistency.** ([View Highlight](https://read.readwise.io/read/01jj1cxeg5herr6zv652fdj0zt))

- You must resist the urge to make your little corner of the codebase nicer than the rest of it. ([View Highlight](https://read.readwise.io/read/01jj1cxjrmg497nv6cffa1yhb4))

- On top of that, lack of consistency is the primary long-term killer of large codebases, because it makes it impossible to make any general improvements. ([View Highlight](https://read.readwise.io/read/01jj1czz2e0nqtx0kbbmass8ry))

- So when you sit down to implement anything in a large codebase, you should always first go and look around for prior art, and follow that if at all possible. ([View Highlight](https://read.readwise.io/read/01jj1d1hs59gzn9bv7cxbn393q))

- **you cannot split up a large established codebase without first understanding it**. I have seen large codebases successfully split up, but I have never seen that done by a team that wasn’t already fluent at shipping features inside the large codebase. ([View Highlight](https://read.readwise.io/read/01jj1d91pes374eg8d3d4nc1km))

- Summary
  • Large codebases are worth working in because they usually pay your salary
  • By far the most important thing is consistency
  • Never start a feature without first researching prior art in the codebase
  • If you don’t follow existing patterns, you better have a very good reason for it
  • Understand the production footprint of the codebase
  • Don’t expect to be able to test every case - instead, rely on monitoring
  • Remove code any chance you get, but be very careful about it
  • Make it as easy as possible for domain experts to catch your mistakes ([View Highlight](https://read.readwise.io/read/01jj1da4pc0ws5cphh8xshrktd))



----
📂 [[Articles]] | Последнее изменение: 20.01.2025 11:31