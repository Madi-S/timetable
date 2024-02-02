# FastAPI-TDD-Docker

### Commands (mostly for Windows)

Run application

```
uvicorn app.main:app --reload
```

Get into pyenv

```
env\Scripts\activate.bat
```

Set environmental variables

```
set TESTING=1
```

Set up docker

```
docker-compose up -d --build
```

Connect to postgres

```
docker-compose exec web-db psql -U postgres
```

Enter postgres database

```
docker-compose exec web-db psql -U postgres
```

Init migrations using Aerich

```
docker-compose exec web aerich init -t app.db.TORTOISE_ORM
```

Create a migration

```
docker-compose exec web aerich init-db
```

Run tests

```
docker-compose exec web python -m pytest
```

Run tests with monkeypatching

```
docker-compose exec web pytest -k "unit" -n auto
```

Initialize schemas

```
docker-compose exec web python app/db.py
```

Run tests with coverage

```
docker-compose exec web python -m pytest --cov="."
docker-compose exec web python -m pytest --cov="." --cov-report html
```

Run flake8 for code quality

```
docker-compose exec web flake8 .
```

Check for formatting errors and format them using black

```
docker-compose exec web black . --check
docker-compose exec web black . --diff
docker-compose exec web black .
```

Sort imports using isort

```
docker-compose exec web isort . --check-only
docker-compose exec web isort . --diff
docker-compose exec web isort .
```

Verify all

```
docker-compose exec web flake8 .
docker-compose exec web black . --check
docker-compose exec web isort . --check-only
```

<hr>

### Overview

An example of dockerized fastapi application developed using test-driven technology
This application will follow RESTful design principles, comprise docker configuration, use Tortoise ORM interacting with Postgres
Pytest will be used fod test-driven development
Application will be configured for deployment on Heroku

<hr>

### The application routes:

| Endpoint       | Method | CRUD Operation | Result                          |
| -------------- | ------ | -------------- | ------------------------------- |
| /summaries     | GET    | READ           | Retrieve all summaries          |
| /summaries/:id | GET    | READ           | Retrieve a single summary by id |
| /summaries     | POST   | CREATE         | Create a summary                |
| /summaries/:id | PUT    | UPDATE         | Update a summary by id          |
| /summaries:id  | DELETE | DELETE         | Delete a summary by id          |

<hr>

### Useful links

[FastAPI](https://fastapi.tiangolo.com)

[Pytest](https://docs.pytest.org/en/7.2.x)

[Docker](https://www.docker.com)

[Tortoise](https://tortoise.github.io)

[Postgres](https://www.postgresql.org)

[Heroku](https://devcenter.heroku.com)
