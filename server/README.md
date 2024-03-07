# FastAPI-TDD-Docker

### If shit happens

Mark `generate_schemas=True`
Then undo, once it did initialize schemas

```python
def init_db(app: FastAPI) -> None:
    register_tortoise(
        app,
        db_url=os.environ.get('DATABASE_URL'),
        modules={'models': ['app.models.tortoise']},
        generate_schemas=False,
        add_exception_handlers=True,
    )
```

### Commands (mostly for Windows)

Application address: http://127.0.0.1:8004/docs

Set up docker

```
docker-compose up -d --build
```

Connect to postgres

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
