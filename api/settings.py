"""
Django settings for api project.

Generated by 'django-admin startproject' using Django 2.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
import config as c

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'y7mbld(4so6k(#k729%j_ek4^v*wau2*x37cnzh@9l+$#(x*p%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'rest_framework',
    'article',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

ROOT_URLCONF = 'api.urls'

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

WSGI_APPLICATION = 'api.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': c.API_ADMIN_DB_CONFIG['host'],
        'NAME': c.API_ADMIN_DB_CONFIG['db_name'],
        'USER': c.API_ADMIN_DB_CONFIG['user'],
        'PASSWORD': c.API_ADMIN_DB_CONFIG['password'],
        'PORT': c.API_ADMIN_DB_CONFIG['port'],
        'CHARSET': c.API_ADMIN_DB_CONFIG['charset'],
    },
    'baseball': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': c.BASEBALL_DB_CONFIG['host'],
        'NAME': c.BASEBALL_DB_CONFIG['db_name'],
        'USER': c.BASEBALL_DB_CONFIG['user'],
        'PASSWORD': c.BASEBALL_DB_CONFIG['password'],
        'PORT': c.BASEBALL_DB_CONFIG['port'],
        'CHARSET': c.BASEBALL_DB_CONFIG['charset'],
    },
    'daily_news': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': c.DAILY_NEWS_DB_CONFIG['host'],
        'NAME': c.DAILY_NEWS_DB_CONFIG['db_name'],
        'USER': c.DAILY_NEWS_DB_CONFIG['user'],
        'PASSWORD': c.DAILY_NEWS_DB_CONFIG['password'],
        'PORT': c.DAILY_NEWS_DB_CONFIG['port'],
        'CHARSET': c.DAILY_NEWS_DB_CONFIG['charset'],
    },
}

DATABASE_ROUTERS = [
    'article.db_routers.MultiDBRouter',    # e.g) snsproject.core.routers.MultiDBRouter
]


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

# TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'

SESSION_COOKIE_AGE = 60
SESSION_SAVE_EVERY_REQUEST = True

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True

'''
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://{URL}:6379',
    },
}
'''