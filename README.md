# IMDB

## About the Project
This is my first Web Project Based on Django and Vue


### Used Technologies
* Python
* Django
* PostgreSQL
* Docker
* Django REST framework
* .[![Bootstrap][Bootstrap.com]][Bootstrap-url]
* .[![Vue][Vue.js]][Vue-url]
* .[![Pinia][Pinia.Vue.js][Pinia-url]]
* JavaScript

## Quick Start

1. clone it
```sh
git clone https://github.com/edonssfall/IMDB.git
```

2. copy `example.dev.py` to `dev.py` and fill it
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'DB Name',
        'USER': 'DB User',
        'PASSWORD': 'DB Password',
        'HOST': 'db',
        'PORT': '5432',
        'ATOMIC_REQUESTS': True
    }
}

CELERY_BROKER_URL = 'redis://redis:port/celery_tasks'

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '<your app id goes here>'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '<your app secret goes here>'

SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = [
    'https://www.googleapis.com/auth/userinfo.email',
    'https://www.googleapis.com/auth/userinfo.profile',
]

STATIC_ROOT = '/folder/for/static'
```

3. copy `.env.example` to `.env` and fill it
`.env`
```python
SECRET_KEY='secret_key_for_django'
```
`db.env`
```python
POSTGRES_PASSWORD=DB_PASSWORD
POSTGRES_DB=DB_NAME
```

4. check client/src/constance.js on host-name
```javascript
export let DjangoAPIHost = 'http://localhost:8000/';
//export let DjangoAPIHost = 'http://fill.your.address/';
```

5. run
```sh
docker-compose up
```

6. makemigrations and create super user
```sh
docker exec -it docker_web_name bash
./manage.py migrate
./manage.py createsuperuser
```
