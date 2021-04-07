from pathlib import Path
import sys
import os

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = '%yljx9-ty+m3x3idwp$o=ejd$qibxwljgb2cr00nksi8^@ic8q'

DEBUG = True

PROJECT_ROOT = os.path.dirname(__file__)

sys.path.insert(0, os.path.join(PROJECT_ROOT, 'apps'))

ALLOWED_HOSTS = ['*']

STATIC_URL = '/static/'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',

        'NAME': 'crm',

        'USER': 'postgres',

        'PASSWORD': '2151796qw',

        'HOST': 'localhost',

        'PORT': '5432',
    }
}