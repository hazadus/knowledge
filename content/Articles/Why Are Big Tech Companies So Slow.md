![rw-book-cover](https://readwise-assets.s3.amazonaws.com/static/images/article0.00998d930354.png)

## Metadata
- Author: [[seangoedecke.com]]
- Full Title: Why Are Big Tech Companies So Slow?
- Category: #articles
- Document Note: Учесть при разработке проектов: чем больше накапливается фич, тем сложнее и дольше реализовывать последующие фичи.
- Document Tags: [[leaddev]] [[LeadDev]] [[outline]] [[Outline]] 
- Summary: Big tech companies are slow because they have many features that interact with each other, making it complex to build and ship new ones. This complexity creates a high cognitive load for engineers, who must balance these features carefully. While some may think big tech engineers are incompetent, the reality is that adding features for profit makes the development process much more challenging.
- URL: https://www.seangoedecke.com/difficulty-in-big-tech/

## Highlights
- So why do big tech companies find it so much harder to build? It’s the scale of the app itself: not the number of traffic or users, but the number of *features*. As that number grows, it becomes more and more difficult to build and ship new features. The reason is straightforwardly mathematical. Each new feature potentially interacts with all the features before it. You have to check to make sure it doesn’t interfere with an existing feature, and if it does, you have make some kind of balancing change to keep both features working. ([View Highlight](https://read.readwise.io/read/01jjp90s05sbyxse79spyvea5k))

- To someone without a lot of big tech experience, this can look like a problem with the codebase. It just seems so awkward and complicated - if it were correctly factored, all of this would be so much easier. But this is an error. First, you’ll never get around the mathematics of adding new features, no matter how nice the code is. Second, big tech codebases are awkward *because* balancing features is difficult, not the other way around. An ungainly big tech codebase is the agglomeration of millions of small feature-balancing decisions (i.e. edge cases) over many years. That’s where all the value comes from! You can build any of the individual features in a weekend. But the next feature will take four days, and the one after that a whole week, and pretty soon you’ll be operating at the speed of big tech. ([View Highlight](https://read.readwise.io/read/01jjp9z96nfbtn00fyhtv746kz))
    - Note: В дополнение: размеры кодовой базы тоже дадут о себе знать. См. например Симана, который пишет, что однажды разработчик ему сказал - ему понадобилось три месяца подготовки, прежде чем начать вносить изменения в legacy code base.

- Much of the complexity is produced by a small set of what I call “wicked features”, which interfere with *every other* feature. For instance, adding a whole new user type: once you do that, you have to ask “can this user type access this feature” for every feature for the rest of the company’s life. ([View Highlight](https://read.readwise.io/read/01jjpa2htpygr421xt6a6htd42))



----
📂 [[Articles]] | Последнее изменение: 28.01.2025 18:44