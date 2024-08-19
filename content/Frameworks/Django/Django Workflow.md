## Create project
```Bash
$ cd ~/projects
$ mkdir django-project-name
$ cd django-project-name
$ python3 -m venv .venv
$ source .venv/bin/activate
$ python3 -m pip install django
$ python3 -m pip install gunicorn
# Note the dot at the end of the line below:
$ django-admin startproject django_project .
$ python3 manage.py startapp app-name
$ touch README.md
$ touch .gitignore
# Do not initial migrate before you create Custom User Model!
$ python3 manage.py migrate
$ mkdir templates
$ python -m pip freeze > requirements.txt
$ python manage.py runserver
```
```Bash
.venv/
.idea/
media/
__pycache__/
.DS_Store
.env
*.pyc
db.sqlite3
```
### Configure git
```Bash
$ git status
$ git init
```
NB: do `git add .` and initial commit after removing secrets from `settings.py`!
## Change basic project settings
### Use env vars for settings
```Bash
import secrets
print(secrets.token_urlsafe())
```
```Bash
# python -m pip install 'environs[django]'
# environs==9.5.0
from environs import Env
env = Env()
env.read_env()
...
SECRET_KEY = env.str("SECRET_KEY")
DEBUG = env.bool("DEBUG", False)
```
```Bash
DEBUG=True
SECRET_KEY=VsjFqreIGNU...........FWi7aziSvzRZ1M_cP-vKbI
```
### Set template paths, etc.
```Python
INSTALLED_APPS = [
		...,
    'posts.apps.PostsConfig',  # new
]
LANGUAGE_CODE = 'ru-RU'
TIME_ZONE = "Europe/Moscow"
AUTH_USER_MODEL = "accounts.CustomUser"  # new

ALLOWED_HOSTS = ['localhost', '127.0.0.1']  # + add prod host name
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],
...
# Before deploy:
ALLOWED_HOSTS = ['85.193.89.177', 'localhost', '127.0.0.1']
CSRF_TRUSTED_ORIGINS = ['http://85.193.89.177','http://*.127.0.0.1']
ALLOWED_HOSTS = ['85.193.89.177', 'localhost', '127.0.0.1']
CSRF_TRUSTED_ORIGINS = ['http://85.193.89.177','http://*.127.0.0.1']

STATIC_ROOT = 'staticfiles/'
STATIC_URL = 'static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
		# BASE_DIR / 'static',
)
# This is for uploads (added by me):
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# or MEDIA_ROOT = BASE_DIR / 'media'
```
```Python
from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('posts.urls')),
]
```
### Create CustomUser model
See “Django for Professionals” page 55.
NB: add GitHub link to my demo project, too.
```Bash
python manage.py startapp accounts
# ... edit accounts/models.py
# ... edit accounts/forms.py
# ... edit accounts/admin.py
```
```Python
# accounts/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    address = models.TextField("Delivery address", null=True, blank=True)
    def __str__(self):
        return self.username
```
```Python
# settings.py
# add new setting:
AUTH_USER_MODEL = "accounts.CustomUser"
```
```Python
# accounts/forms.py
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        # The password field is implicitly included, no need to explicitly include it
        fields = (
            "email",
            "username",
        )

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        # The password field is implicitly included, no need to explicitly include it
        fields = (
            "email",
            "username",
            "address",
        )
```
```Python
# accounts/admin.py
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
custom_user = get_user_model()

class CustomUserAdmin(UserAdmin):
    """
    Configures admin panel views for CustomUsers.
    https://docs.djangoproject.com/en/4.1/ref/contrib/admin/\#modeladmin-options
    """
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = custom_user
    # Which fields will be listed in admin section (on the list, not 'details' page):
    list_display = [
        "email",
        "username",
        "is_superuser",
        "address",
    ]
    # Which fields to show when editing user via admin panel:
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("address",)}), )
    # Which fields to show when creating user via admin panel:
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("address",)}), )

admin.site.register(custom_user, CustomUserAdmin)
```
After creating CustomUser, we can safely do the initial migration!
### Initial Migrations
```Bash
python manage.py makemigrations
python manage.py migrate
```
Don’t forget to add all migrations to git!
### Add superuser
```Bash
python manage.py createsuperuser
```
## Add model, view, url
```Python
from django.urls import path
from .views import HomePageView
urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
]
```
```Python
from django.db import models

class Post(models.Model):
    text = models.TextField()
    def __str__(self):
        return self.text[:50]
```
```Python
# Add new model to Admin page
from django.contrib import admin
from .models import Post
admin.site.register(Post)
```
```Bash
$ python manage.py makemigrations app-name
$ python manage.py migrate
```
```Python
from django.views.generic import ListView
from .models import Post

class HomePageView(ListView):
    model = Post
    template_name = "home.html"
```
```Python
# FBVs example
from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponse
from .models import Category, Product

def product_list(request: HttpRequest, category_slug=None) -> HttpResponse:
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, "shop/product_list.html", {
        "category": category,
        "categories": categories,
        "products": products
    })
```
```HTML
<h1>Message Board Homepage</h1>
<ul>
    {% for post in post_list %}
        <li>{{  post.text }}</li>
    {% endfor %}
</ul>
```
## Add static files folder
```Python
# Project's settings.py (bottom):
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
```
```HTML
{% load static %}
<html>
    <head>
        <title>Django Blog App</title>
    </head>
    <body>
        <header>
            <h1><a href="{% url 'home' %}">Django Blog - Home</a></h1>
            <link rel="stylesheet" href="{% static 'css/base.css' %}">
        </header>
...
```
## File Uploads
### Upload and process files
- Example from python_django/09_Files
    
    ```Python
    # forms.py
    from django import forms
    
    class UploadPostsForm(forms.Form):
        file = forms.FileField(label="Выберите файл в формате CSV на вашем устройстве")
    
    
    
    # views.py
    @login_required
    def upload_posts(request: HttpRequest) -> HttpResponse:
        context = {}
    
        if request.method == "POST":
            upload_form = UploadPostsForm(request.POST, request.FILES)
    
            if upload_form.is_valid():
                # Note that file itself is not saved in MEDIA dir!
                file = upload_form.cleaned_data["file"].read()
                # Don't forget to split rows for csv reader:
                file_str = file.decode("utf-8").split("\n")
                csv_reader = reader(file_str, delimiter="|", quotechar='"')
    
                csv_errors = []
                new_posts = []
                for num, row in enumerate(csv_reader):
                    # Check number of rows in line:
                    if not len(row) == 3:
                        csv_errors.append("Строка {line}: неверный формат строки.".format(
                            line=num+1
                        ))
                        continue
    
                    # Try to parse datetime:
                    try:
                        post_date = datetime.strptime(row[1], "%d.%m.%Y %H:%M")
                        print(num, post_date)
                    except:
                        csv_errors.append("Строка {line}: неверный формат даты.".format(
                            line=num+1
                        ))
                        continue
    
                    # Add blog post if data is OK:
                    new_post = Post.objects.create(
                        title=row[0],
                        body=row[2],
                        author=request.user
                    )
                    # Overwrite 'auto_now_add' datetime value on 'created' field and save again:
                    new_post.created = post_date
                    new_post.save()
                    new_posts.append(new_post)
    
    
                context["filename"] = upload_form.cleaned_data["file"].name
                context["csv_errors"] = csv_errors
                context["new_posts"] = new_posts
        else:
            upload_form = UploadPostsForm()
    
        context["form"] = upload_form
        return render(request, "post_upload.html", context=context)
    ```
    
