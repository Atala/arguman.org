# coding:utf-8

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

from datetime import timedelta

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('ARGUMAN_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost'
]


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django.contrib.sitemaps',

    'typogrify',
    'social_auth',
    'django_gravatar',
    'rest_framework',
    'rest_framework.authtoken',
    'profiles',
    'premises',
    'nouns',
    'newsfeed',
    'blog',
    'api',
)

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

PREVENT_LANGUAGE_REDIRECTION = True

DEFAULT_LANGUAGE = 'fr'

BASE_DOMAIN = 'localhost'

AVAILABLE_LANGUAGES = (
    'fr'
)

TIME_ZONE = 'Europe/Paris'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/assets/'
STATIC_ROOT = '/assets/'

# Social Auth Settings
AUTHENTICATION_BACKENDS = (
    # 'social_auth.backends.twitter.TwitterBackend', # TO-DO : get twitter keys
    'django.contrib.auth.backends.ModelBackend',
)

LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'

DEFAULT_FROM_EMAIL = 'alois.guillope@gmail.com'

SITE_URL = "localhost"

# Markitup Settings
MARKITUP_SET = 'markitup/sets/markdown'
MARKITUP_FILTER = ('markdown.markdown', {'safe_mode': False})

BLOG_FEED_TITLE = "Arguman Nuit Debout"
BLOG_FEED_DESCRIPTION = "Plateforme de débats analytiques"
BLOG_URL = "http://arguman.nuitdebout.fr/blog"

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'null': {
            'class': 'django.utils.log.NullHandler',
        },
    },
    'loggers': {
        'django.security.DisallowedHost': {
            'handlers': ['null'],
            'propagate': False,
     },
    }
}