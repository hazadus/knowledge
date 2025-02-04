**Base64** – кодировка, которая применяется для передачи двоичных данных в при помощи символов ASCII. Например, в URL.

----
**Base64** is a group of similar [binary-to-text encoding](https://en.wikipedia.org/wiki/Binary-to-text_encoding) schemes that represent binary data in an [ASCII](https://developer.mozilla.org/en-US/docs/Glossary/ASCII) string format by transforming it into a radix-64 representation. The term _Base64_ originates from a specific [MIME content transfer encoding](https://en.wikipedia.org/wiki/MIME#Content-Transfer-Encoding).

When the term "Base64" is used on its own to refer to a specific [algorithm](https://developer.mozilla.org/en-US/docs/Glossary/Algorithm), it typically refers to the version of Base64 outlined in [RFC 4648](https://datatracker.ietf.org/doc/html/rfc4648), section 4, which uses the following alphabet to represent the radix-64 digits, alongside ` = ` as a padding character:

ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/

A common variant is "Base64 URL safe", which omits the padding and replaces `+/` with `-_` to avoid characters that might cause problems in [URL](https://developer.mozilla.org/en-US/docs/Glossary/URL) path segments or query parameters. You don't need this encoding if you are not putting the data in a path segment or query parameter — for example, [data URLs](https://developer.mozilla.org/en-US/docs/Web/URI/Schemes/data) have neither and can use the standard Base64 encoding.

Base64 encoding schemes are commonly used to encode binary data for storage or transfer over media that can only deal with ASCII text (or some superset of ASCII that still falls short of accepting arbitrary binary data). This ensures that the data remains intact without modification during transport. Common applications of Base64 include:

- Email via [MIME](https://en.wikipedia.org/wiki/MIME)
- Storing complex data in [XML](https://developer.mozilla.org/en-US/docs/Web/XML)
- Encoding binary data so that it can be included in a [`data:` URL](https://developer.mozilla.org/en-US/docs/Web/URI/Schemes/data)

----
## References

- https://developer.mozilla.org/en-US/docs/Glossary/Base64

----
📂 [[Misc]] | Последнее изменение: 28.12.2024 13:09