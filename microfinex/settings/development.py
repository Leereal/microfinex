from .base import *
from decouple import config
# EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend" #Default for django
EMAIL_BACKEND = "djcelery_email.backends.CeleryEmailBackend" # use when using celery
EMAIL_HOST = config("EMAIL_HOST")
EMAIL_USE_TLS = True
EMAIL_PORT = config("EMAIL_PORT")
EMAIL_HOST_USER = config("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = config("EMAIL_HOST_PASSWORD")
DEFAULT_FROM_EMAIL = "info@microfinex.com"
DOMAIN = config("DOMAIN")
SITE_NAME = config("SITE_NAME")

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# DB_USERNAME = config("POSTGRES_USER")
# DB_PASSWORD = config("POSTGRES_PASSWORD")
# DB_DATABASE = config("POSTGRES_DB")
# DB_HOST = config("POSTGRES_HOST")
# DB_PORT = config("POSTGRES_PORT")

# DB_IS_AVAIL = all([
#     DB_USERNAME,
#     DB_PASSWORD,
#     DB_DATABASE,
#     DB_HOST,
#     DB_PORT
# ])

# if DB_IS_AVAIL:
#     DATABASES = {
#         'default': {
#             "ENGINE": 'django.db.backends.postgresql',
#             "NAME": DB_DATABASE,
#             "USER": DB_USERNAME,
#             "PASSWORD": DB_PASSWORD,
#             "HOST": DB_HOST,
#             "PORT": DB_PORT
#         }
#     }

CELERY_BROKER_URL = config("CELERY_BROKER")
CELERY_RESULT_BACKEND = config("CELERY_BACKEND")
CELERY_TIMEZONE = "Africa/Kigali"
