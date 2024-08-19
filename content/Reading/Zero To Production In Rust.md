## Zero To Production In Rust

### Luca Palmieri · Independently Published · 2022 г. · 433 с.

#book #programming #Rust 

[[Books Reading]] | [[Rust]]

http://library.hazadus.ru/books/45/details/

> [!abstract]
> _Zero To Production_ is the ideal starting point for your journey as a Rust backend developer. You will learn by doing: you will build a fully functional email newsletter API, starting from scratch.
>
You'll learn how to:
>
>- Navigate and leverage Rust's crates ecosystem
>- Structure your application to make it modular and extensible
>- Write tests, from single units to full-blown integration tests
>- Enforce your domain invariants using Rust's type system
>- Authenticate and authorize users of your API
>- Implement a robust error handling strategy
>- Observe the state of your application using structured logs
>- Set up an extensive continuous integration and continuous deployment pipeline for your Rust projects
>
All code comes attached to the book, tests included.
>
[Сайт книги](https://www.zero2prod.com/index.html)
> https://www.lpalmieri.com/about/

----

Load balancing relies on a strong assumption: no matter which backend is used to serve an incoming request, the outcome will be the same.

That’s why load balancing works: all backends are talking to the same database to query and manipulate the same **state**.

Think of a database as a single gigantic global variable. Continuously accessed and mutated by all replicas of our application.

---

Deployments _(p.214)_

- [BlueGreenDeployment](https://martinfowler.com/bliki/BlueGreenDeployment.html)
- [CanaryRelease](https://martinfowler.com/bliki/CanaryRelease.html)

----

Type-driven development (p.139)
- [Parse, don't validate](https://lexi-lambda.github.io/blog/2019/11/05/parse-don-t-validate/)
- [Domain Modeling Made Functional](https://pragprog.com/titles/swdddf/domain-modeling-made-functional/) by Scott Wlaschin

---

P.46

- https://gist.github.com/LukeMathWalker/5ae1107432ce283310c3e601fac915f3
- https://www.lpalmieri.com/posts/2020-07-04-choosing-a-rust-web-framework-2020-edition/
- https://actix.rs/
- https://docs.rs/actix-web/4.0.1/actix_web/index.html
- https://github.com/actix/examples
- https://cfsamson.github.io/books-futures-explained/introduction.html

----


----
📂 [[Reading]] | Последнее изменение: 06.12.2023 15:34