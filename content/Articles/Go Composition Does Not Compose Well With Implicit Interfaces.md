![rw-book-cover](https://readwise-assets.s3.amazonaws.com/static/images/article1.be68295a7e40.png)

## Metadata
- Author: [[Internal Tools Deployment Platform | Clace]]
- Full Title: Go Composition Does Not Compose Well With Implicit Interfaces
- Category: #articles
- Document Note: Учитывать описанную проблему при использовании композиции типов.
- Document Tags: [[go]] [[Outline]] 
- Summary: Clace encountered a problem where Server-Sent Events (SSE) stopped working due to a change in how HTTP response status codes were tracked. This issue arose because adding a composition over `http.ResponseWriter` caused it to lose support for the implicit interface `http.Flusher`, which is needed for SSE. To fix the problem, the custom struct must explicitly implement the `http.Flusher` interface to maintain its functionality.
- URL: https://clace.io/blog/go-composition/

## Highlights
- The reason for the issue encountered is an implicit interface [http.Flusher](https://pkg.go.dev/net/http#Flusher) implemented by most implementations of [http.ResponseWriter](https://pkg.go.dev/net/http#ResponseWriter). Adding a composition over `http.ResponseWriter` causes this implicit interface to no longer be implemented. ([View Highlight](https://read.readwise.io/read/01jj3pexzpxs3mwyg5ktsqeczc))

- The takeaway is that if using composition over types which could have implicit interfaces, it is important to look at whether any of those implicit interfaces have to be explicitly implemented by the composing type. ([View Highlight](https://read.readwise.io/read/01jj3pf8sjcjdk269ah2kwfv4m))



----
📂 [[Articles]] | Последнее изменение: 21.01.2025 10:44