🔗 [[HTTP]]

----
The [HTTP/1.1 protocol](https://developer.mozilla.org/en-US/docs/Web/HTTP) provides a special mechanism that can be used to upgrade an already established connection to a different protocol, using the [`Upgrade`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Upgrade) header field.

This mechanism is optional; it cannot be used to insist on a protocol change. Implementations can choose not to take advantage of an upgrade even if they support the new protocol, and in practice, this mechanism is used mostly to bootstrap a WebSockets connection.

Note also that HTTP/2 explicitly disallows the use of this mechanism; it is specific to HTTP/1.1.

## Upgrading to a WebSocket connection
By far, the most common use case for upgrading an HTTP connection is to use WebSockets, which are always implemented by upgrading an HTTP or HTTPS connection. Keep in mind that if you're opening a new connection using the [WebSocket API](https://developer.mozilla.org/en-US/docs/Web/API/WebSocket), or any library that does WebSockets, most or all of this is done for you. For example, opening a WebSocket connection is as simple as:

```js
webSocket = new WebSocket("ws://destination.server.ext", "optionalProtocol");
```

The [`WebSocket()`](https://developer.mozilla.org/en-US/docs/Web/API/WebSocket/WebSocket "WebSocket()") constructor does all the work of creating an initial HTTP/1.1 connection then handling the handshaking and upgrade process for you.

If you need to create a WebSocket connection from scratch, you'll have to handle the handshaking process yourself. After creating the initial HTTP/1.1 session, you need to request the upgrade by adding to a standard request the [`Upgrade`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Upgrade) and [`Connection`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Connection) headers, as follows:

```http
Connection: Upgrade
Upgrade: websocket
```

----
## References
- https://developer.mozilla.org/en-US/docs/Web/HTTP/Protocol_upgrade_mechanism