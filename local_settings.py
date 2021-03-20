from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = '%yljx9-ty+m3x3idwp$o=ejd$qibxwljgb2cr00nksi8^@ic8q'

DEBUG = True

ALLOWED_HOSTS = ['*']

STATIC_URL = '/static/'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',

        'NAME': 'meet-legalact',

        'USER': 'postgres',

        'PASSWORD': '2151796qw',

        'HOST': 'localhost',

        'PORT': '5432',
    }
}