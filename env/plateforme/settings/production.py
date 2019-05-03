from . import *

import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration


SECRET_KEY = '_7cd!+a@ci9f93a%lb3#-a(brz2zblelg=1qjlc!b_*g_@(mxk'

DEBUG = False
ALLOWED_HOSTS = ['157.230.34.183']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql', # on utilise l'adaptateur postgresql
        'NAME': 'plateforme', # le nom de notre base de données créée précédemment
        'USER': 'jb', # attention : remplacez par votre nom d'utilisateur !!
        'PASSWORD': 'tiotiotio333',
        'HOST': '',
        'PORT': '5432',
    }
}

sentry_sdk.init(
    dsn="https://36a8e7d38bef428ebe69a8e6fa584789@sentry.io/1452140",
    integrations=[DjangoIntegration()]
)


