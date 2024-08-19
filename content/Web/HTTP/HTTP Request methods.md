🔗 [[HTTP]] / [[HTTP Messages]]

----
HTTP defines a set of **request methods** to indicate the desired action to be performed for a given resource. Although they can also be nouns, these request methods are sometimes referred to as HTTP verbs. Each of them implements a different semantic, but some common features are shared by a group of them: e.g. a request method can be **safe**, **idempotent**, or **cacheable**.

## Safe
An HTTP method is **safe** if it doesn't alter the state of the server. In other words, a method is safe if it leads to a read-only operation. Several common HTTP methods are safe: [`GET`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/GET), [`HEAD`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/HEAD), or [`OPTIONS`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/OPTIONS). All safe methods are also [idempotent](https://developer.mozilla.org/en-US/docs/Glossary/Idempotent), but not all idempotent methods are safe. For example, [`PUT`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/PUT) and [`DELETE`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/DELETE) are both idempotent but unsafe.
## Idempotent
An HTTP method is **idempotent** if the intended effect on the server of making a single request is the same as the effect of making several identical requests.

This does not necessarily mean that the request does not have _any_ unique side effects: for example, the server may log every request with the time it was received. Idempotency only applies to effects intended by the client: for example, a POST request intends to send data to the server, or a DELETE request intends to delete a resource on the server.
## Cacheable
A **cacheable** response is an HTTP response that can be cached, that is stored to be retrieved and used later, saving a new request to the server. Not all HTTP responses can be cached.

----
| Method | Description |
| ------ | ------- |
| [`GET`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/GET) | The `GET` method requests a representation of the specified resource. Requests using `GET`should only retrieve data.   |
| [`HEAD`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/HEAD) | The `HEAD` method asks for a response identical to a `GET` request, but without the response body. |
| [`POST`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/POST) | The `POST` method submits an entity to the specified resource, often causing a change in state or side effects on the server. |
| [`PUT`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/PUT) |  The `PUT` method replaces all current representations of the target resource with the request payload. |
| [`DELETE`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/DELETE) | The `DELETE` method deletes the specified resource. |
| [`CONNECT`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/CONNECT) | The `CONNECT` method establishes a tunnel to the server identified by the target resource. |
| [`OPTIONS`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/OPTIONS) | The `OPTIONS` method describes the communication options for the target resource. |
| [`TRACE`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/TRACE) | The `TRACE` method performs a message loop-back test along the path to the target resource. |
| [`PATCH`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/PATCH) | The `PATCH` method applies partial modifications to a resource. |

----
## References
- https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods

----
📂 [[HTTP]] | Последнее изменение: 20.02.2024 16:51