## Add tests
```Python
from django.test import TestCase
from django.urls import reverse
from .models import Post

class PostTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        """
        Put some data into DB for test.
        """
        cls.post = Post.objects.create(text="This is a test!")
    def test_model_content(self):
        """
        Check if the test data exists in DB.
        """
        self.assertEqual(self.post.text, "This is a test!")
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
		# Following three test can be combined in one:
    def test_url_available_by_name(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
    def test_template_name_correct(self):
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "home.html")
    def test_template_content(self):
        response = self.client.get(reverse("home"))
        self.assertContains(response, "<h1>Message Board Homepage</h1>")
```
```Bash
# Run tests
$ python manage.py test
```
## Internationalisation and Localisation
`i18n` - Internationalisation
`L10n` - Localisation

> [!info] Poedit Translation Editor - Poedit  
> Poedit Full gettext support.  
> [https://poedit.net/](https://poedit.net/)  
```Python
LANGUAGE_CODE = "ru-RU"  # or "ru"
LANGUAGES = [
	("ru", "Russian"),
	("en", "English"),
]
LOCALE_PATHS = [os.path.join(BASE_DIR, "locale")]
USE_I18N = True
USE_L10N = True
# Check Middleware:
#...
#...Session
'django.middleware.locale.LocaleMiddleware',
# ...Common
# Template:
{% load i18n %}
...
{% trans "English text" %}
```
![[attachments/Untitled 23.png|Untitled 23.png]]
![[attachments/Untitled 1 9.png|Untitled 1 9.png]]
![[attachments/Untitled 2 8.png|Untitled 2 8.png]]
```Bash
# create "locale/ru/LC_MESSAGES/django.po"
python -m manage makemessages -l ru
# ...translate po file ...
python -m manage compilemessages
```
![[attachments/Untitled 3 7.png|Untitled 3 7.png]]
### **Интернационализация административной панели**
![[attachments/Untitled 4 6.png|Untitled 4 6.png]]
![[attachments/Untitled 5 6.png|Untitled 5 6.png]]
## Caching
### View caching
[https://docs.djangoproject.com/en/4.1/topics/cache/#specifying-per-view-cache-in-the-urlconf](https://docs.djangoproject.com/en/4.1/topics/cache/#specifying-per-view-cache-in-the-urlconf)
```Python
from django.views.decorators.cache import cache_page
urlpatterns = [
    path('foo/<int:code>/', cache_page(60 * 15)(my_view)),
]
```
### Template fragment caching
[https://docs.djangoproject.com/en/4.1/topics/cache/#template-fragment-caching](https://docs.djangoproject.com/en/4.1/topics/cache/#template-fragment-caching)
```Python
{% load cache %}
{% cache 500 sidebar request.user.username %}
    .. sidebar for logged in user ..
{% endcache %}
```
### Low-level caching
[https://stackoverflow.com/questions/40772832/caching-results-of-a-django-function-call-with-cache-get-or-set](https://stackoverflow.com/questions/40772832/caching-results-of-a-django-function-call-with-cache-get-or-set)
```Python
from django.core.cache import cache
# ...
class OfferListView(ListView):
    model = Offer
    template_name = "offer_list.html"
    context_object_name = "offer_list"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
				# Caching:
        offer_list = cache.get("offer_list")
        if not offer_list:
            language = self.request.LANGUAGE_CODE
            offer_list = Offer.objects.translated(language).all().order_by("-translations__title")
            cache.set("offer_list", offer_list, 60 * 10)
        context["offer_list"] = offer_list
        return context
```
---
## New Deployment
### Migrations
[https://realpython.com/django-migrations-a-primer/](https://realpython.com/django-migrations-a-primer/)
Next workflow tested for ‘clean’ DB setup:
- remove `migrations` directories with all files from apps;
- run `makemigrations` for each app:
```Bash
$ python manage.py makemigrations accounts
$ python manage.py makemigrations articles
$ python manage.py makemigrations pages
```
- run `migrate`, `createsuperuser`:
```Bash
$ python manage.py migrate
$ python manage.py createsuperuser
```
New DB will be created, along with `migrations` dirs in app dirs, and `0001_initial.py` files there.
- use `showmigrations` to check which migrations were applied to DB:
```Bash
$ manage.py showmigrations
```
![[attachments/Untitled 6 6.png|Untitled 6 6.png]]
### Nginx
**Readme**: [GitHub - hazadus/django-website: Basic Django website. For learning purposes. Demo: http://85.193.89.177/](https://github.com/hazadus/django-website)
```Bash
# sudo nano /etc/nginx/conf.d/virtual.conf
# sudo nginx -t
# sudo service nginx restart
# NOTE trailing '/'s in paths!!
server {
    listen 80;
    server_name 85.193.89.177;
    location / {
        proxy_pass http://127.0.0.1:8000/;
    }
    
    # STATIC_URL from settings.py
    location /static/ {
        autoindex on;
        alias /home/hazadus/django-static/; # STATIC_ROOT from settings.py
    }
    location /media/ {
        autoindex on;
        alias /home/hazadus/projects/django-website/media/;
    }
}
```
Nginx need + x to all dirs along the path to static, media dirs.
```Bash
# chmod +x /root
# chmod +x /root/projects/
# chmod +x /root/projects/newspaper/
# chmod +x /root/projects/newspaper/media/
# chmod +x /root/projects/newspaper/media/images/
```
View nginx logs:
```Bash
$ sudo tail -f /var/log/nginx/access.log
$ sudo tail -f /var/log/nginx/error.log
```
### Collect static
```Bash
# Remove all previous stuff
rm -rf /home/hazadus/django-static/*
# Collect new static
source .venv/bin/activate
python3 -m manage collectstatic
```
### Copy files
```Bash
scp ./db.sqlite3 hazadus@85.193.89.177:~/projects/django-c8-newspaper/
scp ./media/images/*.* hazadus@85.193.89.177:~/projects/django-c8-newspaper/media/images
```
### Docker

> [!info] Docker compose with Django 4, Celery, Redis and Postgres  
> Deploying Django application that is using Celery and Redis might be challenging.  
> [https://saasitive.com/tutorial/django-celery-redis-postgres-docker-compose/?utm_campaign=Django%2BNewsletter&utm_medium=email&utm_source=Django_Newsletter_157](https://saasitive.com/tutorial/django-celery-redis-postgres-docker-compose/?utm_campaign=Django%2BNewsletter&utm_medium=email&utm_source=Django_Newsletter_157)  
```Bash
# docker-compose
# SERVER version
# note 'network: host' must be UNDER build!
# https://forums.docker.com/t/option-network-mode-host-in-docker-compose-file-not-working-as-expected/51682
version: "3.9"
services:
  web:
    build:
      context: .
      network: host
    ports:
      - "8000:8000"
    command: python manage.py runserver 0.0.0.0:8000
# command: gunicorn django_project.wsgi -b 0.0.0.0:8000
    volumes:
      - .:/code
```
```Bash
# By choosing network=host the container has access to the network of the host.
# https://github.com/docker/cli/issues/2707
sudo docker build . --network=host
# compose
sudo docker compose --file docker-compose.prod.yml build
sudo docker compose --file docker-compose.prod.yml up
sudo docker compose --file docker-compose.prod.yml up -d
# list running containers
sudo docker ps
# stop
sudo docker compose down
```
```Bash
sudo docker compose build
sudo docker compose up -d --build
# New DB for Django:
sudo docker compose exec web python manage.py migrate
sudo docker compose exec web python manage.py createsuperuser
```
Back up and restore Postgres DB data:
```Bash
# Creates 'backup.tar' with postgresql data in current directory
#
# Container id of Postgres (f0de8da471d2) got from 'sudo docker ps' when containers are up
# '/var/lib/postgresql/data/' is from 'docker-compose.yml', lines:
# volumes:
#      - postgres_data:/var/lib/postgresql/data/
cd /Users/hazadus/backup
sudo docker run --rm --volumes-from c0e3a99224e3 -v $(pwd):/backup ubuntu tar cvf /backup/backup.tar /var/lib/postgresql/data/
```
```Bash
# Change web to running container name, e.g. newspaper-web-1
sudo docker compose exec web python manage.py dumpdata --indent=2 --output=mysite_data.json
# Or, connect to it then run command:
docker exec -it newspaper-web-1 bash
python manage.py dumpdata --indent=2 --output=mysite_data.json
# Restore data:
sudo docker compose exec web python manage.py loaddata mysite_data.json
```
```Bash
# Restoring postgresql data from backup tar
#
#
# ls -al
sudo docker run --rm -v django-c8-newspaper_postgres_data:/var/lib/postgresql/data/ -v $PWD:/backup-dir bash -c "cd /var/lib/postgresql/data/ && ls -al"
#
# untar - RUN FROM DIR WITH 'backup.tar' in it!!!
#
cd /Users/hazadus/backup
sudo docker run --rm -v django-c8-newspaper_postgres_data:/var/lib/postgresql/data/ -v $PWD:/backup-dir bash -c "tar xvf /backup-dir/backup.tar"
```
```Bash
# Copy DB contents from CONTAINER (not volume!) to a folder:
# 3501a6e46de1 = containerID from `docker ps`
docker cp 3501a6e46de1:/var/lib/postgresql/data ~/PycharmProjects/polstagramm/data/postgres/
```
```Bash
# enter CLI:
docker exec -it django-c8-newspaper-db-1 bash
# then run psql:
psql -U postgres
# then in psql
\dt - list all tables
```
```Bash
python -m manage dumpdata users --format json -o users.json
```
### Email – setup and test
```Bash
docker compose exec web python manage.py shell
```
```Python
from django.core.mail import send_mail
send_mail('Django mail', 'This was sent with Django', 'hazadus7@gmail.com', ['hazadus7@gmail.com'], fail_silently=False)
```
### Complete script – rebuild and run containers
```Bash
#!/bin/bash
cd /home/hazadus/projects/django-c8-newspaper
source .venv/bin/activate
echo '[0] Update virtual environment...'
python3 -m pip install -r requirements.txt
echo '[1] Removing static files...'
rm -rf /home/hazadus/django-static/*
echo '[2] Collecting static files...'
python3 -m manage collectstatic
deactivate
echo '[3] Shutting down containers...'
sudo docker compose down
echo '[4] Build containers...'
sudo docker compose build
echo '[5] Run containers...'
sudo docker compose up -d
```
After `collectstatic` copy files from project staticfiles dir to `/home/hazadus/django-static/`
### Load testing

> [!info] GitHub - rakyll/hey: HTTP load generator, ApacheBench (ab) replacement  
> hey is a tiny program that sends some load to a web application.  
> [https://github.com/rakyll/hey](https://github.com/rakyll/hey)  
```Bash
brew install hey
hey -n 1000 https://www.polstagramm.ru
```

> [!info] Getting started - Locust 2.13.1 documentation  
> A Locust test is essentially a Python program.  
> [https://docs.locust.io/en/stable/quickstart.html](https://docs.locust.io/en/stable/quickstart.html)  
- use Locust
### Backup via rsync
```Bash
# copy all the stuff directly to polsta-30.12/
sync -arv --exclude=.venv --exclude=.git --exclude=__pycache__ root@85.193.89.177:/root/projects/newspaper/ /Users/hazadus/webbackup/polsta-30.12/
```

----
📂 [[Django]] | Последнее изменение: 07.02.2024 15:04