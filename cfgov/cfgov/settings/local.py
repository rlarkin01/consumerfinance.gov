import warnings

from unipath import DIRS

from .base import *


DEBUG = True
SECRET_KEY = 'not-secret-key-for-testing'
INSTALLED_APPS += (
    'sslserver',
    'wagtail.contrib.wagtailstyleguide',
)

STATIC_ROOT = REPOSITORY_ROOT.child('collectstatic')
STATICFILES_DIRS += [str(d) for d in REPOSITORY_ROOT.child('static.in').listdir(filter=DIRS)]

ALLOW_ADMIN_URL = DEBUG or os.environ.get('ALLOW_ADMIN_URL', False)


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
        }
    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': True,
        }
    }
}

# Django Debug Toolbar
if os.environ.get('ENABLE_DEBUG_TOOLBAR'):
    INSTALLED_APPS += ('debug_toolbar',)

    INTERNAL_IPS = ('127.0.0.1',)
    MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware',)

    DEBUG_TOOLBAR_CONFIG = {
        'SHOW_COLLAPSED': True,
    }


MIDDLEWARE_CLASSES += CSP_MIDDLEWARE_CLASSES

# Disable caching when working locally.
CACHES = {
    k: {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
        'TIMEOUT': 0,
    } for k in (
        'default', 'eregs_longterm_cache', 'api_cache',
        'post_preview', 'default_fragment_cache'
    )
}

# Optionally enable cache for post_preview
if os.environ.get('ENABLE_POST_PREVIEW_CACHE'):
    CACHES['post_preview'] = {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'post_preview_cache',
        'TIMEOUT': None,
    }

# Optionally enable cache for general template fragments, including mega menu
if os.environ.get('ENABLE_DEFAULT_FRAGMENT_CACHE'):
    CACHES['default_fragment_cache'] = {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'default_fragment_cache',
        'TIMEOUT': None,
    }

# Use a mock GovDelivery API instead of the real thing.
# Remove this line to use the real API instead.
GOVDELIVERY_API = 'core.govdelivery.LoggingMockGovDelivery'
