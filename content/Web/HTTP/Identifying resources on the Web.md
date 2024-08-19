🔗 [[HTTP]]

----
> The target of an HTTP request is called a "resource", whose nature isn't defined further; it can be a document, a photo, or anything else. Each resource is identified by a Uniform Resource Identifier ([URI](https://developer.mozilla.org/en-US/docs/Glossary/URI)) used throughout HTTP for identifying resources.

## URLs
The most common form of URI is the Uniform Resource Locator ([URL](https://developer.mozilla.org/en-US/docs/Glossary/URL)), which is known as the _web address_.
```
https://developer.mozilla.org
https://developer.mozilla.org/en-US/docs/Learn/
https://developer.mozilla.org/en-US/search?q=URL
```
A URL is composed of different parts, some mandatory and others optional. A more complex example might look like this:
```
http://www.example.com:80/path/to/myfile.html?key1=value1&key2=value2#SomewhereInTheDocument
```
## URNs
A Uniform Resource Name (URN) is a URI that identifies a resource by name in a particular namespace.
```
urn:isbn:9780141036144
urn:ietf:rfc:7230
```
# Syntax of Uniform Resource Identifiers (URIs)
## Scheme or Protocol
| Scheme | Descrtiption |
| ---- | ---- |
| `data` | Data URLs, prefixed with the `data:` scheme, allow content creators to embed small files inline in documents. |
| `file` | Host-specific file names |
| `ftp` | FTP |
| `http/https` | HTTP, HTTPS |
| `javascript` | URL-embedded JS code |
| `mailto` | Email |
| `ssh` | Secure shell |
| `tel` | Phone number |
| `urn` | Uniform Resource Name |
| `view-source` | Source code of the resource |
| `ws/wss` | WebSocket connections (Secure) |
## Authority
Domain name or IP address.
## Port
By default, `:80` for HTTP and `:443` for HTTPS.
## Path
Path to the resource on the Web server. May or may not represent physical file location.
## Query
`?key1=value1&key2=value2` are extra parameters provided to the Web server. Those parameters are a list of key/value pairs separated with the `&` symbol.
## Fragment
`#SomewhereInTheDocument` is an anchor to another part of the resource itself. An anchor represents a sort of "bookmark" inside the resource, giving the browser the directions to show the content located at that "bookmarked" spot.

----
📂 [[HTTP]] | Последнее изменение: 20.02.2024 12:26