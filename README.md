# Browser Extensions Tool

### This is a tool for finding extensions ideas, niches based on jobs postings and currently available extensions.

#### Tech stack

- Django
- Django Rest Framework
- Vue.js
- Postgres
- Redis
- Celery
- AWS
- Docker
- Docker Compose

#### How it works

- Upwork job postings is used as a source of data
- Chrome Extensions store is used as a source of data
- Extensions ideas are validated by searching the store and job postings
- LLM models are used for analysis of the data

#### How to run
Go to backend directory

``` bash
cd backend
```
Install from requirements

``` bash
poetry install
```
Run migrations(make sure all apps are migrated(users, contact, payment))

``` bash
poetry run manage.py makemigrations
```

``` bash
poetry run python manage.py migrate users && poetry run python manage.py migrate
```
Run server

``` bash
poetry run python manage.py runserver
```

Backend is running on http://localhost:8000
Admin panel is running on http://localhost:8000/ADMIN_URL (ADMIN_URL is set in .env file)
Swagger docs is running on http://localhost:8000/api/docs