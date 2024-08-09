🔗 [[HTTP]] / [[HTTP Messages]]

----
> **HTTP headers** let the client and the server pass additional information with an HTTP request or response. An HTTP header consists of its case-insensitive name followed by a colon (`:`), then by its value. [Whitespace](https://developer.mozilla.org/en-US/docs/Glossary/Whitespace) before the value is ignored.

Headers can be grouped according to their contexts:

- [Request headers](https://developer.mozilla.org/en-US/docs/Glossary/Request_header): Contain more information about the resource to be fetched, or about the client requesting the resource.
- [Response headers](https://developer.mozilla.org/en-US/docs/Glossary/Response_header): Hold additional information about the response, like its location or about the server providing it.
- [Representation headers](https://developer.mozilla.org/en-US/docs/Glossary/Representation_header): Contain information about the body of the resource, like its [MIME type](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types), or encoding/compression applied.
- [Payload headers](https://developer.mozilla.org/en-US/docs/Glossary/Payload_header): Contain representation-independent information about payload data, including content length and the encoding used for transport.

----
## Most common headers
Тут приведены только наиболее часто встречающиеся мне заголовки. Полный список см. на [MDN](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers).

![[telegram-cloud-photo-size-2-5341794858219721582-y.jpg]]
### Authentication
- [`Authorization`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Authorization): Contains the credentials to authenticate a user-agent with a server.
### Caching
...
### Conditionals
- [`ETag`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/ETag): A unique string identifying the version of the resource. Conditional requests using [`If-Match`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/If-Match)and [`If-None-Match`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/If-None-Match) use this value to change the behavior of the request.
### Connection management
- [`Connection`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Connection): Controls whether the network connection stays open after the current transaction finishes.
- [`Keep-Alive`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Keep-Alive): Controls how long a persistent connection should stay open.
### Content negotiation
- [`Accept`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Accept): Informs the server about the [types](https://developer.mozilla.org/en-US/docs/Glossary/MIME_type) of data that can be sent back.
### Controls
...
### Cookies
- [`Cookie`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Cookie): Contains stored [HTTP cookies](https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies) previously sent by the server with the [`Set-Cookie`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie) header.
- [`Set-Cookie`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie): Send cookies from the server to the user-agent.
### CORS
...
### Downloads
- [`Content-Disposition`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Disposition): Indicates if the resource transmitted should be displayed inline (default behavior without the header), or if it should be handled like a download and the browser should present a "Save As" dialog.
### Message body information
- [`Content-Length`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Length): The size of the resource, in decimal number of bytes.
- [`Content-Type`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Type): Indicates the media type of the resource.
### Proxies
...
### Redirects
- [`Location`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Location): Indicates the URL to redirect a page to.
### Request context
- [`Referer`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Referer): The address of the previous web page from which a link to the currently requested page was followed.
- [`Referrer-Policy`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Referrer-Policy): Governs which referrer information sent in the [`Referer`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Referer) header should be included with requests made.
- [`User-Agent`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/User-Agent): Contains a characteristic string that allows the network protocol peers to identify the application type, operating system, software vendor or software version of the requesting software user agent.
### Response context
- [`Allow`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Allow): Lists the set of HTTP request methods supported by a resource.
- [`Server`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Server): Contains information about the software used by the origin server to handle the request.
### Range requests
...
### Security
...

----
## References
- https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers