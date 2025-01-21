![rw-book-cover](https://readwise-assets.s3.amazonaws.com/media/reader/parsed_document_assets/258496378/LVSHX7UYKJA-afi0K9kd6e2Drn6gkWWiikM7F-rwshQ-cove_C6EBUx7.png)

## Metadata
- Author: [[Alex Edwards]]
- Full Title: Let's Go
- Category: #articles
- Document Tags: [[Book]] [[Go]] 
- URL: https://readwise.io/reader/document_raw_content/258496378

## Highlights
- One of the great things about Go is that you can establish a web server and listen for incoming requests as part of your application itself. You don’t need an external third-party server like Nginx or Apache. ([View Highlight](https://read.readwise.io/read/01jh80fsfn0na6bf2t9a1hrkjk))

- Important: Before we continue, I should explain that Go’s servemux treats the URL pattern "/" like a catch-all. So at the moment all HTTP requests to our server will be handled by the home function, regardless of their URL path. For instance, you can visit a different URL path like http://localhost:4000/foo and you’ll receive exactly the same response. ([View Highlight](https://read.readwise.io/read/01jh80rzmnccgb0ctzmr66e38r))

- In Go’s servemux, fixed path patterns like these are only matched (and the corresponding handler called) when the request URL path exactly matches the fixed path. ([View Highlight](https://read.readwise.io/read/01jh80r4p5qh0jfm1793yg5v0j))

- Although this approach can make your code slightly shorter, I don’t recommend it for production applications.
  Because DefaultServeMux is a global variable, any package can access it and register a route — including any third-party packages that your application imports. If one of those third-party packages is compromised, they could use DefaultServeMux to expose a malicious handler to the web.
  So, for the sake of security, it’s generally a good idea to avoid DefaultServeMux and the corresponding helper functions. Use your own locally-scoped servemux instead, like we have been doing in this project so far. ([View Highlight](https://read.readwise.io/read/01jh80wpxwtxqvkv5vczp0w4zv))

- Important: Changing the response header map after a call to w.WriteHeader() or w.Write() will have no effect on the headers that the user receives. You need to make sure that your response header map contains all the headers you want before you call these methods. ([View Highlight](https://read.readwise.io/read/01jh8171z5bn6wf58fypyzz8f2))
    - Note: Логично, потому что статус-код возвращается в самом начале.



----
📂 [[Articles]] | Последнее изменение: 20.01.2025 11:31