from .base import *

DEBUG = True

# database configuration
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

# celery configuration
CELERY_BROKER_URL = 'redis://redis:port/celery_tasks'


# Google configuration
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '<your app id goes here>'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '<your app secret goes here>'

# Define SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE to get extra permissions from Google.
SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = [
    'https://www.googleapis.com/auth/userinfo.email',
    'https://www.googleapis.com/auth/userinfo.profile',
]

# default static
STATIC_ROOT = '/folder/for/static'
