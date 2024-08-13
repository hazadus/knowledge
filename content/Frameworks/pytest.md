## Справочные материалы

- [Pytest with Eric](https://pytest-with-eric.com) – подборка отличных туториалов по всем вопросам, связанным с написанием тестов под `pytest`.
- Серия статей о тестировании (в т.ч., с `pytest`) в блоге Bite Code!:
	- [Testing with Python (part 1): the basics](https://www.bitecode.dev/p/testing-with-python-part-1-the-basics)
	- [Testing with Python (part 2): moving to pytest](https://www.bitecode.dev/p/testing-with-python-part-2-moving)
	- [Testing with Python (part 3): pytest setup](https://www.bitecode.dev/p/testing-with-python-part-3-pytest)
	- [Testing with Python (part 4): why and what to test?](https://www.bitecode.dev/p/testing-with-python-part-4-why-and)
	- [Testing with Python (part 5): the different types of tests](https://www.bitecode.dev/p/testing-with-python-part-5-the-different)
	- [Testing with Python (part 6): Fake it...](https://www.bitecode.dev/p/testing-with-python-part-6-fake-it)
	- [Testing with Python (part 7): ...until you make it](https://www.bitecode.dev/p/testing-with-python-part-7-until)
	- [Testing with Python (part 8): purity test](https://www.bitecode.dev/p/testing-with-python-part-8-purity)
	- [Testing with Python (part 9): the extra mile](https://www.bitecode.dev/p/testing-with-python-part-9-the-extra)
- [Developing and Testing an Asynchronous API with FastAPI and Pytest – TestDriven.io](https://testdriven.io/blog/fastapi-crud/)

## Examples
- - [FastAPI Project Setup: The Ultimate Guide with Async Postgres, SQLModel, Pytest, & Docker](https://medium.com/@lawsontaylor/the-ultimate-fastapi-project-setup-fastapi-async-postgres-sqlmodel-pytest-and-docker-ed0c6afea11b)
- [Async tests with FastAPI and Postgres](https://github.com/hazadus/fastapi-template/tree/main/backend/app/tests)

----
## Configuration

Configure using `pyproject.toml`:

```toml
[tool.pytest.ini_options] # mandatory section name
addopts = "-s --no-header --no-summary" # force cmd flags
testpaths = [ # what directories contain tests
    "tests",
]
pythonpath = [ # what to add to the python path
    "."
]
```

## Useful Flags

- `-x`_: stop a first failure._
- `--pdb`_: start the Python debugger on failure._
- `-k <filter>`_: only discover tests that match the filter._
- `--ff`_: start with tests that failed in the previous run._
- `--nf`_: start with new files._
- `--sw`_: start from where it stopped the previous run._
- `--no-header` _/_ `--no-summary`_: remove the big blobs of texts in the output._
- `--verbosity=x`_: from 0 to 3 levels of output granularity._

----
📂 [[Frameworks]]