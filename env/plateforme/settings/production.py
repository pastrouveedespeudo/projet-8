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
    dsn="https://3be951771b6744659d92bf290ff432ee@sentry.io/1451910",
    integrations=[DjangoIntegration()]
)





