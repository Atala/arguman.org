import os

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('ARGUMAN_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = DEBUG

BASE_DOMAIN = 'arguman.nuitdebout.fr'
SITE_URL = "arguman.nuitdebout.fr"
BLOG_URL = "arguman.nuitdebout.fr/blog"
