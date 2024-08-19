🔗 [[HTTP]]

----
> HTTP messages are how data is exchanged between a server and a client. There are two types of messages: _requests_ sent by the client to trigger an action on the server, and _responses_, the answer from the server.

HTTP messages are composed of textual information encoded in ASCII, and span over multiple lines. In HTTP/1.1, and earlier versions of the protocol, these messages were openly sent across the connection. In HTTP/2, the once human-readable message is now divided up into HTTP frames, providing optimization and performance improvements.

HTTP requests, and responses, share similar structure and are composed of:

1. A _start-line_ describing the requests to be implemented, or its status of whether successful or a failure. This is always a single line.
2. An optional set of _HTTP headers_ specifying the request, or describing the body included in the message.
3. A blank line indicating all meta-information for the request has been sent.
4. An optional _body_ containing data associated with the request (like content of an HTML form), or the document associated with a response. The presence of the body and its size is specified by the start-line and HTTP headers.

The start-line and HTTP headers of the HTTP message are collectively known as the _head_ of the requests, whereas its payload is known as the _body_.

![[Pasted image 20240220133254.png]]

>[!important]
> Request line and headers must be in ASCII encoding.

----
## HTTP Requests
### Request line
HTTP requests are messages sent by the client to initiate an action on the server. Their _request-line_ contain three elements:

1. An _[HTTP method](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods)_, a verb (like [`GET`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/GET), [`PUT`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/PUT) or [`POST`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/POST)) or a noun (like [`HEAD`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/HEAD) or [`OPTIONS`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/OPTIONS)), that describes the action to be performed. For example, `GET` indicates that a resource should be fetched or `POST` means that data is pushed to the server (creating or modifying a resource, or generating a temporary document to send back).
2. The _request target_, usually a [URL](https://developer.mozilla.org/en-US/docs/Glossary/URL), or the absolute path of the protocol, port, and domain are usually characterized by the request context. The format of this request target varies between different HTTP methods. It can be
    - An absolute path, ultimately followed by a `'?'` and query string. This is the most common form, known as the _origin form_, and is used with `GET`, `POST`, `HEAD`, and `OPTIONS` methods.
        - `POST / HTTP/1.1`
        - `GET /background.png HTTP/1.0`
        - `HEAD /test.html?query=alibaba HTTP/1.1`
        - `OPTIONS /anypage.html HTTP/1.0`
    - A complete URL, known as the _absolute form_, is mostly used with `GET` when connected to a proxy. `GET https://developer.mozilla.org/en-US/docs/Web/HTTP/Messages HTTP/1.1`
    - The authority component of a URL, consisting of the domain name and optionally the port (prefixed by a `':'`), is called the _authority form_. It is only used with `CONNECT` when setting up an HTTP tunnel. `CONNECT developer.mozilla.org:80 HTTP/1.1`
    - The _asterisk form_, a simple asterisk (`'*'`) is used with `OPTIONS`, representing the server as a whole. `OPTIONS * HTTP/1.1`
3. The _HTTP version_, which defines the structure of the remaining message, acting as an indicator of the expected version to use for the response.

### Headers
[[HTTP Headers]] from a request follow the same basic structure of an HTTP header: a case-insensitive string followed by a colon (`':'`) and a value whose structure depends upon the header. The whole header, including the value, consists of one single line, which can be quite long.

Many different headers can appear in requests. They can be divided in several groups:

- [General headers](https://developer.mozilla.org/en-US/docs/Glossary/General_header), like [`Via`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Via), apply to the message as a whole.
- [Request headers](https://developer.mozilla.org/en-US/docs/Glossary/Request_header), like [`User-Agent`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/User-Agent) or [`Accept`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Accept), modify the request by specifying it further (like [`Accept-Language`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Accept-Language)), by giving context (like [`Referer`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Referer)), or by conditionally restricting it (like [`If-None-Match`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/If-None-Match)).
- [Representation headers](https://developer.mozilla.org/en-US/docs/Glossary/Representation_header) like [`Content-Type`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Type) that describe the original format of the message data and any encoding applied (only present if the message has a body).

![[Pasted image 20240220134022.png]]

### Body
The final part of the request is its body. Not all requests have one: requests fetching resources like `GET` or `HEAD` usually don't need a body. Requests that send data to the server to create a resource, such as `PUT` or `POST` requests, typically require a body with the data used to fulfill the request (for instance, HTML form data).

Bodies can be broadly divided into two categories:

- Single-resource bodies, consisting of one single file, defined by the two headers: [`Content-Type`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Type) and [`Content-Length`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Length).
- [Multiple-resource bodies](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types#multipartform-data), consisting of a multipart body, each containing a different bit of information. This is typically associated with [HTML Forms](https://developer.mozilla.org/en-US/docs/Learn/Forms).

----
## HTTP Responses
### Status line
The start line of an HTTP response, called the _status line_, contains the following information:

1. The _protocol version_, usually `HTTP/1.1`, but can also be `HTTP/1.0`.
2. A [_status code_](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status), indicating success or failure of the request. Common status codes are [`200`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/200), [`404`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/404), or [`302`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/302).
3. A _status text_. A brief, purely informational, textual description of the status code to help a human understand the HTTP message.

A typical status line looks like: `HTTP/1.1 404 Not Found`.

### Headers
[[HTTP Headers]] for responses follow the same structure as any other header: a case-insensitive string followed by a colon (`':'`) and a value whose structure depends upon the type of the header. The whole header, including its value, presents as a single line.

Many different headers can appear in responses. These can be divided into several groups:

- [General headers](https://developer.mozilla.org/en-US/docs/Glossary/General_header), like [`Via`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Via), apply to the whole message.
- [Response headers](https://developer.mozilla.org/en-US/docs/Glossary/Response_header), like [`Vary`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Vary) and [`Accept-Ranges`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Accept-Ranges), give additional information about the server which doesn't fit in the status line.
- [Representation headers](https://developer.mozilla.org/en-US/docs/Glossary/Representation_header) like [`Content-Type`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Type) that describe the original format of the message data and any encoding applied (only present if the message has a body).

![[Pasted image 20240220134739.png]]

### Body
The last part of a response is the body. Not all responses have one: responses with a status code that sufficiently answers the request without the need for corresponding payload (like [`201`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/201)**`Created`** or [`204`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/204) **`No Content`**) usually don't.

Bodies can be broadly divided into three categories:

- Single-resource bodies, consisting of a single file of known length, defined by the two headers: [`Content-Type`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Type) and [`Content-Length`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Length).
- Single-resource bodies, consisting of a single file of unknown length, encoded by chunks with [`Transfer-Encoding`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Transfer-Encoding) set to `chunked`.
- [Multiple-resource bodies](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types#multipartform-data), consisting of a multipart body, each containing a different section of information. These are relatively rare.

----
## References
- https://developer.mozilla.org/en-US/docs/Web/HTTP/Messages
- [[Julia Evans - HTTP_ Learn your browser's language!-Julia Evans 1.pdf]]


----
📂 [[HTTP]] | Последнее изменение: 18.04.2024 11:56