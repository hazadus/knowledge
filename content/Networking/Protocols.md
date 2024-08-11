🔗 [[Networking]]

----
## Contents

- [[TCP]] - used to transmit data reliably.
- UDP - used to transmit data quickly and unreliably.
- [[IP]] - used to route packets over the network from one computer to another.
- Ethernet - used to send data over a LAN.
- [[HTTP]] - used to get web pages and make other web requests.

----
## Network Layers and Abstraction

Here’s a quick overview of what happens when data goes out on the network. We’ll cover this in much more detail in the coming modules.

1. A user program says, “I want to send the bytes `GET / HTTP/1.1` to that web server over there.” (Servers are identified by _IP address_ and a _port_ on the Internet–more on that later.)
2. The OS takes the data and wraps it up in a _header_ (that is, prepends some data) that provides error detection (and maybe ordering) information. The exact structure of this header would be defined by a protocol such as TCP or UDP.
3. The OS takes all of _that_, and wraps it up in another header that helps with routing. This header would be defined by the IP protocol.
4. The OS hands all that data to the network interface card (the _NIC_–the piece of hardware that’s responsible for networking).
5. The NIC wraps all _that_ data up into another header that’s defined by a protocol such as Ethernet that helps with delivery on the LAN.
6. The NIC sends the entire, multiply-wrapped data out over the wire, or over the air (with WiFi).

When the receiving computer gets the packet, the reverse process happens. Its NIC strips the Ethernet header, the OS makes sure the IP address is correct, figures out which program is listening on that port, and sends it the fully unwrapped data.

----
## An Example of Layering of Protocols on Data

Let’s consider what happens with an HTTP request.

1. The web browser builds the HTTP request that looks like this:
    
    ```
    GET / HTTP/1.1
    Host: example.com
    Connection: close
    ```
    
    And that’s all the browser cares about. It doesn’t care about IP routing or TCP data integrity or Ethernet.
    
    It just says “Send this data to that computer on port 80”.
    
2. The OS takes over and says, “OK, you asked me to send this over a stream-oriented socket, and I’m going to use the TCP protocol to do that and ensure all the data arrives intact and in order.”
    
    So the OS takes the HTTP data and wraps it in a TCP header which includes the port number.
    
3. And then the OS says, “And you wanted to send it to this remote computer whose IP address is 198.51.100.2, so we’ll use the IP protocol to do that.”
    
    And it takes the entire TCP-HTTP data and wraps it up in an IP header. So now we have data that looks like this: IP-TCP-HTTP.
    
4. After that, the OS takes a look at its routing table and decides where to send the data next. Maybe the web server is on the LAN, conveniently. More likely, it’s somewhere else, so the data would be sent to the router for your house destined for the greater Internet.
    
    In either case, it’s going to send the data to a server on the LAN, or to your outbound router, also on the LAN. So it’s going to a computer on the LAN.
    
    And computers on the LAN have an Ethernet address (AKA _MAC address_–which stands for “Media Access Control”), so the sending OS looks up the MAC address that corresponds to the next destination IP address, whether that’s a local web server or the outbound router. (This happens via a lookup in something called the _ARP Cache_, but we’ll get to that part of the story another time.)
    
    And it wraps the whole IP-TCP-HTTP packet in an Ethernet header, so it becomes Ethernet-IP-TCP-HTTP. The web request is still in there, buried under layers of protocols!
    
5. And finally, the data goes out on the wire (even if it’s WiFi, we still say “on the wire”).
    

The computer with the destination MAC address, listening carefully, sees the Ethernet packet on the wire and reads it in. (Ethernet packets are called _Ethernet frames_.)

It strips off the Ethernet header, exposing the IP header below it. It looks at the destination IP address.

1. If the inspecting computer is a server and it has that IP address, its OS strips off the IP header and looks deeper. (If it doesn’t have that IP address, something’s wrong and it discards the packet.)
2. It looks at the TCP header and does all the TCP magic needed to make sure the data isn’t corrupted. If it is, it replies back with the magic TCP incantations, saying, “Hey, I need you to send that data again, please.”
    
    Note that the web browser or server never knows about this TCP conversation that’s happening. It’s all behind the scenes. For all it can see, the data is just magically arriving intact and in order.
    
    The reason is that they’re on a higher layer of the network. They don’t have to worry about routing or anything. The lower layers take care of it.
    
3. If everything’s good with TCP, that header gets stripped and the OS is left with the HTTP data. It wakes up the process (the web server) that was waiting to read it, and gives it the HTTP data.
    

But what if the destination Ethernet address was an intermediate router?

1. The router strips off the Ethernet frame as always.
2. The router looks at the destination IP address. It consults its routing table and decides to which interface to forward the packet.
3. It sends it out to that interface, which wraps it up in another Ethernet frame and sends it to the next router in line.
    (Or maybe it’s not Ethernet! Ethernet is a protocol, and there are other low-level protocols in use with fiber optic lines and so on. This is part of the beauty of these layers of abstraction–you can switch protocols partway through transmission and the HTTP data above it is completely unaware that any such thing has happened.)

----
## The Internet Layer Model
| Layer | Responsibility | Example Protocols |
| ---- | ---- | ---- |
| Application | Structured application data | HTTP, FTP, TFTP, Telnet, SSH, SMTP, POP, IMAP |
| Transport | Data Integrity, packet splitting and reassembly | TCP, UDP |
| Internet | Routing | IP, IPv6, ICMP |
| Link | Physical, signals on wires | Ethernet, PPP, token ring |


## The ISO OSI Network Layer Model

The Internet Layer Model is a special case of this more-detailed model called the ISO OSI model. (Bonus points for being a palindrome.) It’s the International Organization for Standardization Open Systems Interconnect model. I know that “ISO” is not a direct English abbreviation for “International Organization for Standardization”, but I don’t have enough global political influence to change that.

Coming back to reality, the OSI model is like the Internet model, but more granular.

The Internet model maps to the OSI model, like so, with a single layer of the Internet model mapping to multiple layers of the OSI model:

|ISO OSI Layer|Internet Layer|
|---|---|
|Application|Application|
|Presentation|Application|
|Session|Application|
|Transport|Transport|
|Network|Network|
|Data link|Link|
|Physical|Link|
And if we look at the OSI model, we can see some of the protocols that exist at those various layers, similar to what we saw with the Internet model, above.

|ISO OSI Layer|Responsibility|Example Protocols|
|---|---|---|
|Application|Structured application data|HTTP, FTP, TFTP, Telnet, SMTP, POP, IMAP|
|Presentation|Encoding translation, encryption, compression|MIME, SSL/TLS, XDR|
|Session|Suspending, terminating, restarting sessions between computers|Sockets, TCP|
|Transport|Data integrity, packet splitting and reassembly|TCP, UDP|
|Network|Routing|IP IPv6, ICMP|
|Data link|Encapsulation into frames|Ethernet, PPP, SLIP|
|Physical|Physical, signals on wires|Ethernet physical layer, DSL, ISDN|

----
## References
- https://beej.us/guide/bgnet0/html/split/the-layered-network-model.html

----
📂 [[Networking]]