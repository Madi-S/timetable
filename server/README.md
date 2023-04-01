# FastAPI-Alembic

### Initialize
```sh
docker-compose build
docker-compose up
```


## Install pipenv package
```sh
pipenv install <package_name>
```



### Make & Run migrations
```sh
docker-compose run web alembic revision --autogenerate -m "I am a teapot"
docker-compose run web alembic upgrade head
```

PGAdmin - localhost:5050 (pgadmin4@pgadmin.org:admin)
