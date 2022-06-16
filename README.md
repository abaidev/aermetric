## AERMETRIC

#### Preparations
  - clone project
  - create .env file


    SECRET_KEY=django-insecure-secret-key
    DEBUG=False
    DATABASE_URL=postgresql://postgres:postgres@db:5432/postgres
    ALLOWED_HOSTS="127.0.0.1, localhost, 0.0.0.0"


#### Docker commands
  - run project: `docker-compose up --build`
  - stop project: `docker-compose down`
  - access container bash: `docker exec -it <container_id> bash`
  - create superuser in bash `./manage.py createsuperuser`


#### Annotation
`.csv` file is uploading in admin panel (Aviation app -> Aircrafts)

endpoint to get data is `/api/stats/aircraft/`
