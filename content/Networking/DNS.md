🔗 [[Networking]]

----
## Материалы

- [Beej's Guide: 31 Domain Name System (DNS)](https://beej.us/guide/bgnet0/html/split/domain-name-system-dns.html#domain-name-system-dns)
- [[Brandon Rhodes, John Goerzen (auth.) - Foundations of Python Network Programming_ Third Edition-Apress (2014) 1.pdf]]
- [[Julia Evans - How DNS Works-Julia Evans (2022).pdf]]

## Примеры кода
- https://github.com/hazadus/network-learn/blob/main/dns_resolver/dns_resolver.py
- https://github.com/jvns/tiny-resolver/tree/main

----
The general process for converting a name like `www.example.com` that humans use into an IP address that computers use is called _domain name resolution_, and it provided by a distributed group of servers that comprise the _Domain Name System_, or DNS.
## Domain Name Servers

Usually called _name servers_ for short, these servers contain IP records for the domain in which they are an _authority_. That is, a name server doesn’t have records for the entire world; it just has them for a particular domain or subdomain.

> A _subdomain_ is a domain administered by the owner of a domain. For example, the owner of `example.com` might make subdomains `sub1.example.com` and `sub2.example.com`. These aren’t hosts in this case–but they can have their own hosts, e.g. `host1.sub1.examople.com`, `host2.sub1.example.com`, `somecompy.sub2.example.com`.
> 
> Domain owners can make as many subdomains as they want. They just have to make sure they have a name server set up to handle them.

![[Pasted image 20240303160542.png]]

![[Pasted image 20240303155528.png]]

### DNS Server Hierarchy

![[Pasted image 20240303155604.png]]

### Root Nameservers

We have a number of _root name servers_ that can help us on our way. When we don’t know an IP, we can start with them and ask them to tell us IP, or tell us which other server to ask. More on that process in a minute.

Computers are preconfigured with the IP addresses of the 13 root name servers. These IPs rarely ever change, and only one of them is needed to work. Computers that perform DNS frequently retrieve the list to keep it up to date.

![[Pasted image 20240303155658.png]]

## Example Run

Let’s start by doing a query on a computer called `www.example.com`. We need to know its IP address. We don’t know which name server is responsible for the `example.com` domain. All we know is our list of root name servers.

1. Let’s choose a random root server, say `c.root-servers.net`. We’ll contact it and say, “Hey, we’re looking for `www.example.com`. Can you help us?”
    
    But the root name server doesn’t know that. It says, “I don’t know about that, but I can tell you if you’re looking for any `.com` domain, you can contact any one of these name servers.” It attaches a list of name servers who know about the `.com` domains:
    
    ```
    a.gtld-servers.net
    b.gtld-servers.net
    c.gtld-servers.net
    d.gtld-servers.net
    e.gtld-servers.net
    f.gtld-servers.net
    g.gtld-servers.net
    h.gtld-servers.net
    i.gtld-servers.net
    j.gtld-servers.net
    k.gtld-servers.net
    l.gtld-servers.net
    m.gtld-servers.net
    ```
    
2. So we choose one of the `.com` name servers.
    
    “Hey `h.gtld-servers.net`, we’re looking for `www.example.com`. Can you help us?”
    
    And it answers, “I don’t know that name, but I do know the name servers for `example.com`. You can talk to one of them. It attaches the list of name servers who know about the `example.com` domain:
    
    ```
    a.iana-servers.net
    b.iana-servers.net
    ```
    
3. So we choose one of those servers.
    
    “Hey `a.iana-servers.net`, we’re looking for `www.example.com`. Can you help us?”
    
    And that name server answers, “Yes, I can! I know that name! Its IP address is `93.184.216.34`!”
    

So for any lookup, we start with root name server and it directs us on where to go to find more info. (Unless the information has been cached somewhere, but more on that later.)

![[Pasted image 20240303155402.png]]

## Caching Servers

This way we can avoid overloading the root servers with repeated requests.

1. Ask our resolver library for the IP address. If it has it cached, it will return it.
    
2. If it doesn’t have it, ask our local name server for the IP address. If it has it cached, it will return it.
    
3. If it’s not cached **and** if this name server has another upstream name server, it asks that name server for the answer.
    
4. If it’s not cached **and** if this name server does not have another upstream name server, it goes to the root servers and the process continues as before.
    

With all these possible opportunities to get a cached result, it really helps take the load off the root name servers.

Lots of WiFi routers you get also run caching name servers. So when DHCP configures your computer, your computer uses your router as a DNS server for the computers on your LAN. This gives you a snappy response for DNS lookups since you have a really short ping time to your router.

### Time To Live

Since the IP address for a domain or host might change, we have to have a way to expire cache entries.

This is done through a field in the DNS record called _time to live_ (TTL). This is the number of seconds a server should cache the results. It’s commonly set to 86400 seconds (1 day), but could be more or less depending on how often a zone administrator thinks an IP address will change.

When a cache entry expires, the name server will have to once again ask for the data from upstream or the root servers if someone requests it.

----
## `dig` tool

![[Pasted image 20240303165239.png]]

![[Pasted image 20240303165432.png]]

----

## Record Types

The common record types are:

- `A`: An address record for IPv4. This is the type of record we’ve been talking about this whole time. Answers the question, “What is the IPv4 address for this host or domain?”
- `AAAA`: An address record for IPv6. Answers the question, “What is the IPv6 address for this host or domain?”
- `NS`: A name server record for a particular domain. Answers the question, “What are the name servers answering for this host or domain?”
- `MX`: A mail exchange record. Answers the question, “What computers are responsible for handling mail on this domain?”
- `TXT`: A text record. Holds free-form text information. Is sometimes used for anti-spam purposes and proof-of-ownership of a domain.
- `CNAME`: A canonical name record. Think of this as an alias. Makes the statement, “Domain xyz.example.com is an alias for abc.example.com.”
- `SOA`: A start of authority record. This contains information about a domain, including its main name server and contact information.

There are [a lot of DNS record types](https://en.wikipedia.org/wiki/List_of_DNS_record_types).
### A & AAAA records

![[Pasted image 20240303175111.png]]

### CNAME records

![[Pasted image 20240303184411.png]]

### MX records

![[Pasted image 20240303184513.png]]

### TXT records

![[Pasted image 20240303184647.png]]

## Dynamic DNS

Typical users of the Internet don’t have a _static IP address_ (that is, dedicated or unchanging) at their house. If they reboot their modem, their ISP might hand them a different IP address.

This causes a ruckus with DNS because any DNS records pointing to their public IPs would be out of date.

Dynamic DNS (DDNS) aims to solve this problem.

In a nutshell, there are two mechanisms at play:

1. A way for a client to tell the DDNS server what their IP address is.
2. A very short TTL on the DDNS server for that record.

While DNS defines a way to send update records, a common other way is for a computer on your LAN to periodically (e.g. every 10 minutes) contact the DDNS provider with an authenticated HTTP request. The DDNS server will see the IP address it came from and use that to update its record.