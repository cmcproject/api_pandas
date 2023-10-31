# Intro

This is Pandas service API for managing people data

## Prerequisites

### Pre-commit

Install [pre-commit](https://pre-commit.com/) firstly.

Please execute `pre-commit install` once after downloading the repo code. It will help us keep the code quality in
check.

Run `pre-commit run --all-files` if you want to check your code

### Fixtures

Populate the database using Django fixtures

docker-compose run --rm app sh -c "python manage.py loaddata people.json"

# Django setup

docker-compose run --rm app sh -c "django-admin startproject api_pandas ."

docker-compose run --rm app sh -c "python manage.py startapp people"

docker-compose run --rm app sh -c "python manage.py createsuperuser"

# Poetry setup cmds

poetry init

poetry add django-filter

poetry add djangorestframework

poetry shell

poetry add black --group dev

# Docker cmds

docker-compose build

docker-compose up

docker-compose run --rm app sh -c "python manage.py makemigrations"

# Useful commands

Build image

```
make build
```

Run project

```
make up
```

Update dependencies

```
make lock
```

Make migrations

```
make makemigrations
```
