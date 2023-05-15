"""
Django settings for storeServer project.

Generated by 'django-admin startproject' using Django 4.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
from datetime import timedelta
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-kluzk8h%5eq7$()&s_zn_@=is=#0i5r$ap0@gwj8(c^2_b7c2y"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# !TODO remove this
AUTH_USER_MODEL = "users.TuxTechUser"

ALLOWED_HOSTS = [
    "gldb.dev",
    "www.gldb.dev",
    "176.79.170.121",
    "0.0.0.0",
    "localhost",
    "127.0.0.1",
]

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Installed
    "rest_framework",
    "corsheaders",
    "cacheops",
    "cities",
    # Functional apps
    "store",
    "users",
    "product",
    "supply",
    "support",
    "order",
    "cart",
    "favourites",
]

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    )
}


MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    # dev
    "corsheaders.middleware.CorsMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
]

# dev
CORS_ALLOW_ALL_ORIGINS = True

CSRF_TRUSTED_ORIGINS = ["https://gldb.dev:8443", "https://www.gldb.dev:8443"]

ROOT_URLCONF = "storeServer.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(BASE_DIR, "templates/"),
            os.path.join(BASE_DIR, "website/build"),
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "storeServer.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.contrib.gis.db.backends.postgis",
        "NAME": "djangodev",
        "USER": "postgres",
        # "PASSWORD": os.environ.get("TUXTECH_POSTGRES_PASSWD"),
        "PASSWORD": "123",
        "HOST": "localhost",
        "PORT": "5432",
    }
}

CACHEOPS_REDIS = {
    "host": "localhost",  # Redis server address
    "port": 6379,  # Redis server port
    "db": 0,  # Redis database number
}

CACHEOPS = {
    "products.producttemplate": {
        "ops": "get",
        "timeout": 60 * 15,
    },  # Cache get queries for 15 minutes
}

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

AUTHENTICATION_BACKENDS = [
    # "two_factor.backends.TwoFactorBackend",
    # "users.backends.CustomModelBackend",
    # "users.backends.AdminModelBackend",
    "django.contrib.auth.backends.ModelBackend",
]

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=5),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=14),
    "ROTATE_REFRESH_TOKENS": False,
    "BLACKLIST_AFTER_ROTATION": True,
    "UPDATE_LAST_LOGIN": False,
    "ALGORITHM": "HS256",
    "SIGNING_KEY": SECRET_KEY,
    "VERIFYING_KEY": None,
    "AUDIENCE": None,
    "ISSUER": None,
    "AUTH_HEADER_TYPES": ("Bearer",),
    "AUTH_HEADER_NAME": "HTTP_AUTHORIZATION",
    "USER_ID_FIELD": "id",
    "USER_ID_CLAIM": "user_id",
    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
    "TOKEN_TYPE_CLAIM": "token_type",
    "SLIDING_TOKEN_REFRESH_EXP_CLAIM": "refresh_exp",
    "SLIDING_TOKEN_LIFETIME": timedelta(minutes=5),
    "SLIDING_TOKEN_REFRESH_LIFETIME": timedelta(days=1),
}


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = "/static/"

# STATIC_ROOT = "/var/www/TuxTech/static"
STATIC_ROOT = os.path.join(BASE_DIR, "staticCollected")

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# STATICFILES = [
#     {
#         "DIRS": [
#             os.path.join(BASE_DIR, "static/"),
#             # os.path.join(BASE_DIR, "website/build/static/"),
#         ],
#         "APP_DIRS": True,
#     },
# ]

# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, "static/"),
# ]
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
    os.path.join(BASE_DIR, "website/build/static"),
]


# LOGGING = {
#     "version": 1,
#     "disable_existing_loggers": False,
#     "handlers": {
#         "file": {
#             "class": "logging.FileHandler",
#             "filename": "/var/www/log/django.log",
#         },
#     },
#     "loggers": {
#         "django": {
#             "handlers": ["file"],
#             "level": "INFO",
#         },
#         "storeServer": {
#             "handlers": ["file"],
#             "level": "INFO",
#         },
#     },
# }
# settings.py

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
# MEDIA_ROOT = "/var/www/TuxTech/media"

LOGIN_URL = "/login"
# LOGIN_REDIRECT_URL = "two_factor:profile"

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "mail.gldb.dev"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = "home@gldb.dev"
EMAIL_HOST_PASSWORD = os.environ.get("TUXTECH_MAIL_PASSWD")
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER


# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
