# Pt.3 - How a RESTful API Represents Resources – O’Reilly

![rw-book-cover](https://www.oreilly.com/content/wp-content/uploads/sites/2/2019/06/confluence-2467774_1920-8b6a84c42827ec170551f75deea984f7.jpg)

## Metadata
- Author: [[Filipe Ximenes, Flávio Juvenal]]
- Full Title: Pt.3 - How a RESTful API Represents Resources – O’Reilly
- Category: #articles
- Document Tags: [[api]] [[rest]] [[versioning]] 
- Summary: Formats, linking, and versioning are important in well-formed RESTful APIs.
- URL: https://www.oreilly.com/content/how-a-restful-api-represents-resources/

## Highlights
- The most RESTful way to support sorting and filtering is using HTTP query parameters on each resource. The sortable/filterable fields must match the names used in resource representations. This is how the resource representation Media Type is related to sorting and filtering. So, when documenting your API Media Type, you must document how it supports sorting and filtering. ([View Highlight](https://read.readwise.io/read/01jdc0f7pp77xy1cy2p2zxvkn3))

- However, there’s a more RESTful alternative. As someone once said, [HTTP is your envelope](https://stackoverflow.com/a/9999335) already. You don’t need to add pagination metadata in the response body, you can use response headers! That’s [what the GitHub API does](https://developer.github.com/v3/#pagination) on its paginated responses. It uses the Link header to hold the pagination links. Updating our example to be like GitHub API responses, we get this: ([View Highlight](https://read.readwise.io/read/01jdc0f7ww52rz3vgwe5av97yk))

- The key point for designing a great representation is to think about what’s best for the API client. Look for the good practices of the Media Type you’re using. Grab inspiration from good APIs like [GitHub](https://developer.github.com/v3/) or [Stripe](https://stripe.com/docs/api). Avoid truncating data from the fields that your API exposes. And link resources to other resources. ([View Highlight](https://read.readwise.io/read/01jdc0f83vg146gwrwyatpcwh1))

- HTTP servers can support multiple Media Types for the same resource. In a request, the client specifies which Media Type it wants for the resource representation to be with the Accept header. You can imagine, then, an API that can respond either with JSON or XML, depending whether the client passed `Accept: application/json` or `Accept: application/xml`. ([View Highlight](https://read.readwise.io/read/01jdc0f895b0gw8yn9kvvz5237))

- If you want your API users to stay happy, try hard to avoid API changes. When updating is inevitable, keep the old versions online for some good amount of time. Regardless of what versioning option you’ll chose, **always launch with a version and ask your API clients to specify it on requests**. This will solve most of the problems of incompatibility, because it will allow you to have multiple versions online and safely launch new versions without breaking old clients. ([View Highlight](https://read.readwise.io/read/01jdc0f8cye3m2n21bqtm8hvqb))

- The most RESTful way to version an API is to version the resource representations. For example, remember the problem we’ve discussed where some APIs don’t use Booleans for true/false fields? Imagine that on the first version of our Bike rental API we had `"is_active": "0"` in our `GET /rents/` response. Then we learned that’s bad, and we decided to change to `"is_active": false`. How should we introduce that change? Ideally with a different Media Type, since the representation changed. To do that properly, we should publish our API from day 1 with a custom Media Type that includes the version, like: `application/vnd.bikerental.v1+json`. Then, our first API clients should use that Media Type on their Accept headers. That’s equivalent of saying “I want data formatted as the Bike rental JSON version 1”. Currently, GitHub API [handles versioning in that way](https://developer.github.com/v3/media/). Afterwards, we can deploy the change to `"is_active": false` and introduce a second Media Type: `application/vnd.bikerental.v2+json`. This allows us to keep both versions for some time and disable the older one once its traffic is minimal. ([View Highlight](https://read.readwise.io/read/01jdc0f8geb6xxskayhq59p8hp))

- The conservative solution would be to keep supporting `DELETE /v1/rents/{id}/` for some time to avoid breaking clients and launch a `/v2/` API without this functionality. ([View Highlight](https://read.readwise.io/read/01jdc0f8nq442jr6yv5vwbb6a9))

- In practice, the most important thing about versioning is to launch with a version, either on the Media Type or the URL, and communicate well with API clients, documenting changes and giving them time to adapt to newer versions by deprecating older versions slowly. Your backend code might become a bit cluttered to support multiple versions online at the same time, but your API clients will be thankful. ([View Highlight](https://read.readwise.io/read/01jdc0f8sbwzfdtcz7hnat3vc3))



----
📂 [[Articles]] | Последнее изменение: 23.11.2024 16:34