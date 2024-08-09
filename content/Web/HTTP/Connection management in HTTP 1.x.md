🔗 [[HTTP]]

----

> Connection management is a key topic in HTTP: opening and maintaining connections largely impacts the performance of websites and Web applications. In HTTP/1.x, there are several models: _short-lived connections_, _persistent connections_, and _HTTP pipelining._

HTTP mostly relies on TCP for its transport protocol, providing a connection between the client and the server. In its infancy, HTTP used a single model to handle such connections. These connections were short-lived: a new one created each time a request needed sending, and closed once the answer had been received.

This simple model held an innate limitation on performance: opening each TCP connection is a resource-consuming operation. Several messages must be exchanged between the client and the server. Network latency and bandwidth affect performance when a request needs sending. Modern Web pages require many requests (a dozen or more) to serve the amount of information needed, proving this earlier model inefficient.

Two newer models were created in HTTP/1.1. The persistent-connection model keeps connections opened between successive requests, reducing the time needed to open new connections. The HTTP pipelining model goes one step further, by sending several successive requests without even waiting for an answer, reducing much of the latency in the network.

![[Pasted image 20240220154201.png]]

## Short-lived connections
The original model of HTTP, and the default one in HTTP/1.0, is _short-lived connections_. Each HTTP request is completed on its own connection; this means a TCP handshake happens before each HTTP request, and these are serialized.

The TCP handshake itself is time-consuming, but a TCP connection adapts to its load, becoming more efficient with more sustained (or warm) connections. Short-lived connections do not make use of this efficiency feature of TCP, and performance degrades from optimum by persisting to transmit over a new, cold connection.

This model is the default model used in HTTP/1.0 (if there is no [`Connection`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Connection) header, or if its value is set to `close`). In HTTP/1.1, this model is only used when the [`Connection`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Connection) header is sent with a value of `close`.

## Persistent connections
Short-lived connections have two major hitches: the time taken to establish a new connection is significant, and performance of the underlying TCP connection gets better only when this connection has been in use for some time (warm connection). To ease these problems, the concept of a _persistent connection_ has been designed, even prior to HTTP/1.1. Alternatively this may be called a _keep-alive connection_.

A persistent connection is one which remains open for a period of time, and can be reused for several requests, saving the need for a new TCP handshake, and utilizing TCP's performance enhancing capabilities. This connection will not stay open forever: idle connections are closed after some time (a server may use the [`Keep-Alive`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Keep-Alive) header to specify a minimum time the connection should be kept open).

Persistent connections also have drawbacks; even when idling they consume server resources, and under heavy load, [[DoS Attack]]s can be conducted. In such cases, using non-persistent connections, which are closed as soon as they are idle, can provide better performance.

HTTP/1.0 connections are not persistent by default. Setting [`Connection`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Connection) to anything other than `close`, usually `retry-after`, will make them persistent.

In HTTP/1.1, persistence is the default, and the header is no longer needed (but it is often added as a defensive measure against cases requiring a fallback to HTTP/1.0).

## HTTP Pipelining
By default, [HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP) requests are issued sequentially. The next request is only issued once the response to the current request has been received. As they are affected by network latencies and bandwidth limitations, this can result in significant delay before the next request is _seen_ by the server.

Pipelining is the process to send successive requests, over the same persistent connection, without waiting for the answer. This avoids latency of the connection. Theoretically, performance could also be improved if two HTTP requests were to be packed into the same TCP message. The typical [MSS](https://en.wikipedia.org/wiki/Maximum_segment_size) (Maximum Segment Size), is big enough to contain several simple requests, although the demand in size of HTTP requests continues to grow.

Not all types of HTTP requests can be pipelined: only [idempotent](https://developer.mozilla.org/en-US/docs/Glossary/Idempotent) methods, that is [`GET`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/GET), [`HEAD`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/HEAD), [`PUT`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/PUT) and [`DELETE`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/DELETE), can be replayed safely. Should a failure happen, the pipeline content can be repeated.

Today, every HTTP/1.1-compliant proxy and server should support pipelining, though many have limitations in practice: a significant reason no modern browser activates this feature by default.

----
## References
- https://developer.mozilla.org/en-US/docs/Web/HTTP/Connection_management_in_HTTP_1.x