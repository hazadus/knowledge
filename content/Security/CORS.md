📁 [[Security]]

----

CORS – Cross-Origin Resource Sharing (совместное использование ресурсов из разных источников)

Браузер подставит header `Origin` в случае, если источник отличается от цели запроса. Эти хедеры видны на бэкенде. Во фласке посмотреть хедеры: `request.headers`.

Хедер `Access-Control-Allow-Origin` в ответе сервера позволяет установить разрешенные источники.

Во Flask:

```python
@app.after_request
def add_cors(response: Response):
	# Можно установить один источник или *:
	response.headers['Access-Control-Allow-Origin'] = "https://amgold.ru:3000"
	return response
```

> **Внимание**: домен должен совпадать полностью, то есть `https://rss.hazadus.ru` и `https://hazadus.ru` – не одно и то же.

Есть ещё несколько важных заголовков, связанных с CORS:
- `Access-Control-Allow-Methods`: указывает список методов, которые проходят CORS-политику;
- `Access-Control-Allow-Headers`: указывает список заголовков, которые разрешены CORS;
- `Access-Control-Max-Age`: указывает, сколько времени браузер может кешировать информацию, полученную из двух предыдущих заголовков.

----
🔗 Ref: https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS

**Cross-Origin Resource Sharing** ([CORS](https://developer.mozilla.org/en-US/docs/Glossary/CORS)) is an [HTTP](https://developer.mozilla.org/en-US/docs/Glossary/HTTP)-header based mechanism that allows a server to indicate any [origins](https://developer.mozilla.org/en-US/docs/Glossary/Origin) (domain, scheme, or port) other than its own from which a browser should permit loading resources. CORS also relies on a mechanism by which browsers make a "preflight" request to the server hosting the cross-origin resource, in order to check that the server will permit the actual request. In that preflight, the browser sends headers that indicate the HTTP method and headers that will be used in the actual request.

An example of a cross-origin request: the front-end JavaScript code served from `https://domain-a.com` uses [`fetch()`](https://developer.mozilla.org/en-US/docs/Web/API/fetch) to make a request for `https://domain-b.com/data.json`.

----
🔗 [[Julia Evans - HTTP_ Learn your browser's language!-Julia Evans 1.pdf]]

![[Pasted image 20240418114430.png]]

![[Pasted image 20240418114616.png]]

![[Pasted image 20240418115519.png]]

![[Pasted image 20240418115538.png]]



----
📂 [[Security]]