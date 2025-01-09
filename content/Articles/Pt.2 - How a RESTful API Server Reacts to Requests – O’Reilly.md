# Pt.2 - How a RESTful API Server Reacts to Requests – O’Reilly

![rw-book-cover](https://www.oreilly.com/content/wp-content/uploads/sites/2/2019/06/light-traces-2985871_1920-0b0b64dd0f932b0620f6491448cadccd.jpg)

## Metadata
- Author: [[Filipe Ximenes, Flávio Juvenal]]
- Full Title: Pt.2 - How a RESTful API Server Reacts to Requests – O’Reilly
- Category: #articles
- Document Tags: [[api]] [[auth]] [[caching]] [[cors]] [[favorite]] [[rest]] 
- Summary: Learn how to properly design RESTful APIs communication with clients, accounting for request structure, authentication, and caching.
- URL: https://www.oreilly.com/content/how-a-restful-api-server-reacts-to-requests/

## Highlights
- Since we already defined URLs and methods for our API, we can now discuss what success means for each URL/method combination. It’s important to properly define success conditions to allow API clients to communicate success in their interfaces to their end users. Ever interacted with a web or mobile app that didn’t properly inform you whether the operation you had just made worked or not? It’s quite awful, forcing you to find another way to check, like refreshing the page, closing and reopening the app, or even contacting support! Even worse, there are apps out there that don’t show any error, but actually didn’t save your changes. This is probably because their APIs don’t properly inform them of the success conditions, or return a 200 OK even for wrong inputs. ([View Highlight](https://read.readwise.io/read/01jdc0f95a7e3kq9ef5m0epsrm))

- ### GET /rents/ (User sees the history of rents) ([View Highlight](https://read.readwise.io/read/01jdc0f9bq1m2r4b0wpy3ar7nv))

- ### POST /rents/ (User rents a bike) ([View Highlight](https://read.readwise.io/read/01jdc0f9jj509paa6a33tybvns))

- If a user tries to PUT a rent that belongs to another user, the API should return **404 Not Found**. It’s more secure than 403 Forbidden because it avoids the disclosure of existing rent ids from other users. If we returned Forbidden instead of Not Found, an attacker would know there’s some rent with that ID, and might be able to do some mischief with that information. In APIs, there’s no advantage in disclosing which resources belong to which users, so let’s “pretend” the requested resource doesn’t exist with a 404, as it doesn’t belong to the requesting user. We’ll talk more about this in the Authentication section. Intuitively, 404 is the appropriate status code if the rent ID in the URL is invalid or nonexistent, too. ([View Highlight](https://read.readwise.io/read/01jdc0f9vctdeaphhvdrzfk6js))

- In the context of HTTP, safety means that a given request will not produce any changes in the server state. GET is the main safe method in HTTP. Correct implementations of GET requests, as in our bike rental API, don’t have side effects. Secondary effects like logging or throttling are fine, but in general the server shouldn’t change any resources after handling a GET request. Therefore, it’s perfectly safe to retry GET requests if the client somehow lost track of the server state. ([View Highlight](https://read.readwise.io/read/01jdc0f9z8wdp645a62d9fb3aq))

- On the other hand, idempotency means the resource state doesn’t change after subsequent requests, i.e., a first request can change something, but the following requests will change nothing. This means the request can be replayed any number of times without introducing new changes in the resource. DELETE is the easiest method to understand when we think about idempotency. The first time you make a DELETE `/rents/123/` request, you change the rent state by cancelling it. But subsequent DELETE requests to the same `/rents/123/` resource won’t change it, since it was already cancelled[1](#dfref-footnote-1). It’s like multiplying by 0\. Everything that’s safe is also idempotent, but opposite isn’t true. ([View Highlight](https://read.readwise.io/read/01jdc0fa52v4nb21nt3yqfsvng))

- A counterexample of safety and idempotency is the POST method for creating resources. If you make repeated POST requests to the same URL, you’ll create multiple resources. You change the server state after every request, so there’s no safety nor idempotency here. If the client connection with the API server is interrupted in the middle of a POST request, it’s always good to check the server state with a GET before making another POST. ([View Highlight](https://read.readwise.io/read/01jdc0fa8nbygdh54pf2ncq238))

- There are many ways to authenticate a user in an RESTful HTTP API. We will introduce the most popular stateless authentication methods to help you chose the one that best suits your application. The **stateless** concept is important for a truly RESTful Authentication, because REST demands stateless communication between client and server, i.e., “each request from client to server must contain all of the information necessary to understand the request.”[3](#dfref-footnote-3) If you have server-side sessions holding state about the user, you’re not doing stateless authentication. Commonly, cookie-based authentication methods hold state information. They are not RESTful. ([View Highlight](https://read.readwise.io/read/01jdc0faee33jnjj11fp887ck8))

- It’s important to note that, regardless of your choice, you should **not** roll your own authentication protocol. A secure authentication scheme requires expert knowledge in cryptography algorithms. Also, there are tons of edge cases that can pass unnoticed by an inexperienced programmer. ([View Highlight](https://read.readwise.io/read/01jdc0faj5yxes8nncn25v4kg5))

- Basic Authentication is the simplest stateless authentication scheme that can be implemented in HTTP. The client authenticates users by including an `Authorization` header with credentials on requests. The credentials are computed by joining the username and password with a colon (:) and encoding the result with base64\. The result will be something like: `Authorization: Basic dXNlcm5hbWU6cGFzc3dvcmQ=` ([View Highlight](https://read.readwise.io/read/01jdc0faqt8tamte42de0e47wj))

- Using Basic Auth with HTTPS is fine for simple or private APIs. However, other authentication methods are preferable for public APIs, like our bike rental API example. Other methods support useful functionalities such as credential rotation or using tokens instead of passwords after the first authentication request, which are useful to increase security in real-world production-level apps. ([View Highlight](https://read.readwise.io/read/01jdc0faxj0gahe354xckya27f))

- Usually, APIs that support Token Authentication have a “sign in” URL that accepts a POST request with username and password and responds with a token. A token is simply a string, usually randomly or cryptographically generated. Subsequent requests should use the token instead of the username and password, typically in the form of a header like `Authorization: Token t$IKL&qNhTfx0pr$`. The token is mapped to the user in the server, generally in a database table. ([View Highlight](https://read.readwise.io/read/01jdc0fb19d64e2nd0pye0ks37))

- The advantage of Token Authentication over Basic Authentication is that it decouples the authorization from the password, thereby supporting the following functionalities: ([View Highlight](https://read.readwise.io/read/01jdc0fb73wqx1pcj7b43ppjcc))

- The encoded JWT looks like a random string, a opaque token. However, it actually holds data. Decoding the JWT above, we have the following JSON payload: ([View Highlight](https://read.readwise.io/read/01jdc0fbh1xad7dd1sqrgem88p))

- You may ask: is this really safe? Can’t the client side change the payload and authenticate as another user or become an admin?. Yes it’s safe, and no, the client can’t change the payload. If they change the payload, the token can be recognized on the server side as false. The reason is that the JWT payload is cryptographically signed by the server, meaning it can’t be tampered with. This may sound a bit magical if you don’t know much about cryptography, but that’s the beauty of JWT. It can pass authentication information back and forth safely.[6](#dfref-footnote-6) ([View Highlight](https://read.readwise.io/read/01jdc0fbtdd4pa0y1nw73ackxp))

- On browsers, there’s something called _same-origin policy_ that restricts how a document or script loaded from one origin can interact with a resource from another origin. Origin here means the protocol, port, and host of a URL. If there were no same-origin policy, when you visited hack-me.com, it could make an AJAX request from your browser to your-bank.com and impersonate you using your cookies, since the request is coming from your browser! ([View Highlight](https://read.readwise.io/read/01jdc0fc37xfjj9jqzcz5z6kat))

- However, the stateless authentication methods we’ve discussed don’t use cookies. If no cookies are involved in the authentication, you can safely enable cross-origin requests in your API using **CORS** (Cross-Origin Resource Sharing). Public APIs are made to allow integration with external services, so enabling all origins access is part of their nature. Check for your web framework documentation on how to enable CORS. But remember: don’t enable CORS for all origins if you’re using any cookie-based authentication in your website. Also, if you have both a website version and a API-based version of a service, a good idea is to host them in different subdomains or domains. The website should keep same-origin policy active, while the API can have CORS enabled. ([View Highlight](https://read.readwise.io/read/01jdc0fc6zsw11brz2816tzvtb))

- ### Caching with max-age ([View Highlight](https://read.readwise.io/read/01jdc0fccxvs3rchnb5j1qwdw0))

- ### Caching with ETag ([View Highlight](https://read.readwise.io/read/01jdc0fcp26j4csf0v5xmtwpp1))

- ## Optimistic Locking ([View Highlight](https://read.readwise.io/read/01jdc0fcz65hhggx624dgc2yps))

- It’s worth noting that JWT does **not** encrypt its payload. It does not hide or obscure the payload. The client **can** read the payload. It can’t change it, though. ([View Highlight](https://read.readwise.io/read/01jdc0fd8tyaz2ewtk773g6qf5))



----
📂 [[Articles]] | Последнее изменение: 23.11.2024 16:34