[How to integrate Django with a legacy database](https://docs.djangoproject.com/en/5.0/howto/legacy-databases/)
https://docs.djangoproject.com/en/5.0/ref/django-admin/#django-admin-inspectdb

[Unit-Testing Unmanaged Models — Django](https://blog.devgenius.io/unit-testing-unmanaged-models-django-93648b5e6e24)
[A cleaner approach to mocking unmanaged models in Django tests](https://gist.github.com/TobeTek/e6214cebcf138f1127a1a64a4d1fa494)

```
# Создать модели к структуре существующей БД
docker compose exec -it web bash
python manage.py inspectdb --settings "django_project.settings"
```
