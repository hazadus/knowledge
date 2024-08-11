🔗 [[Networking]]

----
- **IP Address** – historically 4-byte number uniquely identifying your computer on the Internet. Written in dots-and-numbers notation, like so: `198.51.100.99`.
    
    These are IP version 4 (“IPv4”) addresses. Typically “v4” is implied in the absence of any other version identifier.
    
- **Port** – Programs talk through ports, which are numbered 0-65535 and are associated with the TCP or UDP protocols.
    
    Since multiple programs can be running on the same IP address, the port provides a way to uniquely identify those programs on the network.
    
    For example, it’s very common for a web server to listen for incoming connections on port 80.
    
    Publishing the port number is really important for server programs since client programs need to know where to connect to them.
    
    Clients usually let the OS choose an unused port for them to use since no one tries to connect to clients.
    
    In a URL, the port number is after a colon. Here we try to connect to `example.com` on port `3490`: `http://example.com:3490/foo.html`
    
    Ports under 1024 need root/administrator privileges to bind to (but not to connect to).
    
- **TCP** – Transmission Control Protocol, responsible for reliable, in-order data transmission. From a higher-up perspective, makes a packet-switched network feel more like a circuit-switched network.
    
    TCP uses port numbers to identify senders and receivers of data.
    
    This protocol was invented in 1974 and is still in extremely heavy use today.
    
    In the sockets API, TCP sockets are called _stream sockets_.
    
- **UDP** – sibling of TCP, except lighter weight. Doesn’t guarantee data will arrive, or that it will be in order, or that it won’t be duplicated. If it arrives, it will be error-free, but that’s all you get.
    
    In the sockets API, UDP sockets are called _datagram sockets_.
    
- **IPv6 Address** – Four bytes isn’t enough to hold a unique address, so IP version 6 expands the address size considerably to 16 bytes. IPv6 addresses look like this: `::1` or `2001:db8::8a2e:370:7334`, or even bigger.
    
- **NAT** – Network Address Translation. A way to allow organizations to have private subnets with non-globally-unique addresses that get translated to globally-unique addresses as they pass through the router.
    
    Private subnets commonly start with addresses `192.168.x.x` or `10.x.x.x`.
    
- **Router** – A specialized computer that forwards packets through the packet switching network. It inspects destination IP addresses to determine which route will get the packet closer to its goal.
    
- **IP** – Internet Protocol. This is responsible for identifying computers by IP address and using those addresses to route data to recipients through a variety of routers.
    
- **LAN** – Local Area Network. A network where all the computers are effectively directly connected, not via a router.
    
- **Interface** – physical networking hardware on a computer. A computer might have a number of interfaces. Your computer likely has two: a wired Ethernet interface and a wireless Ethernet interface.
    
    A router might have a large number of interfaces to be able to route packets to a large number of destinations. Your home router probably only has two interfaces: one facing inward to your LAN and the other facing outward to the rest of the Internet.
    
    Each interface typically has one IP address and one MAC address.
    
    The OS names the interfaces on your local machine. They might be something like `wlan0` or `eth2` or something else. It depends on the hardware and the OS.
    
- **Header** – Some data that is prepended to some other data by a particular protocol. The header contains information appropriate for that protocol. A TCP header would include some error detection and correction information and a source and destination port number. IP would include the source and destination IP addresses. Ethernet would include the source and destination MAC addresses. And an HTTP response would include things like the length of the data, the date modified, and whether or not the request was successful.
    
    Putting a header in front of the data is analogous to putting your letter in an envelope in the snail-mail analogy. Or putting that envelope in another envelope.
    
    As data moves through the network, additional headers are added and removed. Typically only the top-most (front-most?) header is removed or added in normal operation, like a stack. (But some software and hardware peeks deeper.)
    
    **Network Adapter** – Another name for “network card”, the hardware on your computer that does network stuff.
    
    **MAC Address** (Media Access Control) – Ethernet interfaces have MAC addresses, which take the form `aa:bb:cc:dd:ee:ff`, where the fields are random-ish one-byte hex numbers. MAC addresses are 6 bytes long, and must be unique on the LAN. When a network adapter is manufactured, it is given a unique MAC address that it keeps for life, typically.

----
📂 [[Networking]]