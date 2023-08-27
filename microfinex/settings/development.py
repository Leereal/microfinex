from .base import *

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