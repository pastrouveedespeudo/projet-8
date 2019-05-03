from . import *
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration
import raven



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





INSTALLED_APPS += [
    'raven.contrib.django.raven_compat',
]


RAVEN_CONFIG = {
    'dsn': 'https://somethingverylong@sentry.io/216272', # caution replace by your own!!
    # If you are using git, you can also automatically configure the
    # release based on the git info.
    'release': raven.fetch_git_sha(os.path.dirname(os.pardir)),
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'root': {
        'level': 'INFO', # WARNING by default. Change this to capture more than warnings.
        'handlers': ['sentry'],
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s '
                      '%(process)d %(thread)d %(message)s'
        },
    },
    'handlers': {
        'sentry': {
            'level': 'INFO', # To capture more than ERROR, change to WARNING, INFO, etc.
            'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
            'tags': {'custom-tag': 'x'},
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        }
    },
    'loggers': {
        'django.db.backends': {
            'level': 'ERROR',
            'handlers': ['console'],
            'propagate': False,
        },
        'raven': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },
        'sentry.errors': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },
    },
}

