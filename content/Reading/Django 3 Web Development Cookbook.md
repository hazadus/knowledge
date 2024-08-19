## Django 3 Web Development Cookbook

### Aidas Bendoraitis, Jake Kronika · «Packt» · 2020 г. · 601 с.

#django #programming #book 

[[Books Read]] | [[Dev/Frameworks/Django/Django]]

http://library.hazadus.ru/books/30/details/

> [!abstract]
> Django is a web framework for perfectionists with deadlines, designed to help you build manageable medium and large web projects in a short time span. This fourth edition of the Django Web Development Cookbook is updated with Django 3's latest features to guide you effectively through the development process. This Django book starts by helping you create a virtual environment and project structure for building Python web apps. You'll learn how to build models, views, forms, and templates for your web apps and then integrate JavaScript in your Django apps to add more features. As you advance, you'll create responsive multilingual websites, ready to be shared on social networks. The book will take you through uploading and processing images, rendering data in HTML5, PDF, and Excel, using and creating APIs, and navigating different data types in Django. You'll become well-versed in security best practices and caching techniques to enhance your website's security and speed. This edition not only helps you work with the PostgreSQL database but also the MySQL database. You'll also discover advanced recipes for using Django with Docker and Ansible in development, staging, and production environments. By the end of this book, you will have become proficient in using Django's powerful features and will be equipped to create robust websites.
>
[https://www.packtpub.com/free-ebook/django-3-web-development-cookbook-fourth-edition/9781838987428](https://www.packtpub.com/free-ebook/django-3-web-development-cookbook-fourth-edition/9781838987428)

----

##### Notable recipes

- Avoiding circular dependencies (p.105)
- Adding database constraints (p.107)
- Uploading images (p.110, pdf=133) - check out usage of ` django-imagekit` for image versions.
- Preview images in Django Admin _forms_ (p. 116, pdf=137)
- Preview images in Django Admin _tables_ (p. 277, pdf=299)
- Creating sortable inlines (p.281, pdf=303) - check `django-ordered-model`.
- Downloading authorized files (p.346, pdf=367)

----

P.51 - how to get git HEAD timestamp. *Won't work in Docker?*
```python
# versioning.py
import subprocess
from datetime import datetime

def get_git_changeset_timestamp(absolute_path):
	repo_dir = absolute_path
	git_log = subprocess.Popen(
		"git log --pretty=format:%ct --quiet -1 HEAD",
		stdout=subprocess.PIPE,
		stderr=subprocess.PIPE,
		shell=True,
		cwd=repo_dir,
		universal_newlines=True,
	 )
	timestamp = git_log.communicate()[0]
	try:
		timestamp = datetime.utcfromtimestamp(int(timestamp))
	except ValueError:
		# Fallback to current timestamp
		return datetime.now().strftime('%Y%m%d%H%M%S')
	
	changeset_timestamp = timestamp.strftime('%Y%m%d%H%M%S')
	return changeset_timestamp
```

----


----
📂 [[Reading]] | Последнее изменение: 07.02.2024 15:05