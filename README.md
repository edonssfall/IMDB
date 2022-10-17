# IMDB

## About the Project
![](https://github.com/edonssfall/IMDB/blob/main/gif-presentation.gif)
This is my first Web Project Based on Django and Vue
https://ithillel-leonid.ogir-ok.com/



### Used Technologies
* Python
* Django
* PostgreSQL
* Docker
* Django REST framework
* Bootstrap
* Vue.js
* Pinia
* JavaScript
* SSL Certificate

## Quick Start

1. clone it
```sh
git clone https://github.com/edonssfall/IMDB.git
```

2. copy `example.dev.py` to `dev.py` and fill it
```python
DATABASES = {
    'default': {
        'NAME': 'DB Name',
        'USER': 'DB User',
        'PASSWORD': 'DB Password'
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
