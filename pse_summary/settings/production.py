import os

from .base import *

SECRET_KEY = os.environ.get('SECRET_KEY')
DEBUG = False
ALLOWED_HOSTS = [os.environ.get('SITENAME') or '*']
PRODUCTION = True

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
