🔗 [[Security]]

----
**OWASP** – The Open Worldwide Application Security Project (OWASP) is a nonprofit foundation that works to improve the security of software.

## API Security Top 10 2023

Проблемы и риски перечислены на [сайте OWASP](https://owasp.org/www-project-api-security/). В описании каждого риска также есть описание возможных атак и путей устранения данного риска.

### API1:2023 Broken Object Level Authorization

Every API endpoint that receives an ID of an object, and performs any action on the object, should implement object-level authorization checks. The checks should validate that the logged-in user has permissions to perform the requested action on the requested object.

Failures in this mechanism typically lead to unauthorized information disclosure, modification, or destruction of all data.

### API2:2023 Broken Authentication

An API is vulnerable if it:

- Permits credential stuffing where the attacker uses brute force with a list of valid usernames and passwords.
- Permits attackers to perform a brute force attack on the same user account, without presenting captcha/account lockout mechanism.
- Permits weak passwords.
- Sends sensitive authentication details, such as auth tokens and passwords in the URL.
- Allows users to change their email address, current password, or do any other sensitive operations without asking for password confirmation.
- Doesn't validate the authenticity of tokens.
- Accepts unsigned/weakly signed JWT tokens (`{"alg":"none"}`)
- Doesn't validate the JWT expiration date.
- Uses plain text, non-encrypted, or weakly hashed passwords.
- Uses weak encryption keys.

On top of that, a microservice is vulnerable if:

- Other microservices can access it without authentication
- Uses weak or predictable tokens to enforce authentication

### [API3:2023 - Broken Object Property Level Authorization](https://owasp.org/API-Security/editions/2023/en/0xa3-broken-object-property-level-authorization/)

When allowing a user to access an object using an API endpoint, it is important to validate that the user has access to the specific object properties they are trying to access.

An API endpoint is vulnerable if:

- The API endpoint exposes properties of an object that are considered sensitive and should not be read by the user.
- The API endpoint allows a user to change, add/or delete the value of a sensitive object's property which the user should not be able to access.

### [API4:2023 - Unrestricted Resource Consumption](https://owasp.org/API-Security/editions/2023/en/0xa4-unrestricted-resource-consumption/)

Satisfying API requests requires resources such as network bandwidth, CPU, memory, and storage. Sometimes required resources are made available by service providers via API integrations, and paid for per request, such as sending emails/SMS/phone calls, biometrics validation, etc.

An API is vulnerable if at least one of the following limits is missing or set inappropriately (e.g. too low/high):

- Execution timeouts
- Maximum allocable memory
- Maximum number of file descriptors
- Maximum number of processes
- Maximum upload file size
- Number of operations to perform in a single API client request (e.g. GraphQL batching)
- Number of records per page to return in a single request-response
- Third-party service providers' spending limit

### [API5:2023 - Broken Function Level Authorization](https://owasp.org/API-Security/editions/2023/en/0xa5-broken-function-level-authorization/)

The best way to find broken function level authorization issues is to perform a deep analysis of the authorization mechanism while keeping in mind the user hierarchy, different roles or groups in the application, and asking the following questions:

- Can a regular user access administrative endpoints?
- Can a user perform sensitive actions (e.g. creation, modification, or deletion ) that they should not have access to by simply changing the HTTP method (e.g. from `GET` to `DELETE`)?
- Can a user from group X access a function that should be exposed only to users from group Y, by simply guessing the endpoint URL and parameters (e.g. `/api/v1/users/export_all`)?

Don't assume that an API endpoint is regular or administrative only based on the URL path.

While developers might choose to expose most of the administrative endpoints under a specific relative path, like `/api/admins`, it's very common to find these administrative endpoints under other relative paths together with regular endpoints, like `/api/users`.

### [API6:2023 - Unrestricted Access to Sensitive Business Flows](https://owasp.org/API-Security/editions/2023/en/0xa6-unrestricted-access-to-sensitive-business-flows/)

When creating an API Endpoint, it is important to understand which business flow it exposes. Some business flows are more sensitive than others, in the sense that excessive access to them may harm the business.

Common examples of sensitive business flows and risk of excessive access associated with them:

- Purchasing a product flow - an attacker can buy all the stock of a high-demand item at once and resell for a higher price (scalping)
- Creating a comment/post flow - an attacker can spam the system
- Making a reservation - an attacker can reserve all the available time slots and prevent other users from using the system

The risk of excessive access might change between industries and businesses. For example - creation of posts by a script might be considered as a risk of spam by one social network, but encouraged by another social network.

An API Endpoint is vulnerable if it exposes a sensitive business flow, without appropriately restricting the access to it.

### [API7:2023 - Server Side Request Forgery](https://owasp.org/API-Security/editions/2023/en/0xa7-server-side-request-forgery/)

Server-Side Request Forgery (SSRF) flaws occur when an API is fetching a remote resource without validating the user-supplied URL. It enables an attacker to coerce the application to send a crafted request to an unexpected destination, even when protected by a firewall or a VPN.

Modern concepts in application development make SSRF more common and more dangerous.

More common - the following concepts encourage developers to access an external resource based on user input: Webhooks, file fetching from URLs, custom SSO, and URL previews.

More dangerous - Modern technologies like cloud providers, Kubernetes, and Docker expose management and control channels over HTTP on predictable, well-known paths. Those channels are an easy target for an SSRF attack.

It is also more challenging to limit outbound traffic from your application, because of the connected nature of modern applications.

The SSRF risk can not always be completely eliminated. While choosing a protection mechanism, it is important to consider the business risks and needs.

### [API8:2023 - Security Misconfiguration](https://owasp.org/API-Security/editions/2023/en/0xa8-security-misconfiguration/)

The API might be vulnerable if:

- Appropriate security hardening is missing across any part of the API stack, or if there are improperly configured permissions on cloud services
- The latest security patches are missing, or the systems are out of date
- Unnecessary features are enabled (e.g. HTTP verbs, logging features)
- There are discrepancies in the way incoming requests are processed by servers in the HTTP server chain
- Transport Layer Security (TLS) is missing
- Security or cache control directives are not sent to clients
- A Cross-Origin Resource Sharing (CORS) policy is missing or improperly set
- Error messages include stack traces, or expose other sensitive information

### [API9:2023 - Improper Inventory Management](https://owasp.org/API-Security/editions/2023/en/0xa9-improper-inventory-management/)

The sprawled and connected nature of APIs and modern applications brings new challenges. It is important for organizations not only to have a good understanding and visibility of their own APIs and API endpoints, but also how the APIs are storing or sharing data with external third parties.

Running multiple versions of an API requires additional management resources from the API provider and expands the attack surface.

An API has a "documentation blindspot" if:

- The purpose of an API host is unclear, and there are no explicit answers to the following questions
- Which environment is the API running in (e.g. production, staging, test, development)?
- Who should have network access to the API (e.g. public, internal, partners)?
- Which API version is running?
- There is no documentation or the existing documentation is not updated.
- There is no retirement plan for each API version.
- The host's inventory is missing or outdated.

The visibility and inventory of sensitive data flows play an important role as part of an incident response plan, in case a breach happens on the third party side.

An API has a "data flow blindspot" if:

- There is a "sensitive data flow" where the API shares sensitive data with a third party and
- There is not a business justification or approval of the flow
- There is no inventory or visibility of the flow
- There is not deep visibility of which type of sensitive data is shared

### [API10:2023 - Unsafe Consumption of APIs](https://owasp.org/API-Security/editions/2023/en/0xaa-unsafe-consumption-of-apis/)

Developers tend to trust data received from third-party APIs more than user input. This is especially true for APIs offered by well-known companies. Because of that, developers tend to adopt weaker security standards, for instance, in regards to input validation and sanitization.

The API might be vulnerable if:

- Interacts with other APIs over an unencrypted channel;
- Does not properly validate and sanitize data gathered from other APIs prior to processing it or passing it to downstream components;
- Blindly follows redirections;
- Does not limit the number of resources available to process third-party services responses;
- Does not implement timeouts for interactions with third-party services;



----
📂 [[Security]]