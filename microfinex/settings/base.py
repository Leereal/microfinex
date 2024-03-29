from pathlib import Path
from datetime import timedelta

from decouple import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = ['localhost','127.0.0.1','[::1]', 'api']


# Application definition

DJANGO_APPS = [
    'django.contrib.contenttypes',
    'django.contrib.admin',
    'django.contrib.auth',    
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
]

SITE_ID = 1

APPEND_SLASH = False 

THIRD_PARTY_APPS = [
    'rest_framework',
    'django_filters',
    'django_countries',
    'phonenumber_field',
    'djoser',
    'rest_framework_simplejwt',
    'djcelery_email',
    'corsheaders',
    'easyaudit'
]

LOCAL_APPS = [ 
    "apps.common",
    "apps.users",
    "apps.profiles",
    "apps.loans",
    "apps.enquiries",
    "apps.clients",
    "apps.currencies",
    "apps.loan_products",
    "apps.branches",
    "apps.posts",
    "apps.payments",
    "apps.payment_methods",
    "apps.notes",
    ]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE = [
    'easyaudit.middleware.easyaudit.EasyAuditMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',    
]

ROOT_URLCONF = 'microfinex.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'microfinex.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = config('TIME_ZONE', default='UTC')

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'staticfiles/'
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_DIR = []
MEDIA_URL = "/mediafiles/"
MEDIA_ROOT = BASE_DIR / "mediafiles"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#Tell Django Where Custom User Is Located
AUTH_USER_MODEL = "users.User"

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'apps.users.authentication.CustomJWTAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ]
}

SIMPLE_JWT = {
    "AUTH_HEADER_TYPES": (
        "Bearer",
        "JWT",
    ),
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=120),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "SIGNING_KEY": config("SIGNING_KEY"),
    "AUTH_HEADER_NAME": "HTTP_AUTHORIZATION",
    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
}

DJOSER = {
    "LOGIN_FIELD": "email",
    "USER_CREATE_PASSWORD_RETYPE": True,
    # "USERNAME_CHANGED_EMAIL_CONFIRMATION": True,
    "PASSWORD_CHANGED_EMAIL_CONFIRMATION": True,
    "SEND_CONFIRMATION_EMAIL": True,
    "PASSWORD_RESET_CONFIRM_URL": "password/reset/confirm/{uid}/{token}",
    "SET_PASSWORD_RETYPE": True,
    "PASSWORD_RESET_CONFIRM_RETYPE": True,
    "USERNAME_RESET_CONFIRM_URL": "email/reset/confirm/{uid}/{token}",
    "ACTIVATION_URL": "activate/{uid}/{token}",
    "SEND_ACTIVATION_EMAIL": True,
    "SERIALIZERS": {
        "user_create": "apps.users.serializers.CreateUserSerializer,",
        "user": "apps.users.serializers.UserSerializer",
        "current_user": "apps.users.serializers.UserSerializer",
        "user_delete": "djoser.serializers.UserDeleteSerializer",
    },
}

AUTH_COOKIE = 'access'
AUTH_COOKIE_MAX_AGE = 60 * 60 * 24
AUTH_COOKIE_SECURE = config('AUTH_COOKIE_SECURE', 'True') == 'True'
AUTH_COOKIE_HTTP_ONLY = True
AUTH_COOKIE_PATH = '/'
AUTH_COOKIE_SAMESITE = 'None'

CORS_ALLOWED_ORIGINS = config(
    'CORS_ALLOWED_ORIGINS',
    'http://localhost:3000,http://127.0.0.1:3000,http://localhost:3002,http://127.0.0.1:3002'
).split(',')
CORS_ALLOW_CREDENTIALS = True


# Settings for error logging
import logging
import logging.config

from django.utils.log import DEFAULT_LOGGING
logger = logging.getLogger(__name__)
LOG_LEVEL = "INFO"
logging.config.dictConfig({
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "console": {
            "format": "%(asctime)s %(name)-12s %(levelname)-8s %(message)s",            
        },
        "file": {
            "format": "%(asctime)s %(name)-12s %(levelname)-8s %(message)s",
        },
        "django.server": DEFAULT_LOGGING["formatters"]["django.server"],
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "console",
        },
        "file": {
            "level": "INFO",
            "class": "logging.FileHandler",
            "formatter": "file",  # Corrected formatter name
            "filename": "logs/microfinex.log"
        },
        "django.server": DEFAULT_LOGGING["handlers"]["django.server"],
    },
    "loggers": {
        "": {
            "level": "INFO", "handlers": ["console", "file"], "propagate": False
        },
        "apps": {
            "level": "INFO", "handlers": ["console"], "propagate": False
        },
        "django.server": DEFAULT_LOGGING["loggers"]["django.server"],
    }
})

DJANGO_EASY_AUDIT_WATCH_AUTH_EVENTS=False
DJANGO_EASY_AUDIT_WATCH_REQUEST_EVENTS=False
DJANGO_EASY_AUDIT_WATCH_AUTH_EVENTS=False