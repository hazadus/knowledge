🔗 [[HTTP]]

----
> A **media type** (also known as a **Multipurpose Internet Mail Extensions or MIME type**) indicates the nature and format of a document, file, or assortment of bytes. MIME types are defined and standardized in IETF's [RFC 6838](https://datatracker.ietf.org/doc/html/rfc6838).

The [Internet Assigned Numbers Authority (IANA)](https://www.iana.org/) is responsible for all official MIME types, and you can find the most up-to-date and complete list at their [Media Types](https://www.iana.org/assignments/media-types/media-types.xhtml) page.

> [!important]
> **Warning:** Browsers use the MIME type, _not the file extension_, to determine how to process a URL, so it's important that web servers send the correct MIME type in the response's [`Content-Type`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Type) header. If this is not correctly configured, browsers are likely to misinterpret the contents of files, sites will not work correctly, and downloaded files may be mishandled.

----
## Structure of a MIME type
A MIME type most commonly consists of just two parts: a _type_ and a _subtype_, separated by a slash (`/`) — with no whitespace between: `type/subtype`.

The **_type_** represents the general category into which the data type falls, such as `video` or `text`.

The **_subtype_** identifies the exact kind of data of the specified type the MIME type represents. For example, for the MIME type `text`, the subtype might be `plain` (plain text), `html` ([HTML](https://developer.mozilla.org/en-US/docs/Glossary/HTML)source code), or `calendar` (for iCalendar/`.ics`) files.

Each type has its own set of possible subtypes. A MIME type always has both a type and a subtype, never just one or the other.

An optional **parameter** can be added to provide additional details: `type/subtype;parameter=value`;  `text/plain;charset=UTF-8`.

MIME types are case-insensitive but are traditionally written in lowercase. The parameter values can be case-sensitive.

### Discrete types
| Type | Description |
| ---- | ---- |
| `application` | Any kind of binary data that doesn't fall explicitly into one of the other types; either data that will be executed or interpreted in some way or binary data that requires a specific application or category of application to use. Generic binary data (or binary data whose true type is unknown) is `application/octet-stream`. Other common examples include `application/pdf`, `application/pkcs8`, and `application/zip`. |
| `audio` | Audio or music data. Examples include `audio/mpeg`, `audio/vorbis`. |
| `example` | Reserved for use as a placeholder in examples showing how to use MIME types. These should never be used outside of sample code listings and documentation. |
| `font` | Font/typeface data. Common examples include `font/woff`, `font/ttf`, and `font/otf`. |
| `image` | Image or graphical data including both bitmap and vector still images as well as animated versions of still image formats such as animated [GIF](https://developer.mozilla.org/en-US/docs/Glossary/GIF) or APNG. Common examples are `image/jpeg`, `image/png`, and `image/svg+xml`. |
| `model` | Model data for a 3D object or scene. Examples include `model/3mf` and `model/vrml`. |
| `text` | Text-only data including any human-readable content, source code, or textual data such as comma-separated value (CSV) formatted data. Examples include: `text/plain`, `text/csv`, and `text/html`. |
| `video` | Video data or files, such as MP4 movies (`video/mp4`). |
For text documents without a specific subtype, `text/plain` should be used. Similarly, for binary documents without a specific or known subtype, `application/octet-stream` should be used.

### Multipart types
**Multipart** types indicate a category of document broken into pieces, often with different MIME types; they can also be used — especially in email scenarios — to represent multiple, separate files which are all part of the same transaction. They represent a **composite document**.

Except for `multipart/form-data`, used in the [`POST`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/POST) method of [HTML Forms](https://developer.mozilla.org/en-US/docs/Learn/Forms), and `multipart/byteranges`, used with [`206`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/206) `Partial Content` to send part of a document, HTTP doesn't handle multipart documents in a special way: the message is transmitted to the browser (which will likely show a "Save As" window if it doesn't know how to display the document).

| Type | Description |
| ---- | ---- |
| `message` | A message that encapsulates other messages. This can be used, for instance, to represent an email that includes a forwarded message as part of its data, or to allow sending very large messages in chunks as if it were multiple messages. |
| `multipart` | Data that consists of multiple components which may individually have different MIME types. Examples include `multipart/form-data` (for data produced using the [`FormData`](https://developer.mozilla.org/en-US/docs/Web/API/FormData) API) and `multipart/byteranges` (defined in [RFC 7233, section 5.4.1](https://datatracker.ietf.org/doc/html/rfc7233#section-5.4.1) and used with [HTTP](https://developer.mozilla.org/en-US/docs/Glossary/HTTP)'s [`206`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/206)"Partial Content" response returned when the fetched data is only part of the content, such as is delivered using the [`Range`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Range) header). |
#### `multipart/form-data`
The `multipart/form-data` type can be used when sending the values of a completed [HTML Form](https://developer.mozilla.org/en-US/docs/Learn/Forms) from browser to server.

As a multipart document format, it consists of different parts, delimited by a boundary (a string starting with a double dash `--`). Each part is its own entity with its own HTTP headers, [`Content-Disposition`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Disposition), and [`Content-Type`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Type) for file uploading fields.

```
Content-Type: multipart/form-data; boundary=aBoundaryString
(other headers associated with the multipart document as a whole)

--aBoundaryString
Content-Disposition: form-data; name="myFile"; filename="img.jpg"
Content-Type: image/jpeg

(data)
--aBoundaryString
Content-Disposition: form-data; name="myField"

(data)
--aBoundaryString
(more subparts)
--aBoundaryString--
```

The following `<form>`:

```html
<form
  action="http://localhost:8000/"
  method="post"
  enctype="multipart/form-data">
  <label>Name: <input name="myTextField" value="Test" /></label>
  <label><input type="checkbox" name="myCheckBox" /> Check</label>
  <label>
    Upload file: <input type="file" name="myFile" value="test.txt" />
  </label>
  <button>Send the file</button>
</form>
```

will send this message:

```http
POST / HTTP/1.1
Host: localhost:8000
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:50.0) Gecko/20100101 Firefox/50.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: keep-alive
Upgrade-Insecure-Requests: 1
Content-Type: multipart/form-data; boundary=---------------------------8721656041911415653955004498
Content-Length: 465

-----------------------------8721656041911415653955004498
Content-Disposition: form-data; name="myTextField"

Test
-----------------------------8721656041911415653955004498
Content-Disposition: form-data; name="myCheckBox"

on
-----------------------------8721656041911415653955004498
Content-Disposition: form-data; name="myFile"; filename="test.txt"
Content-Type: text/plain

Simple file.
-----------------------------8721656041911415653955004498--
```

#### `multipart/byteranges`

The `multipart/byteranges` MIME type is used to send partial responses to the browser.

When the [`206 Partial Content`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/206) status code is sent, this MIME type indicates that the document is composed of several parts, one for each of the requested ranges. Like other multipart types, the [`Content-Type`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Type) uses a `boundary` to separate the pieces. Each piece has a [`Content-Type`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Type)header with its actual type and a [`Content-Range`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Range) of the range it represents.

```http
HTTP/1.1 206 Partial Content
Accept-Ranges: bytes
Content-Type: multipart/byteranges; boundary=3d6b6a416f9b5
Content-Length: 385

--3d6b6a416f9b5
Content-Type: text/html
Content-Range: bytes 100-200/1270

eta http-equiv="Content-type" content="text/html; charset=utf-8" />
    <meta name="viewport" content
--3d6b6a416f9b5
Content-Type: text/html
Content-Range: bytes 300-400/1270

-color: #f0f0f2;
        margin: 0;
        padding: 0;
        font-family: "Open Sans", "Helvetica
--3d6b6a416f9b5--
```

----
## References
- https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types

----
📂 [[HTTP]] | Последнее изменение: 20.02.2024 14:49