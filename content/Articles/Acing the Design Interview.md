![rw-book-cover](https://readwise-assets.s3.amazonaws.com/static/images/article1.be68295a7e40.png)

## Metadata
- Author: [[seangoedecke.com]]
- Full Title: Acing the Design Interview
- Category: #articles
- Document Tags: [[development]] [[interview]] [[outline]] [[Outline]] 
- Summary: In a design interview, focus on brainstorming system entities and their relationships rather than jumping to technical details. Be prepared to discuss trade-offs in your design choices and adapt based on the interviewers' guidance. Asking questions about operational constraints and the tech stack can help shape a more effective design.
- URL: https://www.seangoedecke.com/acing-the-design-interview/

## Highlights
- The first step is to identify the actual pieces that will go into your system. This is effectively brainstorming: don’t worry about what’s going to be a database table or a class or service, just write down the entities that your system will support. For our journal app, this might be: journal, user, post, comment, reply, mood. ([View Highlight](https://read.readwise.io/read/01jjv46mvraj3s9cvzbgrdbrs7))

- Once you’ve got that list, start another list next to it with what data will go into each record. For a relational database like MySQL, this would be the columns of each table. ([View Highlight](https://read.readwise.io/read/01jjv46tvcpysh8h5ygkjye0e8))

- Once you’ve got some idea of what your data model looks like, it’s time to think about data flows. These are actions that your app or service will be asked to do by its users. ([View Highlight](https://read.readwise.io/read/01jjv477xmga2gbbpcy3gzvgg8))

- Flesh out how each of these will work in practice against the data model you’ve laid out already. ([View Highlight](https://read.readwise.io/read/01jjv48vadsvvvn2fgdj4e91rz))

- Outside of an interview, you ought to begin with a flurry of questions about what tech stack the company uses, what infrastructure is most easily supported for its services, what kind of interoperability or communications protocol works best with existing services, which stakeholders you’d need to collaborate on the design with, and so on. ([View Highlight](https://read.readwise.io/read/01jjv4c0pb7ffwhwca4rwp8swq))

- You should ask about operational constraints: uptime, speed and scale. A journal website that needs to scale to a hundred thousand concurrent users is different from one that needs to only support a few hundred. Likewise, requiring three or more nines of uptime or sub-50ms latency will impose strict restrictions on your design. If you are posed tough operational requirements, it’s worth asking about graceful degradation. Is it OK for posting new journal entries to sometimes fail, as long as reading journal entries always succeeds? Is it OK for a list of comments to be a minute or two out of date if that means we can make reading comments blazing fast? The answer to these questions can dramatically change the appropriate design. ([View Highlight](https://read.readwise.io/read/01jjv4dqv5d08my8a32gxyhgvq))

- Start simple, with a monolithic design, but watch for signs that your interviewers are really looking for a service split. If not, proceed to the next steps - there’s plenty of other ground to cover. ([View Highlight](https://read.readwise.io/read/01jjv4h046es1z27a7cjkmyc26))

- If you do get asked to split up your monolith, try to keep it straightforwardly linked to your data model. Have each service own its associated data: if you have a `UserService`, that should be the only service reading the `users` table. All other services that need user data should communicate with the `UserService` over the network. To enforce this, typically each service will have a database all to itself. Your service model will end up looking a lot like your data model, with lines between the boxes that represent network calls instead of foreign key relationships. ([View Highlight](https://read.readwise.io/read/01jjv4hxy22nm144gcz8e993gk))

- Be ready to give a list of tradeoffs for and against splitting up the monolith. Keeping it together allows for faster development, removes the need to synchronise deploys or database migrations, allows multi-table writes to happen in an atomic database transaction, and removes the potential failure point of internal network calls. Splitting it up allows for easier distribution of the app between multiple teams, allows crucial or performance-sensitive components to be written in different languages or technologies, and potentially makes it easier to horizontally scale your app (since each individual service can be scaled independently to meet its needs). ([View Highlight](https://read.readwise.io/read/01jjv4jy2m15sd65h9wfa1yryy))

- Once you’ve got a sense of the problem, it’s time to lay out some technology choices. ([View Highlight](https://read.readwise.io/read/01jjv59jvdp3svbnhsgdetn1we))

- When it comes to services, you typically want to choose languages and technologies that naturally fit the operational constraints. If the goal is sub-second latency, dynamic languages like Ruby and Python can provide that and make writing code quicker. However, if the goal is too keep latency under 50ms, a naturally faster server-side language like Golang or Java might be a better fit. Of course it is possible to keep Ruby or Python services that fast, with a little effort. The point here is to convey to your interviewers that you’re not a technology zealot and will happily choose the best tool for the job, whatever it may be. If you know what languages your team or company is using, it is a good idea to use those in your examples to make it abundantly clear that you won’t come in demanding to rewrite everything in Haskell (or whatever). ([View Highlight](https://read.readwise.io/read/01jjv5b20ds9hmffz4b5y12qx4))

- An app running in production is almost never a single service connected to a data store, particularly if scaling is a concern. It is generally a complex distributed system. Even if the application itself is a monolith, it needs read-replicas of its data store, layers of caching, queues and workers, streams, CDNs, and so on. You should familiarise yourself with the point of these components so you can deploy them in your design where appropriate. ([View Highlight](https://read.readwise.io/read/01jjv5bysy8qjy856z6pqx302s))

- Your interviewers will probably not ask you to put in a cache or a queue. Instead, with that solution in mind, they will ask you to make a particular operation faster or more reliable in your current design, and you will be expected to come up with the solution on your own. ([View Highlight](https://read.readwise.io/read/01jjv5chqcvxznpe3d269hdvxt))

- A read-replica of a data store is a separate database, automatically kept up to date by the db technology, that can only handle read requests. Writes must (typically) still go to a single writer node to prevent conflicts. ([View Highlight](https://read.readwise.io/read/01jjv5e4pdsn4vzp37hnn8mv5x))

- A cache is a separate data store held entirely in memory. It is much faster than a proper database, but does not persist data (so nothing can be permanently written there). This can be a separate service on the network (memcached, redis), or a component of the application itself running in the actual server process. ([View Highlight](https://read.readwise.io/read/01jjv5endmzb1pn37gmnrzfh4h))

- Queues and workers are typically used to farm out expensive tasks. Instead of doing a task (like sending an email) immediately, your service can make a request to put an item in the queue (which, much like a cache, is effectively another data store). ([View Highlight](https://read.readwise.io/read/01jjv5fkgn03mcsgz8tk7detkj))



----
📂 [[Articles]] | Последнее изменение: 30.01.2025 13:52