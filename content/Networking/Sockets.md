🔗 [[Networking]]

----
[Сокет](https://ru.wikipedia.org/wiki/%D0%A1%D0%BE%D0%BA%D0%B5%D1%82_(%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%BD%D1%8B%D0%B9_%D0%B8%D0%BD%D1%82%D0%B5%D1%80%D1%84%D0%B5%D0%B9%D1%81)) - это некоторая абстракция операционной системы, представляющая собой интерфейс обмена данными между процессами. В частности и по сети. Сокет можно открыть, можно записать в него данные и прочитать данные из него.

![[Pasted image 20240220172839.png]]

Т.к. видов [межпроцессных взаимодействий](https://ru.wikipedia.org/wiki/%D0%9C%D0%B5%D0%B6%D0%BF%D1%80%D0%BE%D1%86%D0%B5%D1%81%D1%81%D0%BD%D0%BE%D0%B5_%D0%B2%D0%B7%D0%B0%D0%B8%D0%BC%D0%BE%D0%B4%D0%B5%D0%B9%D1%81%D1%82%D0%B2%D0%B8%D0%B5) с помощью сокетов множество, то и сокеты могут иметь различные конфигурации: сокет характеризуется семейством протоколов (IPv4 или IPv6 для сетевого и UNIX для локального взаимодействия), типом передачи данных (потоковая или датаграммная) и протоколом (TCP, UDP и т.п.).

## Client Connection Process

The most confusing thing about using sockets is that there are generally several steps you have to take to connect to another computer, and they’re not obvious.

But they are:

1. **Ask the OS for a socket**. In C, this is just a file descriptor (an integer) that will be used from here on to refer to this network connection. Python will return an object representing the socket. Other language APIs might return different things.
    
	But the important thing about this step is that you have a way to refer to this socket for upcoming data transmission. Note that it’s not connected to anything yet at all.
    
2. **Perform a DNS lookup** to convert the human-readable name (like `example.com`) into an IP address (like 198.51.100.12). DNS is the distributed database that holds this mapping, and we query it to get the IP address.
    
    We need the IP address so that we know the machine to connect to.
    
    Python Hint: While you can do DNS lookups in Python with `socket.getaddrinfo()`, just calling `socket.connect()` with a hostname will do the DNS lookup for you. So you can skip this step.
    
	Optional C Hint: Use `getaddrinfo()` to perform this lookup.
    
3. **Connect the socket** to that IP address on a specific port.
    
    Think of a port number like an open door that you can connect through. They’re integers that range from 0 to 65535.
    
    A good example port to remember is 80, which is the standard port used for servers that speak the HTTP protocol (unencrypted).
    
    There must be a server listening on that port on that remote computer, or the connection will fail.
    
4. **Send data and receive data**. This is the part we’ve been waiting for.
    
    Data is sent as a sequence of bytes.
    
5. Close the connection. When we’re done, we close the socket indicating to the remote side that we have nothing more to say. The remote side can also close the connection any time it wishes.

## Server Listening Process

Writing a server program is a little bit different.

1. **Ask the OS for a socket**. Just like with the client.
    
2. **Bind the socket to a port**. This is where you assign a port number to the server that other clients can connect to. “I’m going to be listening on port 80!” for instance.
    
    Caveat: programs that aren’t run as root/administrator can’t bind to ports under 1024–those are reserved. Choose a big, uncommon port number for your servers, like something in the 15,000-30,000 range. If you try to bind to a port another server is using, you’ll get an “Address already in use” error.
    
    Ports are per-computer. It’s OK if two different computers use the same port. But two programs on the same computer cannot use the same port on that computer.
    
    Fun fact: clients are bound to a port, as well. If you don’t explicitly bind them, they get assigned an unused port when the connect–which is usually what we want.
    
3. **Listen for incoming connections**. We have to let the OS know when it gets an incoming connection request on the port we selected.
    
4. **Accept incoming connections**. The server will block (it will sleep) when you try to accept a new connection if none are pending. Then it wakes up when someone tries to connect.
    
    Accept returns a new socket! This is confusing. The original socket the server made in step 1 is still there listening for new connections. When the connection arrives, the OS makes a new socket _specifically for that one connection_. This way the server can handle multiple clients at once.
    
    Sometimes the server spawns a new thread or process to handle each new client. But there’s no law that says it has to.
    
5. **Send data and receive data**. This is typically where the server would receive a request from the client, and the server would send back the response to that request.
    
6. **Go back and accept another connection**. Servers tend to be long-running processes and handle many requests over their lifetimes.

----
## References
- https://iximiuz.com/ru/posts/writing-python-web-server-part-1/
- [Socket Programming HOWTO](https://docs.python.org/3.12/howto/sockets.html) in Python 3.12 documentation.
- [Introducing The Sockets API](https://beej.us/guide/bgnet0/html/split/introducing-the-sockets-api.html#introducing-the-sockets-api)
- [_Beej’s Guide to Network Programming_](https://beej.us/guide/bgnet) – optional, for C devs.


----
📂 [[Networking]] | Последнее изменение: 21.02.2024 09:35