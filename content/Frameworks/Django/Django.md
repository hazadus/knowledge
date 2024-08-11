📂 [[Python]] | [[Frameworks]]

----

# Development
## Tips and Best Practices
- Always include migrations in VCS (_p.70 2scoops_)
- Always set `objects = models.Manager()` above any custom manager that has a new name (_p.80 2Scoops_) ([https://docs.djangoproject.com/en/4.1/topics/db/managers/](https://docs.djangoproject.com/en/4.1/topics/db/managers/) )

> [!info] Django Best Practices: Function-Based Views vs Class-Based Views  
> Django's use of both function-based views (FBVs) and class-based views (CBVs) causes a lot of confusion for newcomers.  
> [https://learndjango.com/tutorials/django-best-practices-function-based-views-vs-clas](https://learndjango.com/tutorials/django-best-practices-function-based-views-vs-clas)  

> [!info] Django Views - The Right Way  
> Welcome to my opinionated guide on how to write views in Django!  
> [https://spookylukey.github.io/django-views-the-right-way/](https://spookylukey.github.io/django-views-the-right-way/)  

> [!info] Building a higher-level query API: the right way to use Django's ORM  
> Note: this post refers to a very old version of Django.  
> [https://www.dabapps.com/blog/higher-level-query-api-django-orm/](https://www.dabapps.com/blog/higher-level-query-api-django-orm/)  

> [!info] Boring Python: code quality  
> This is the second in a series of posts I intend to write about how to build, deploy, and manage Python applications in as boring a way as possible.  
> [https://www.b-list.org/weblog/2022/dec/19/boring-python-code-quality/?utm_campaign=Django%2BNewsletter&utm_medium=email&utm_source=Django_Newsletter_159](https://www.b-list.org/weblog/2022/dec/19/boring-python-code-quality/?utm_campaign=Django%2BNewsletter&utm_medium=email&utm_source=Django_Newsletter_159)  
### Selecting technologies for your project

> [!info] A Failed SaaS Postmortem · Matt Layman  
> My Software as a Service failed.  
> [https://www.mattlayman.com/blog/2019/failed-saas-postmortem/](https://www.mattlayman.com/blog/2019/failed-saas-postmortem/)  
### Рекомендации куратора

> [!info] What is the difference between null=True and blank=True in Django?  
> When we add a model field in Django we generally write: models.  
> [https://stackoverflow.com/questions/8609192/what-is-the-difference-between-null-true-and-blank-true-in-django](https://stackoverflow.com/questions/8609192/what-is-the-difference-between-null-true-and-blank-true-in-django)  

> [!info] Кастомизация админ-панели Django  
> Содержание Фреймворк Django поставляется с мощным инструментом администрирования под названием admin.  
> [https://pythonist.ru/kastomizacziya-admin-paneli-django/#Modifying%20a%20Change%20List%20Using%20list_display](https://pythonist.ru/kastomizacziya-admin-paneli-django/#Modifying%20a%20Change%20List%20Using%20list_display)  
## Dev Workflow
[[Django Workflow]]

> [!info] Local web development vs Vagrant vs Docker: What's right for you? · Matt Layman  
> Web development is full of tools that claim to help you develop your perfect application.  
> [https://www.mattlayman.com/blog/2019/web-development-environments/](https://www.mattlayman.com/blog/2019/web-development-environments/)  
## Tools
References to tools.

> [!info] Flake8: Your Tool For Style Guide Enforcement - flake8 5.0.4 documentation  
> It is very important to install Flake8 on the correct version of Python for your needs.  
> [https://flake8.pycqa.org/en/latest/index.html#quickstart](https://flake8.pycqa.org/en/latest/index.html#quickstart)  
Test the site under load:

> [!info] Getting started - Locust 2.14.0 documentation  
> A Locust test is essentially a Python program.  
> [https://docs.locust.io/en/stable/quickstart.html#quickstart](https://docs.locust.io/en/stable/quickstart.html#quickstart)  
## Coding Style / Design Philosophies
References to resources on coding style.

> [!info] Coding style | Django documentation | Django  
> Please follow these coding standards when writing code for inclusion in Django.  
> [https://docs.djangoproject.com/en/4.1/internals/contributing/writing-code/coding-style/](https://docs.djangoproject.com/en/4.1/internals/contributing/writing-code/coding-style/)  

> [!info] Design philosophies | Django documentation | Django  
> A fundamental goal of Django's stack is loose coupling and tight cohesion.  
> [https://docs.djangoproject.com/en/dev/misc/design-philosophies/](https://docs.djangoproject.com/en/dev/misc/design-philosophies/)  

> [!info] Code Guide  
> Standards for developing consistent, flexible, and sustainable HTML and CSS.  
> [https://codeguide.co/#html-syntax](https://codeguide.co/#html-syntax)  
### Docstrings

> [!info] PEP 257 – Docstring Conventions | peps.python.org  
> Python Enhancement Proposals (PEPs)  
> [https://peps.python.org/pep-0257/](https://peps.python.org/pep-0257/)  

> [!info] Writing docstrings — Sphinx-RTD-Tutorial documentation  
>  
> [https://sphinx-rtd-tutorial.readthedocs.io/en/latest/docstrings.html#the-sphinx-docstring-format](https://sphinx-rtd-tutorial.readthedocs.io/en/latest/docstrings.html#the-sphinx-docstring-format)  
---
## References

> [!info] Django Forum  
> Discussion of the Django framework  
> [https://forum.djangoproject.com](https://forum.djangoproject.com)  

> [!info] Django Class-Based-View Inspector -- Classy CBV  
> Detailed descriptions, with full methods and attributes, for each of Django's class-based generic views.  
> [https://ccbv.co.uk](https://ccbv.co.uk)  

> [!info] GitHub - jasonvriends/django-starter: A starter project for django  
> Starting a Django project from scratch is no easy task.  
> [https://github.com/jasonvriends/django-starter](https://github.com/jasonvriends/django-starter)  
From author: I created a Django [starter project 4](https://github.com/jasonvriends/django-starter) and would like to share in case anyone has any improvements. **For references.**

> [!info] GitHub - wsvincent/djangox: Django starter project with 🔋  
> A batteries-included Django starter project.  
> [https://github.com/wsvincent/djangox](https://github.com/wsvincent/djangox)  
WSV starter project. **For references.**
## Database

> [!info] Django ORM Cheatsheet: Mastering Database Operations in Django  
> Django, as a powerful and popular web framework, comes equipped with an impressive Object-Relational Mapping (ORM) system that simplifies database interactio  
> [https://djangocentral.com/django-orm-cheatsheet/](https://djangocentral.com/django-orm-cheatsheet/)  

> [!info] How to Filter Django QuerySets - 15 Examples For Beginners - CTRL Z Blog  
> A tutorial on creating QuerySets with Django ORM and filtering the data.  
> [https://ctrlzblog.com/django-queryset-filter-15-examples/?utm_campaign=Django%2BNewsletter&utm_medium=email&utm_source=Django_Newsletter_152](https://ctrlzblog.com/django-queryset-filter-15-examples/?utm_campaign=Django%2BNewsletter&utm_medium=email&utm_source=Django_Newsletter_152)  
Incl exists()

> [!info] Mastering Django: Advanced Models - Mastering Django  
> In this chapter, we'll dig much deeper into Django's models and comprehensively explore the essentials.  
> [https://masteringdjango.com/django-tutorials/mastering-django-advanced-models/](https://masteringdjango.com/django-tutorials/mastering-django-advanced-models/)  

> [!info] Aggregation | Django documentation | Django  
> The topic guide on Django's database-abstraction API described the way that you can use Django queries that create, retrieve, update and delete individual objects.  
> [https://docs.djangoproject.com/en/4.1/topics/db/aggregation/](https://docs.djangoproject.com/en/4.1/topics/db/aggregation/)  
[https://stackoverflow.com/questions/43770118/simple-subquery-with-outerref](https://stackoverflow.com/questions/43770118/simple-subquery-with-outerref)
### contenttypes

> [!info] The contenttypes framework | Django documentation | Django  
> Django includes a application that can track all of the models installed in your Django-powered project, providing a high-level, generic interface for working with your models.  
> [https://docs.djangoproject.com/en/4.1/ref/contrib/contenttypes/](https://docs.djangoproject.com/en/4.1/ref/contrib/contenttypes/)  
Together, [`**get_object_for_this_type()**`](https://docs.djangoproject.com/en/4.1/ref/contrib/contenttypes/#django.contrib.contenttypes.models.ContentType.get_object_for_this_type) and [`**model_class()**`](https://docs.djangoproject.com/en/4.1/ref/contrib/contenttypes/#django.contrib.contenttypes.models.ContentType.model_class) enable two extremely important use cases:
1. Using these methods, you can write high-level generic code that performs queries on any installed model – instead of importing and using a single specific model class, you can pass an `**app_label**` and `**model**` into a [`**ContentType**`](https://docs.djangoproject.com/en/4.1/ref/contrib/contenttypes/#django.contrib.contenttypes.models.ContentType) lookup at runtime, and then work with the model class or retrieve objects from it.
2. You can relate another model to [`**ContentType**`](https://docs.djangoproject.com/en/4.1/ref/contrib/contenttypes/#django.contrib.contenttypes.models.ContentType) as a way of tying instances of it to particular model classes, and use these methods to get access to those model classes.
Adding a foreign key from one of your own models to [`**ContentType**`](https://docs.djangoproject.com/en/4.1/ref/contrib/contenttypes/#django.contrib.contenttypes.models.ContentType) allows your model to effectively tie itself to another model class, as in the example of the [`**Permission**`](https://docs.djangoproject.com/en/4.1/ref/contrib/auth/#django.contrib.auth.models.Permission)model above. But it’s possible to go one step further and use [`**ContentType**`](https://docs.djangoproject.com/en/4.1/ref/contrib/contenttypes/#django.contrib.contenttypes.models.ContentType)to enable truly generic (sometimes called “polymorphic”) relationships between models.
## Templates

> [!info] Built-in template tags and filters | Django documentation | Django  
> This document describes Django's built-in template tags and filters.  
> [https://docs.djangoproject.com/en/4.1/ref/templates/builtins/](https://docs.djangoproject.com/en/4.1/ref/templates/builtins/)  

> [!info] How to create custom template tags and filters | Django documentation | Django  
> Django's template language comes with a wide variety of built-in tags and filters designed to address the presentation logic needs of your application.  
> [https://docs.djangoproject.com/en/4.1/howto/custom-template-tags/#how-to-create-custom-template-tags-and-filters](https://docs.djangoproject.com/en/4.1/howto/custom-template-tags/#how-to-create-custom-template-tags-and-filters)  

> [!info] Markdown: Basics  
> This page offers a brief overview of what it's like to use Markdown.  
> [https://daringfireball.net/projects/markdown/basics](https://daringfireball.net/projects/markdown/basics)  
## Flat pages

> [!info] Django  
> Django comes with an optional "flatpages" application.  
> [https://docs.djangoproject.com/en/4.1/ref/contrib/flatpages/](https://docs.djangoproject.com/en/4.1/ref/contrib/flatpages/)  

> [!info] How to Use Django's Flatpages App  
> Django ships with a Flatpages application that enables the user to create flat HTML pages and store it in the database.  
> [https://simpleisbetterthancomplex.com/tutorial/2016/10/04/how-to-use-django-flatpages-app.html](https://simpleisbetterthancomplex.com/tutorial/2016/10/04/how-to-use-django-flatpages-app.html)  
## Serving Static Files
[Serving Static Files · Matt Layman](https://www.mattlayman.com/understand-django/serving-static-files/)
[WhiteNoise 6.2.0 documentation (evans.io)](http://whitenoise.evans.io/en/stable/) \#try_out
## Views

> [!info] Django Best Practices: Function-Based Views vs Class-Based Views  
> Django's use of both function-based views (FBVs) and class-based views (CBVs) causes a lot of confusion for newcomers.  
> [https://learndjango.com/tutorials/django-best-practices-function-based-views-vs-clas](https://learndjango.com/tutorials/django-best-practices-function-based-views-vs-clas)  

> [!info] Django Views - The Right Way  
> Welcome to my opinionated guide on how to write views in Django!  
> [https://spookylukey.github.io/django-views-the-right-way/](https://spookylukey.github.io/django-views-the-right-way/)  
### Request and Response objects

> [!info] Request and response objects | Django documentation | Django  
> Passing strings Typical usage is to pass the contents of the page, as a string, bytestring, or , to the constructor: But if you want to add content incrementally, you can use as a file-like object: Passing iterators Finally, you can pass HttpResponse an iterator rather than strings.  
> [https://docs.djangoproject.com/en/4.1/ref/request-response/#django.http.HttpRequest](https://docs.djangoproject.com/en/4.1/ref/request-response/#django.http.HttpRequest)  
### Function Based Views
**HttpRequest** is passed into each view as a parameter…
View must return **HttpResponse**.
### Class Based Views

> [!info] Django Class-Based-View Inspector -- Classy CBV  
> Detailed descriptions, with full methods and attributes, for each of Django's class-based generic views.  
> [https://ccbv.co.uk](https://ccbv.co.uk)  
### Pagination

> [!info] Pagination in Django  
> Pagination is the process of breaking large chunks of data up across multiple, discrete web pages.  
> [https://testdriven.io/blog/django-pagination/](https://testdriven.io/blog/django-pagination/)  
---
## Forms
[https://www.mattlayman.com/understand-django/user-interaction-forms](https://www.mattlayman.com/understand-django/user-interaction-forms)

> [!info] Classy Django Forms  
> Detailed descriptions, with full methods, properties and attributes, for each form class.  
> [https://cdf.9vo.lt/](https://cdf.9vo.lt/)  
## Admin panel

> [!info] Кастомизация админ-панели Django  
> Содержание Фреймворк Django поставляется с мощным инструментом администрирования под названием admin.  
> [https://pythonist.ru/kastomizacziya-admin-paneli-django/#Modifying%20a%20Change%20List%20Using%20list_display](https://pythonist.ru/kastomizacziya-admin-paneli-django/#Modifying%20a%20Change%20List%20Using%20list_display)  
JSON formatting, read-only fields: [Pretty Formatting JSON in the Django Admin (feldroy.com)](https://daniel.feldroy.com/posts/pretty-formatting-json-django-admin)
## Custom [manage.py](http://manage.py) commands

> [!info] Django  
> Applications can register their own actions with .  
> [https://docs.djangoproject.com/en/4.1/howto/custom-management-commands/](https://docs.djangoproject.com/en/4.1/howto/custom-management-commands/)  

> [!info] Command Your App · Matt Layman  
> In the last Understand Django article, we dug into file management.  
> [https://www.mattlayman.com/understand-django/command-apps/](https://www.mattlayman.com/understand-django/command-apps/)  
## Middleware
Built-in middleware reference: [https://docs.djangoproject.com/en/4.1/ref/middleware/](https://docs.djangoproject.com/en/4.1/ref/middleware/)
Creating your own middleware: [https://docs.djangoproject.com/en/4.1/topics/http/middleware/#writing-your-own-middleware](https://docs.djangoproject.com/en/4.1/topics/http/middleware/#writing-your-own-middleware)

> [!info] Middleware Do You Go? · Matt Layman  
> In the previous Understand Django article, we covered the built-in auth system.  
> [https://www.mattlayman.com/understand-django/middleware-do-you-go/](https://www.mattlayman.com/understand-django/middleware-do-you-go/)  
## Context Processors
Example: cart in eshop [https://github.com/hazadus/django-eshop/commit/125871efdb83a9be2f3f0bafa773ecd54afea152#](https://github.com/hazadus/django-eshop/commit/125871efdb83a9be2f3f0bafa773ecd54afea152#)
## Managing Files

> [!info] Django  
> This document describes Django's file access APIs for files such as those uploaded by a user.  
> [https://docs.djangoproject.com/en/4.1/topics/files/](https://docs.djangoproject.com/en/4.1/topics/files/)  
## Storages

> [!info] User File Use · Matt Layman  
> In the last Understand Django article, you learned about Django settings and how to manage the configuration of your application.  
> [https://www.mattlayman.com/understand-django/media-files/](https://www.mattlayman.com/understand-django/media-files/)  
## Authentication
### User registration
![[attachments/Untitled 17.png|Untitled 17.png]]
FBV for sign up + login
`UserCreationForm` – Django built-in [https://docs.djangoproject.com/en/4.1/topics/auth/default/#django.contrib.auth.forms.UserCreationForm](https://docs.djangoproject.com/en/4.1/topics/auth/default/#django.contrib.auth.forms.UserCreationForm)
![[attachments/Untitled 1 6.png|Untitled 1 6.png]]
Adding fields to UserCreationForms
### Extending User model with profile model
![[attachments/Untitled 2 5.png|Untitled 2 5.png]]
Note OneToOneField
![[attachments/Untitled 3 4.png|Untitled 3 4.png]]
Add profile fields to the registration form
![[attachments/Untitled 4 3.png|Untitled 4 3.png]]
Save profile data in view
### Check user permissions in view
![[attachments/Untitled 5 3.png|Untitled 5 3.png]]
![[attachments/Untitled 6 3.png|Untitled 6 3.png]]
Same with decorator
### Adding permissions to models
![[attachments/Untitled 7 2.png|Untitled 7 2.png]]
---
## HTMX

> [!info] How To Use Htmx In Django · Matt Layman  
> This article shows you how to use htmx in Django.  
> [https://www.mattlayman.com/blog/2021/how-to-htmx-django/](https://www.mattlayman.com/blog/2021/how-to-htmx-django/)  
# Deployment
## Check
```Bash
python manage.py check --deploy --fail-level WARNING
```
## Tutorials

> [!info] Deploy A Site Live · Matt Layman  
> In the previous Understand Django article, we looked at automated testing and how writing tests to check your Django project can be very valuable, saving you time and making sure your site works for your users.  
> [https://www.mattlayman.com/understand-django/deploy-site-live/](https://www.mattlayman.com/understand-django/deploy-site-live/)  

> [!info] How To Set Up Django with Postgres, Nginx, and Gunicorn on Ubuntu 22.04 | DigitalOcean  
> Django is a powerful web framework that can help you get your Python application or website off the ground.  
> [https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-22-04](https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-22-04)  

> [!info] Deployment checklist | Django documentation | Django  
> The internet is a hostile environment.  
> [https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/](https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/)  

> [!info] How to manage static files (e.g. images, JavaScript, CSS) | Django documentation | Django  
> Websites generally need to serve additional files such as images, JavaScript, or CSS.  
> [https://docs.djangoproject.com/en/4.1/howto/static-files/](https://docs.djangoproject.com/en/4.1/howto/static-files/)  

> [!info] How to serve static and media files in NGINX for your Django Project  
> Serve Static Files and Media Files of your Django App using NGINX Setting up Django Applications is tedious and challenging for a beginner.  
> [https://wolfx.io/how-to-serve-static-and-media-files-in-nginx](https://wolfx.io/how-to-serve-static-and-media-files-in-nginx)  

> [!info] Масштабирование и обеспечение безопасности приложения Django | Блог Timeweb Cloud  
> С расширением инфраструктуры перед компанией встает задача масштабирования.  
> [https://timeweb.cloud/blog/masshtabirovanie-django?utm_source=email&utm_medium=info&utm_campaign=digest&utm_content=september22](https://timeweb.cloud/blog/masshtabirovanie-django?utm_source=email&utm_medium=info&utm_campaign=digest&utm_content=september22)  
---
## WSGI

> [!info]  
>  
> [https://ru.wikipedia.org/wiki/WSGI](https://ru.wikipedia.org/wiki/WSGI)  

> [!info] Building Your Own Python Web Framework - WSGI  
> Home Building Your Own Python Web Framework Part 1 WSGI Part 1, Chapter 2 Before we dive into the details of WSGI, let's look at what happens when a user uses a web application from a bird-eye's view.  
> [https://testdriven.io/courses/python-web-framework/wsgi/](https://testdriven.io/courses/python-web-framework/wsgi/)  
## Tools
### Sentry.io
```Bash
pip install --upgrade sentry-sdk
```
```Bash
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration
sentry_sdk.init(
    dsn="https://66d01eead24546f8b45208e98006be35@o1402378.ingest.sentry.io/4504076515999744",
    integrations=[
        DjangoIntegration(),
    ],
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0,
    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True
)
```

----
📂 [[Django]]