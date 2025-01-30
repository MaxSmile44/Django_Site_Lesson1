import locale
import os
from environs import Env


env = Env()
env.read_env()

DEBUG = env.bool('DEBUG', default=False)
SECRET_KEY = env('SECRET_KEY')

DATABASES = {
    'default': {
        'ENGINE': env('DB_ENGINE'),
        'HOST': env('DB_HOST'),
        'PORT': env('DB_PORT'),
        'NAME': env('DB_NAME'),
        'USER': env('DB_USER'),
        'PASSWORD': env('DB_PASSWORD'),
    }
}


INSTALLED_APPS = ['datacenter']

ROOT_URLCONF = 'project.urls'

ALLOWED_HOSTS = ['X-Forwarded-Host']


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
    },
]


locale.setlocale(locale.LC_ALL, "ru_RU.utf8")

USE_L10N = True

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
