# The Multiple Meanings of "Nameserver" and "DNS Resolver"

![rw-book-cover](https://readwise-assets.s3.amazonaws.com/static/images/article1.be68295a7e40.png)

## Metadata
- Author: [[Julia Evans]]
- Full Title: The Multiple Meanings of "Nameserver" and "DNS Resolver"
- Category: #articles
- Document Tags: [[dns]] 
- Summary: The multiple meanings of "nameserver" and "DNS resolver"
- URL: https://jvns.ca/blog/2022/02/14/some-dns-terminology/

## Highlights
- For example, the `getaddrinfo` function from libc doesn’t know how to look up DNS records itself, it just knows to look in `/etc/resolv.conf` and forward the query to whatever DNS server(s) it finds there. ([View Highlight](https://read.readwise.io/read/01jdc0d0pq64hsmcgv27vavcys))

- There are 2 types of nameservers, and which one the term “nameserver” means depends on the context. ([View Highlight](https://read.readwise.io/read/01jdc0d1099yk97ye4tz3p0m7v))

- **Meaning 2\. “recursive” nameservers, also known as “DNS resolvers”** ([View Highlight](https://read.readwise.io/read/01jdc0d1p95b8bdcbrss59dn2e))

- ### meanings of “DNS resolver” ([View Highlight](https://read.readwise.io/read/01jdc0d22jq5m5jm567szgwfqa))

- **Meaning 1b: “stub resolver” (server version)** ([View Highlight](https://read.readwise.io/read/01jdc0d2f9m3azy6fdg92mpap2))

- **Meaning 2: a recursive nameserver (a server)** ([View Highlight](https://read.readwise.io/read/01jdc0d2w38gvsza2cebas4948))



----
📂 [[Articles]] | Последнее изменение: 23.11.2024 16:34