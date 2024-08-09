## FastAPI Template Notes

- [FastAPI Project Setup: The Ultimate Guide with Async Postgres, SQLModel, Pytest, & Docker](https://medium.com/@lawsontaylor/the-ultimate-fastapi-project-setup-fastapi-async-postgres-sqlmodel-pytest-and-docker-ed0c6afea11b)

### Профили в Docker Compose

- [Don’t Repeat Yourself with Anchors, Aliases and Extensions in Docker Compose Files](https://medium.com/@kinghuang/docker-compose-anchors-aliases-extensions-a1e4105d70bd)
- [Using profiles with Compose](https://docs.docker.com/compose/profiles/)

The `test` profile:

- Consisting of a Postgres container and an app container.
- Both of these receive the environment file. The host for the Postgres container will be the name of the service `postgres-test`, which is why we set the environment variable `POSTGRES_HOST=postgres-test` in the `app-test`service.
- Both share the same named network `test` so the testing environment is completely isolated from the other services.
- Along with this, no external ports are mapped. We can have the `dev`services up and running while still being able to run the tests at the same time without interference between the two environments.
- The `postgres-test` service does not have any volumes mounted. When we test, we want to spin up the containers, run tests, and shut them down — we don’t need to persist any data.
- The `app-test` service has a volume bound to the `./app` so that tests can be run without having to rebuild the app image every time.
- The `app-test` service also has a `depends_on` to allow the `postgres-test`service to become healthy before we start running the tests via the command `sh -c "python -m pytest -s -vv"`

The `dev` profile:

- The dev environment is very similar to the test one (hence the templating with YAML anchors 😃)
- Again, give the services a named network `dev` so they can only communicate with each other.
- This time though we map the ports and expose them so we can interact with the application from our local machine.
- The `postgres-dev` service has one volume mount `./postgres/docker-entrypoint-initdb.d/:/docker-entrypoint-initdb.d/` so that we can place scripts or Postgres dumps in this directory that will be run when the service starts up, see _Initialization scripts_ in the Postgres Docker documentation [here](https://hub.docker.com/_/postgres).
- It also gets a named volume `pgdata-dev` that maps to the Postgres data directory to allow you to persist the data in the service. With this, the scripts and dumps in `./postgres/docker-entrypoint-initdb.d` don’t have to run every time the service starts.
- For the `app-dev` container, the main change is the command. This time, you start a FastAPI app with [Uvicorn](https://www.uvicorn.org/) and expose it to localhost on port 8000. In production, you’ll want this running behind something more substantial like [Gunicorn](https://gunicorn.org/).

## Transactional Async Database Unit Tests with SQLAlchemy

Because of the asynchronous nature of your application, it’s necessary to set up an asynchronous testing infrastructure.

Additionally, there are a number of other reasons to create transactional database unit tests:

- **Isolation** — Transactions allow tests to run in isolation.
- **Consistency and Clean-Up** — Because tests run in transactions, you can easily roll them back in the Pytest fixtures regardless of whether the test passes or fails. This ensures that the database remains unchanged after the test, avoiding the need for explicit test clean-up.
- **Testing in Parallel** — Because each unit test is done in isolation from any other test, you can even run them in parallel with this approach if needed, without worrying about data collision issues.
- **Faster Speed —** Transactions are generally faster than traditional approaches, such as recreating the database for each test. Starting a new transaction for each test is a lightweight and efficient process, reducing the overhead of setting up and tearing down the database.

To allow asynchronous unit testing with SQLAlchemy, Pytest, and Postgres, you’ll need the following three Pytest fixtures:

- The `event_loop` fixture is scoped to the entire testing session and allows Pytest to only have one active event loop for the entirety of the test run. The built-in event loop fixture with `pytest-asyncio` is function-scoped by default and using it will cause Pytest to error with lots of _loop closed/open errors_.
- The `engine` fixture will drop and create the entire database and yield the created engine. This is scoped to the class level. This offers the best trade-off between testing speed and lines of code in the tests, but this could be scoped differently depending on your needs.
- The final fixture `session` is maybe the most important. This connects the engine to Postgres, starts a transaction, then binds that connection to a session with a nested transaction. Nesting the transaction allows for the isolation mentioned above by allowing us to commit changes in the inner transaction so it’s only visible to the tests it is working with, but doesn’t fully commit data to the database as the outer transaction will never be committed.