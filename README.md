# FastAPI test app

This app implements REST API service to perform CRUD operations over accounts.

## Getting started

This app requires PostgreSQL as database. To run PostgreSQL server inside Docker with pdAdmin web interface, run

```bash
docker compose up -d
```

Default value for database name, username and password for PostgreSQL is fastapi-postgres. Change it in `docker-compose.yml` file if required. Default port inside Docker is 5432, outside Docker is 54321.

## Environment variables

App required environment variables to run

```
PG_USERNAME=fastapi-postgres
PG_PASSWORD=fastapi-postgres
PG_HOST=localhost
PG_PORT=54321
PG_DATABASE=fastapi-postgres
```

One could create `.env` file in project catalog with these variables or set them directly from bash

```bash
export PG_USERNAME="fastapi-postgres"
export PG_PASSWORD="fastapi-postgres"
export PG_HOST="localhost"
export PG_PORT=54321
export PG_DATABASE="fastapi-postgres"
```
