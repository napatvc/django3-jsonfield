import os

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'jsonfield',
    'testapp',
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'jsonfield-test',
        'USER': os.environ.get('DB_USER', ''),
        'PASSWORD': os.environ.get('DB_PASSWORD', ''),
    }
}

BASE_PATH = os.path.dirname(__file__)
STATIC_URL = "/static/"
MEDIA_ROOT = os.path.join(BASE_PATH, 'static')
STATIC_ROOT = MEDIA_ROOT

SECRET_KEY = '334ebe58-a77d-4321-9d01-a7d2cb8d3eea'
