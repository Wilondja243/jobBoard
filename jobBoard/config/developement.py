
from pathlib import Path
from decouple import config

from .base import *


SECRET_KEY = config('SECRET_KEY')
DEBUG = True

ALLOWED_HOSTS=['*']

# Cookie
CSRF_COOKIE_NAME="csrftoken"
CSRF_HEADER_NAME='HTTP_X_CSRFTOKEN'

# Email backend
EMAIL_BACKEND="django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST="smtp.gmail.com"
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER="wilondjaebuela2001@gmail.com"
EMAIL_HOST_PASSWORD="eqal xqyf rfal zhry "
EMAIL_TIMEOUT=30
