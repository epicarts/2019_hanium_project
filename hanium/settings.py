"""
Django settings for hanium project.

Generated by 'django-admin startproject' using Django 2.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'wufom@f%xvy^36wu=uw)z6&%5xfc$2l=oa6*@)hv2*_bc!ba8d'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DJANGO_DEBUG')

ALLOWED_HOSTS = ['*']


# Application definition
#앱을 만들고 난뒤에 여기에 등록을 해야됨.
INSTALLED_APPS = [
    'channels',
    'accounts',
    'chat',
    'main',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'goologin.apps.GoologinConfig',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'hanium.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['accounts/templates', 'chat/templates', 'goologin/templates', 'main/templates','templates'],
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

WSGI_APPLICATION = 'hanium.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases
DATABASES = {
    'default': {
        #'ENGINE': 'django.db.backends.sqlite3',
        #'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'OPTIONS': {'charset': 'utf8mb4'},#한글 사용을 위해 추가
        'ENGINE': 'django.db.backends.mysql',
            'NAME': os.getenv('DJANGO_DB_NAME', ''),
            'USER': os.getenv('DJANGO_USERNAME', 'root'),
            'PASSWORD': os.getenv('DJANGO_DB_PASSWORD','root'),
            'HOST': os.getenv('DJANGO_DB_HOST','localhost'),
            'PORT': os.getenv('DJANGO_DB_PORT','3306')
    }
}


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

LANGUAGE_CODE = 'ko-kr'
DATABASES_OPTIONS = {'charset':'utf8'}

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/
#URL로만 존재하는 최상위 경로.
STATIC_URL = '/static/'

#개발 단계에서 사용하는 정적 파일들이 어디에 있는지에 대한 경로
#findstatic은 해당 설정 위치에서 정적파일을 찾음
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'accounts', 'static'), os.path.join(BASE_DIR, 'chat', 'static'), os.path.join(BASE_DIR, 'main', 'static'),]

#Django 앱 디렉터리에 있는 static 디렉터리와 STATICFILES_DIRS에 지정된 경로에 있는 모든 파일을 모읍
#실 환경에서 제공
STATIC_ROOT = os.path.join(BASE_DIR,'staticfiles')


#login redirect
#LOGIN_URL = '/login'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/accounts/login'

#media file에 접근하는 URL
MEDIA_URL = '/upload_files/'

#실제 팡리이 위치하는 서버 내부 경로
MEDIA_ROOT = os.path.join(BASE_DIR, 'uploads')

# 채팅 Channels
ASGI_APPLICATION = 'hanium.routing.application'
#channel layer
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [("redis", 6379)],
        },
    },
}

#구글 로그인 추가
AUTHENTICATION_BACKENDS = (
'django.contrib.auth.backends.ModelBackend',
'allauth.account.auth_backends.AuthenticationBackend',
)
SITE_ID = 1
