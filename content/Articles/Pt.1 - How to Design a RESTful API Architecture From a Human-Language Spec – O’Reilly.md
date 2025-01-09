# Pt.1 - How to Design a RESTful API Architecture From a Human-Language Spec – O’Reilly

![rw-book-cover](https://www.oreilly.com/content/wp-content/uploads/sites/2/2019/06/sofia-84149_1920-c058368844e886c110d0ff26496f77f4.jpg)

## Metadata
- Author: [[Filipe Ximenes, Flávio Juvenal]]
- Full Title: Pt.1 - How to Design a RESTful API Architecture From a Human-Language Spec – O’Reilly
- Category: #articles
- Document Tags: [[api]] [[rest]] 
- Summary: A process to build RESTful APIs that solve users’ needs with simplicity, reliability, and performance.
- URL: https://www.oreilly.com/content/how-to-design-a-restful-api-architecture-from-a-human-language-spec/

## Highlights
- Although many programmers release uncreative APIs that merely expose database functions (the well-known CRUD operations of Create, Read, Update, Delete), useful APIs go beyond that and reflect the functions requested by the user, such as Reserve or Buy. They offer terms and processes that are intuitive to the programmer at the other end—including meaningful error status messages—and are structured to maximize efficiency. ([View Highlight](https://read.readwise.io/read/01jdc0fn2txy6f0c8dz3wy2ds3))

- The process for you’ll learn in this article for designing a RESTful HTTP API architecture has two steps: ([View Highlight](https://read.readwise.io/read/01jdc0fn6s9dwgsw3es0mt7cbc))

- Let’s review a few key concepts of RESTful APIs as we start reasoning about our own application. First of all, we need to think about the basic elements used in REST: ([View Highlight](https://read.readwise.io/read/01jdc0fnfp0rcd6z93hm76nrky))

- It’s important to understand that REST is not a protocol, but an architectural style. It’s a set of rules and guidelines that define how a system should function. REST is not limited to HTTP, but in practice, when people talk about RESTful APIs, they are likely talking about APIs using the HTTP protocol. ([View Highlight](https://read.readwise.io/read/01jdc0fnp5yybx99pgpmma1e1a))

- One of the main authors of HTTP is also the creator of REST. No wonder HTTP has parts that fit very well to these REST basic elements: ([View Highlight](https://read.readwise.io/read/01jdc0fnw0vr3jrmhw6k03wcbf))

- Thus, to properly design our RESTful API we need to know really well the meaning of each HTTP _method_. What are the semantics behind each method? How should we use them? Let’s see: ([View Highlight](https://read.readwise.io/read/01jdc0fp2wsd13rg7wbb8mtqas))

- Besides that, we also need to care about _which_ data from resources will be included in request and response bodies. For example, on a POST request for creation, the body needs to include the resource representation to be created. Another example, a GET response body needs to contain a resource representation, but a DELETE response body does not. ([View Highlight](https://read.readwise.io/read/01jdc0fpc4c8a1tzykqsp68yby))

- Summarizing, here’s what we need to answer here to design our API: ([View Highlight](https://read.readwise.io/read/01jdc0fphxpsvj1nmn4shqg6ge))

- **Which HTTP method maps to “Rent”?** ([View Highlight](https://read.readwise.io/read/01jdc0fprf44erdd0adwq74sev))

- There is also another HTTP method used for updates: PATCH. We omitted it because it’s not often used and when it is, it’s used wrongly. A PATCH request should contain in its body the instructions to change a server resource. In other words, it carries a representation of changes to be applied at the resource, not the whole updated resource itself, like in PUT. That’s the difference between them. Those different representations reflect the difference between a partial and a full update. Most RESTful APIs accept both partial and full updates in PUT, with the representation being the resource, not the changes to the applied on it. That’s why PUT is more common than PATCH. ([View Highlight](https://read.readwise.io/read/01jdc0fpycs9g72he4fzkr8twe))

- We’ve seen that REST is made of resources, representations, and actions. We’ve also seen that resources are like nouns and actions are like verbs. So, identifying the nouns and verbs available at a system spec is a good way to start our spec to API process. ([View Highlight](https://read.readwise.io/read/01jdc0fq2yzngrhdgqc7re0v01))



----
📂 [[Articles]] | Последнее изменение: 23.11.2024 16:34