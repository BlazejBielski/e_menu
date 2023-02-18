# eMenu project

Simple online menu

## Technologies used
- Django
- Rest
- Postgresql
- JWT authorization
- Swagger for auto documentation
- Docker compose

## Start instruction

- Clone repository
- Start command ```docker compose up --build```
- on terminal use the command ```docker compose exec backend sh``` to run shell inside container
- use the command ```python manage.py loadadata ./fixtures/card_and_dishes.json``` to load example data
- use the command ```python manage.py createsuperuser```
- enjoy

## What is done
1. Application works on docker
2. App have a two API - public, and nonpublic
- public API allows you to browse the menu and dishes in a given menu
- nonpublic API allows you to create, read, update or delete menu or dishes (full CRUD)
3. Auto documentation with Swagger
4. Test cases in Postman

## TODO
1. Email with reports on added and changed dishes within the last 24 hours
2. Tests
3. Filters for dishes