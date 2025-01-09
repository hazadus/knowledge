# Django REST Framework and Vue Versus Django and HTMX | TestDriven.io

![rw-book-cover](https://testdriven.io/static/images/blog/django/django-htmx/drf_vue_vs_django_htmx_social_card.png)

## Metadata
- Author: [[Špela Giacomelli (aka GirlLovesToCode)]]
- Full Title: Django REST Framework and Vue Versus Django and HTMX | TestDriven.io
- Category: #articles
- Document Tags: [[django]] 
- Summary: This article compares the development of an application using Vue and Django REST Framework (DRF) versus HTMX and Django. Vue is praised for its simplicity and focus on the view layer of web applications, while HTMX is gaining popularity for its lightweight and ease of use. The article provides examples of how to build a simple password generator using both combinations. It highlights the differences in state management, complexity, testing, deployment, and other aspects between Vue/DRF and HTMX/Django. Ultimately, the choice depends on the specific requirements and goals of the project.
- URL: https://testdriven.io/blog/drf-vue-vs-django-htmx/

## Highlights
- HTMX focuses on server-driven interactions, passing the data to the server and updating the page based on its response. Vue's primary purpose is to build and manage dynamic user interfaces on the client side. This main difference ripples through every aspect of the development process. ([View Highlight](https://read.readwise.io/read/01jdc0f70v2qg27td6kneev8dz))

- Having two separate projects requires two development environments and a different approach to testing. Vue can be tested either in isolation, where you need to mock backend responses, or with actual responses from backend, in which case you'd need a dedicated testing environment. Tests with a real API tend to be slower and more flaky but closer to reality. HTMX, when added to Django, can be mostly tested using Django's testing tools and supplemented with something like Cypress for the most critical user flows. ([View Highlight](https://read.readwise.io/read/01jdc0f7aspt3k2p9sj8x1h1e8))



----
📂 [[Articles]] | Последнее изменение: 23.11.2024 16:34