📁 [[Frameworks]]

-----
## References
- [Testing with Python (part 3): pytest setup](https://www.bitecode.dev/p/testing-with-python-part-3-pytest)

## Examples
- [Async tests with FastAPI and Postgres](https://github.com/hazadus/fastapi-template/tree/main/backend/app/tests)

## Configuration

Configure using `pyproject.toml`:

```
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