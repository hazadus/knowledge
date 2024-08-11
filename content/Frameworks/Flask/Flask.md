## References
### Documentation
[Welcome to Flask — Flask Documentation (3.0.x)](https://flask.palletsprojects.com/en/3.0.x/)
[Werkzeug — Werkzeug Documentation (3.0.x)](https://werkzeug.palletsprojects.com/en/3.0.x/)
[Jinja — Jinja Documentation (3.1.x)](https://jinja.palletsprojects.com/en/3.1.x/)
[Welcome to Click — Click Documentation (8.1.x)](https://click.palletsprojects.com/en/8.1.x/)
### Best Practices
[PGJones.dev](https://pgjones.dev/blog/modern-flask-2023/)

### Benefits of Flask in Web Development

Problem: When choosing a web framework for your Python project, you want to understand the advantages of using Flask without an extensive description.

Solution:
Flask offers several key benefits:
Simplicity: Minimalistic and easy-to-understand syntax.
Flexibility: No enforced project structure, customizable components.
Extensibility: Rich ecosystem of extensions for selective feature integration.
Built-in Development Server: Included for easy testing.
Jinja2 Templating: Simplified HTML content generation.
RESTful Support: Convenient for API development.
Active Community: Support and resources available.
Scalability: Suitable for various project sizes.
Werkzeug and Jinja2: Leverages well-tested components.
Microservices: Ideal for microservice architecture.
Learning Curve: Suitable for beginners.

Flask's simplicity and flexibility make it a versatile choice for Python web development.

----
## My Examples

- Структура приложения
	- [flask-pytest](https://gitverse.ru/amgold/flask-pytest): приложение разбито на слои (данные, сервисный, веб).
- Tests
	- [unittests](https://www.notion.so/unittests-f1ebf9c5a60d4447939f467c1740468f?pvs=21).
	- [flask-restx-learn](https://github.com/hazadus/flask-restx-learn/tree/main/tests)
	- [flask-pytest](https://gitverse.ru/amgold/flask-pytest): Flask (blueprints), SQLAlchemy, Flask-SQLAlchemy, Pytest, pytest-cov, Factory Boy, Docker. Юнит-тесты на каждый слой (данные, сервисный, веб) и интеграционные тесты.
- PostgreSQL
	- [flask-postgres-alembic](https://gitverse.ru/amgold/flask-postgres-alembic): Flask + SQLAlchemy + PostgreSQL + Alembic + Docker.
- Forms
	- [Books App](https://gitlab.skillbox.ru/aleksandr_goldovskii/python_advanced/-/tree/master/module_14_mvc/homework)

----
## Basic Flask App

### Running App in Debug Mode
```bash
export FLASK_APP="app.py"
export FLASK_DEBUG=1
python -m flask run --port=8000
```

## Using Application Factory

🔗 [The Application Factory – Flask Docs](https://flask.palletsprojects.com/en/3.0.x/tutorial/factory/#the-application-factory)



----
## Forms

[https://github.com/wtforms/wtforms/](https://github.com/wtforms/wtforms/)
[Flask-WTF — Flask-WTF Documentation (1.2.x)](https://flask-wtf.readthedocs.io/)
[The Flask Mega-Tutorial, Part III: Web Forms](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iii-web-forms)
Example – Books app: https://gitlab.skillbox.ru/aleksandr_goldovskii/python_advanced/-/tree/master/module_14_mvc/homework

Install:
```bash
pip install -U Flask-WTF
pip install email_validator
```
### Set CSRF Token or Disable CSRF
```python
# config.py
import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    # or
    WTF_CSRF_ENABLED = False

# ...then in the main app file:
from config import Config
app = Flask(__name__)
app.config.from_object(Config)
```
### Sample Code with Forms
```python
from flask import Flask
from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField
from wtforms.validators import InputRequired, Email, NumberRange


app = Flask(__name__)


class RegistrationForm(FlaskForm):
    email = StringField(validators=[InputRequired(), Email()])
    phone = IntegerField(
        validators=[InputRequired(), NumberRange(min=1000000000, max=9999999999)]
    )
    name = StringField(validators=[InputRequired()])
    address = StringField(validators=[InputRequired()])
    index = IntegerField(
        validators=[InputRequired(), NumberRange(min=100000, max=999999)]
    )
    comment = StringField()


@app.route("/registration", methods=["POST"])
def registration():
    form = RegistrationForm()

    if form.validate_on_submit():
        email, phone = form.email.data, form.phone.data

        return f"Successfully registered user {email} with phone +7{phone}"

    return f"Invalid input, {form.errors}", 400


if __name__ == "__main__":
    app.config["WTF_CSRF_ENABLED"] = False
    app.run(debug=True)
```
### Custom Validators
```python
from typing import Optional

from flask_wtf import FlaskForm
from wtforms import Field
from wtforms.validators import ValidationError


def number_length(min: int, max: int, message: Optional[str] = None):
    """
    Checks that `field.data` consists of `min`... `max` digits (all zeroes are acceptable).
    """
    error_message = "Must be number {min} to {max} digits long.".format(
        min=min,
        max=max,
    )
    message = f"{message} {error_message}" if message else error_message

    def _number_length(form: FlaskForm, field: Field):
        try:
            number = int(field.data)
            if not max >= len(str(field.data)) >= min:
                raise ValidationError(message)
        except TypeError:
            raise ValidationError(message)

    return _number_length


class NumberLength:
    """
    Checks that `field.data` consists of `min`... `max` digits (all zeroes are acceptable).
    """

    def __init__(self, min: int, max: int, message: Optional[str] = None):
        self.min = min
        self.max = max
        error_message = "Must be number {min} to {max} digits long.".format(
            min=min,
            max=max,
        )
        self.message = f"{message} {error_message}" if message else error_message

    def __call__(self, form, field):
        try:
            number = int(field.data)
            if not self.max >= len(str(field.data)) >= self.min:
                raise ValidationError(self.message)
        except TypeError:
            raise ValidationError(self.message)
```

----
## URL Map

```python
from flask import Flask, url_for
from werkzeug.routing.rules import Rule

app = Flask(__name__)


def has_no_empty_params(rule: Rule) -> bool:
    """
    Check if a Rule has params without defaults.

    :param rule: A Rule represents one URL pattern.
    :return: True if `rule` has no params without defaults; otherwise, False.
    """
    defaults = rule.defaults if rule.defaults is not None else ()
    arguments = rule.arguments if rule.arguments is not None else ()
    return len(defaults) >= len(arguments)

def get_url_list(flask_app: Flask) -> list:
    """
    Create list of of url, endpoint tuples, that can be navigated in a browser
    and do not require parameters.
    Ref: https://stackoverflow.com/questions/13317536/get-list-of-all-routes-defined-in-the-flask-app/13318415#13318415

    :param flask_app: Flask app instance
    :return: list of url, endpoint tuples
    """
    links = []
    for rule in app.url_map.iter_rules():
        # Filter out rules we can't navigate to in a browser
        # and rules that require parameters
        if "GET" in rule.methods and has_no_empty_params(rule):
            url = url_for(rule.endpoint, **(rule.defaults or {}))
            links.append((url, rule.endpoint))
    # links is now a list of url, endpoint tuples
    return links

def create_404_page() -> str:
    """
    Create simple page with a list of available endpoints.

    :return: HTML with a list of available endpoints.
    """
    links = get_url_list(flask_app=app)
    html = "<!DOCTYPE html>\n<html lang='en'>\n<body>\n"
    html += "<h1>Page not found!</h1>\n<p>\nYou can visit one of existing pages:\n</p>\n<ul>\n"
    for link in links:
        html += "<li><a href='{url}'>{title}</a></li>\n".format(
            url=link[0], title=link[1]
        )
    html += "</ul>\n</body>\n</html>"
    return html


@app.route("/dogs")
def dogs():
    return "Страница с пёсиками"


@app.route("/cats/<int:cat_id>")
def cat_page(cat_id: int):
    return f"Страница с котиком {cat_id}"


@app.route("/index")
def index():
    return "Главная страница"


@app.errorhandler(404)
def page_not_found(exc):
    return create_404_page(), 404


if __name__ == "__main__":
    app.run(debug=True)
```

----
📂 [[Flask]]