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

API_TELEGRAM = '1869665786:AAGBwXI1YJ1sD1u3DLjg21oo1gYzFYIcQ7Q'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'crm.sqlite',
    }
}