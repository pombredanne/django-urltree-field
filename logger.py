import logging
from django.conf import settings

LOG_SETTINGS = {
    'version': 1,
    'disable_existing_loggers': True,
    'handlers': {
        'logfile': {
            'level':'INFO',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': settings.SITE_ROOT + "/urltree-logfile",
            'maxBytes': 50000,
            'backupCount': 2,
        },
        'output-logfile': {
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': settings.SITE_ROOT + "/urltree-output-logfile",
            'maxBytes': 50000,
            'backupCount': 0,
        },
        'console':{
            'level':'DEBUG',
            'class':'logging.StreamHandler',
        },
    },
    'loggers': {
        'urltree': {
            'handlers': ['console', 'logfile', 'output-logfile'],
            'level': 'DEBUG',
        },
    },
}


# Make sure that dictConfig is available
# This was added in Python 2.7/3.2
try:
    from logging.config import dictConfig
except ImportError:
    from django.utils.dictconfig import dictConfig

dictConfig(LOG_SETTINGS)
logger = logging.getLogger('urltree')
