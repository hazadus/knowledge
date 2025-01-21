
- Working in large established codebases is one of the hardest things to learn as a software engineer. You can’t practice it beforehand (no, open source does not give you the same experience). Personal projects can never teach you how to do it, because they’re necessarily small and from-scratch.

- There’s one mistake I see more often than anything else, and it’s absolutely deadly: ignoring the rest of the codebase and just implementing your feature in the most sensible way. 

- In fact, you must sink as deeply into the legacy codebase as possible, **in order to maintain consistency.** 

- You must resist the urge to make your little corner of the codebase nicer than the rest of it. 

- On top of that, lack of consistency is the primary long-term killer of large codebases, because it makes it impossible to make any general improvements. 

- So when you sit down to implement anything in a large codebase, you should always first go and look around for prior art, and follow that if at all possible. 

- **you cannot split up a large established codebase without first understanding it**. I have seen large codebases successfully split up, but I have never seen that done by a team that wasn’t already fluent at shipping features inside the large codebase. 

- Summary
  • Large codebases are worth working in because they usually pay your salary
  • By far the most important thing is consistency
  • Never start a feature without first researching prior art in the codebase
  • If you don’t follow existing patterns, you better have a very good reason for it
  • Understand the production footprint of the codebase
  • Don’t expect to be able to test every case - instead, rely on monitoring
  • Remove code any chance you get, but be very careful about it
  • Make it as easy as possible for domain experts to catch your mistakes 

## References

-  https://www.seangoedecke.com/large-established-codebases
	- [[Mistakes Engineers Make in Large Established Codebases]]

----
📂 [[Misc]] | Последнее изменение: 20.01.2025 11:33