With **server-sent events**, it's possible for a server to send new data to a web page at any time, by pushing messages to the web page. These incoming messages can be treated as Events + data inside the web page.

## Преимущества

- Простота использования. Данные идут только от сервера к клиенту, что упрощает логику и сервера, и клиента.
- Поддерживается всеми основными браузерами. 

## Особенности и недостатки

- Нет возможности отправлять данные с клиента на сервер.

## Events

Each message consists of one or more lines of text listing the fields for that message. Each field is represented by the field name, followed by a colon, followed by the text data for that field's value.

Each message received has some combination of the following fields, one per line:

- `event`: A string identifying the type of event described. If this is specified, an event will be dispatched on the browser to the listener for the specified event name; the website source code should use `addEventListener()` to listen for named events. The `onmessage` handler is called if no event name is specified for a message.

- `data`: The data field for the message. When the `EventSource` receives multiple consecutive lines that begin with `data:`, it concatenates them, inserting a newline character between each one. Trailing newlines are removed.

- `id`: The event ID to set the `EventSource` object's last event ID value.

- `retry`: The reconnection time. If the connection to the server is lost, the browser will wait for the specified time before attempting to reconnect. This must be an integer, specifying the reconnection time in milliseconds. If a non-integer value is specified, the field is ignored.

All other field names are ignored.

----
## Примеры

### Server

```go
package main

import (
	"fmt"
	"log"
	"net/http"
	"time"
)

func main() {
	http.HandleFunc("/events", sseHandler)

	fmt.Println("waiting for connections")
	err := http.ListenAndServe(":8080", nil)
	if err != nil {
		log.Fatalf("failed to start server: %s", err.Error())
	}
}

func sseHandler(w http.ResponseWriter, r *http.Request) {
	fmt.Println("new client has connected")

	// Set CORS headers before sending anything to client
	w.Header().Set("Content-Type", "text/event-stream")
	w.Header().Set("Cache-Control", "no-cache")
	w.Header().Set("Connection", "keep-alive")

	// TODO: Configure properly in production
	w.Header().Set("Access-Control-Allow-Origin", "*")
	w.Header().Set("Access-Control-Expose-Headers", "Content-Type")

	rc := http.NewResponseController(w)
	ticker := time.NewTicker(time.Second)
	defer ticker.Stop()

	clientGone := r.Context().Done()

	for {
		select {
		case <-clientGone:
			fmt.Println("client has disconnected")
			return
		case <-ticker.C:
			data := fmt.Sprintf(`{"message": "%s"}`, time.Now().Format("15:04:05"))
			fmt.Fprintf(w, "event:ticker\ndata:%s\n\n", data)
			rc.Flush()
		}
	}
}
```

### Client

```html
<!doctype html>
<html>
    <head>
        <title>Logstream</title>
    </head>
    <body>
        <div id="sse-data"></div>

        <script>
            <!--  TODO: Implement reconnect -->
            const eventSource = new EventSource("http://localhost:8080/events");
            const dataElement = document.getElementById("sse-data");
            dataElement.innerHTML += "Messages will appear here<br>";

            eventSource.addEventListener("ticker", (event) => {
                dataElement.innerHTML += event.data + "<br>";
            });

            eventSource.onerror = (err) => {
                console.error("EventSource failed:", err);
            };
        </script>
    </body>
</html>
```

---
## References

- https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events
- https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events