## Speed Up Your Django Tests

### Adam Johnson · «Gumroad» · 2020 г. · 300 с.

#django #programming #tests #tdd #book 

[[Books Reading]] | [[Dev/Frameworks/Django/Django]]

http://library.hazadus.ru/books/75/details/

> [!abstract]
> This book is a practical guide to making your Django project's tests faster. It has many tips and tricks that apply to all projects, big and small. And it covers the two most popular test runners: Django's test framework and pytest.
>
It's based on my experience speeding up various Django projects' test suites, improving Django's own testing framework, and creating pytest plugins.
>
[Книга на сайте издательства](https://adamchainz.gumroad.com/l/suydt)

----

Django: [Tagging Tests](https://docs.djangoproject.com/en/3.2/topics/testing/tools/#tagging-tests).

----

GitHub Actions [Default environment variables](https://docs.github.com/en/actions/learn-github-actions/variables#default-environment-variables).

`GITHUB_ACTIONS` – Always set to true when GitHub Actions is running the workflow. You can use this variable to differentiate when tests are being run locally or by GitHub Actions.

----

Django’s Test Framework can time database setup separately with the `--timing` flag:
```
$ python manage.py test --timing
```
Using system command:
```
$ time python manage.py test
```

PyCharm: [Optimize your code using profilers](https://www.jetbrains.com/help/pycharm/profiler.html)

----

You shouldn’t run tests with `DEBUG` set to `True`.
It decreases test accuracy since the test environment is less similar to production, and imposes extra overheads on the CPU and memory. Django does a few things extra in debug mode, such as keeping a log of every database query and creating debugging responses for 404 errors. Some third party packages also impose extra overheads in debug mode, such as `django-debug-toolbar`’s profiling.

----


----
📂 [[Reading]] | Последнее изменение: 07.02.2024 15:05