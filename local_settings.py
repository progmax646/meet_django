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

STATICFILES_DIRS = [
    BASE_DIR / "static",
    '/python-projects/meet_django/static/',
]

API_TELEGRAM = '624760197:AAFOx7I3xaB6wbwedsmEZqAd8BfgPYqSOu4s_3Q'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',

        'NAME': 'crm',

        'USER': 'postgres',

        'PASSWORD': '2151',

        'HOST': 'localhost',

        'PORT': '5432',
    }
}