import os
import sys

from django.conf import global_settings
from django.utils.translation import ugettext_lazy as _

import dj_database_url
from unipath import Path

from ..util import admin_emails


# Repository root is 4 levels above this file
REPOSITORY_ROOT = Path(__file__).ancestor(4)

# This is the root of the Django project, 'cfgov'
PROJECT_ROOT = REPOSITORY_ROOT.child('cfgov')
V1_TEMPLATE_ROOT = PROJECT_ROOT.child('jinja2', 'v1')

SECRET_KEY = os.environ.get('SECRET_KEY', os.urandom(32))

# Deploy environment
DEPLOY_ENVIRONMENT = os.getenv('DEPLOY_ENVIRONMENT')

# signal that tells us that this is a proxied HTTPS request
# effects how request.is_secure() responds
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
USE_X_FORWARDED_HOST = True

# Use the django default password hashing
PASSWORD_HASHERS = global_settings.PASSWORD_HASHERS

# Application definition

INSTALLED_APPS = (
    'permissions_viewer',
    'wagtail.wagtailcore',
    'wagtail.wagtailadmin',
    'wagtail.wagtaildocs',
    'wagtail.wagtailsnippets',
    'wagtail.wagtailusers',
    'wagtail.wagtailimages',
    'wagtail.wagtailembeds',
    'wagtail.contrib.wagtailfrontendcache',
#    'wagtail.wagtailsearch', # TODO: conflicts with haystack, will need to revisit.
    'wagtail.wagtailredirects',
    'wagtail.wagtailforms',
    'wagtail.wagtailsites',

    'wagtail.contrib.modeladmin',
    'wagtail.contrib.table_block',
    'wagtail.contrib.wagtailroutablepage',
    'localflavor',
    'modelcluster',
    'taggit',
    'wagtailinventory',
    'wagtailsharing',
    'flags',
    'wagtailflags',
    'watchman',
    'haystack',
    'ask_cfpb',
    'agreements',
    'overextends',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    "django.contrib.sitemaps",
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'storages',
    'data_research',
    'v1',
    'core',
    'legacy',
    'django_extensions',
    'jobmanager',
    'wellbeing',
    'search',
    'regulations3k',
    'treemodeladmin',
    'housing_counselor',
)

OPTIONAL_APPS = [
    {'import': 'comparisontool', 'apps': ('comparisontool', 'haystack',)},
    {'import': 'paying_for_college',
     'apps': ('paying_for_college', 'haystack',)},
    {'import': 'retirement_api', 'apps': ('retirement_api',)},
    {'import': 'ratechecker', 'apps': ('ratechecker', 'rest_framework')},
    {'import': 'countylimits', 'apps': ('countylimits', 'rest_framework')},
    {'import': 'complaint_search', 'apps': ('complaint_search', 'rest_framework')},
    {'import': 'ccdb5_ui', 'apps': ('ccdb5_ui', )},
    {'import': 'teachers_digital_platform', 'apps': ('teachers_digital_platform', 'mptt', 'haystack')},
]

POSTGRES_APPS = []

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.http.ConditionalGetMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'wagtail.wagtailcore.middleware.SiteMiddleware',
    'wagtail.wagtailredirects.middleware.RedirectMiddleware',

    'core.middleware.ParseLinksMiddleware',
    'core.middleware.DownstreamCacheControlMiddleware'
)

CSP_MIDDLEWARE_CLASSES = ('csp.middleware.CSPMiddleware', )

if ('CSP_ENFORCE' in os.environ):
    MIDDLEWARE_CLASSES += CSP_MIDDLEWARE_CLASSES


ROOT_URLCONF = 'cfgov.urls'

# We support two different template engines: Django templates and Jinja2
# templates. See https://docs.djangoproject.com/en/dev/topics/templates/
# for an overview of how Django templates work.
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # Look for Django templates in these directories.
        'DIRS': [
            PROJECT_ROOT.child('templates'),
        ],
        # Look for Django templates in each app under a templates subdirectory.
        'APP_DIRS': True,
        'OPTIONS': {
            'builtins': [
                'overextends.templatetags.overextends_tags',
            ],
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        }
    },
    {
        'NAME': 'wagtail-env',
        'BACKEND': 'django.template.backends.jinja2.Jinja2',
        # Look for Jinja2 templates in these directories.
        'DIRS': [
            V1_TEMPLATE_ROOT,
            V1_TEMPLATE_ROOT.child('_includes'),
            V1_TEMPLATE_ROOT.child('_layouts'),
            PROJECT_ROOT.child('static_built'),
        ],
        # Look for Jinja2 templates in each app under a jinja2 subdirectory.
        'APP_DIRS': True,
        'OPTIONS': {
            'environment': 'v1.jinja2_environment.environment',
            'extensions': [
                'jinja2.ext.do',
                'jinja2.ext.i18n',
                'jinja2.ext.loopcontrols',

                'wagtail.wagtailcore.jinja2tags.core',
                'wagtail.wagtailadmin.jinja2tags.userbar',
                'wagtail.wagtailimages.jinja2tags.images',

                'core.jinja2tags.filters',
                'regulations3k.jinja2tags.regulations',
                'v1.jinja2tags.datetimes_extension',
                'v1.jinja2tags.fragment_cache_extension',
                'v1.jinja2tags.v1_extension',
            ],
        }
    },
]

WSGI_APPLICATION = 'cfgov.wsgi.application'

# Admin Url Access
ALLOW_ADMIN_URL = os.environ.get('ALLOW_ADMIN_URL', False)


# Databases
DATABASES = {}

# If DATABASE_URL is defined in the environment, use it to set the Django DB.
if os.getenv('DATABASE_URL'):
    DATABASES['default'] = dj_database_url.config()

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

LANGUAGES = (
    ('en', _('English')),
    ('es', _('Spanish')),
)

LOCALE_PATHS = (
    os.path.join(PROJECT_ROOT, 'locale'),
)

TIME_ZONE = 'America/New_York'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/
STATIC_URL = '/static/'

# Absolute path to the directory static files should be collected to.
STATIC_ROOT = os.environ.get('DJANGO_STATIC_ROOT', '/var/www/html/static')

MEDIA_ROOT = os.environ.get('MEDIA_ROOT',
                            os.path.join(PROJECT_ROOT, 'f'))
MEDIA_URL = '/f/'


# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
]

STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'

# Used to include directories not traditionally found,
# app-specific 'static' directories.
STATICFILES_DIRS = [
    PROJECT_ROOT.child('static_built'),
    PROJECT_ROOT.child('templates', 'wagtailadmin')
]


ALLOWED_HOSTS = ['*']

EXTERNAL_URL_WHITELIST = (r'^https:\/\/facebook\.com\/cfpb$',
                          r'^https:\/\/twitter\.com\/cfpb$',
                          r'^https:\/\/www\.linkedin\.com\/company\/consumer-financial-protection-bureau$',
                          r'^https:\/\/www\.youtube\.com\/user\/cfpbvideo$',
                          r'https:\/\/www\.flickr\.com\/photos\/cfpbphotos$'
                          )

# Wagtail settings

WAGTAIL_SITE_NAME = 'consumerfinance.gov'
WAGTAILIMAGES_IMAGE_MODEL = 'v1.CFGOVImage'
TAGGIT_CASE_INSENSITIVE = True

WAGTAIL_USER_CREATION_FORM = 'v1.auth_forms.UserCreationForm'
WAGTAIL_USER_EDIT_FORM = 'v1.auth_forms.UserEditForm'

SHEER_ELASTICSEARCH_SERVER = os.environ.get('ES_HOST', 'localhost') + ':' + os.environ.get('ES_PORT', '9200')
SHEER_ELASTICSEARCH_INDEX = os.environ.get('SHEER_ELASTICSEARCH_INDEX', 'content')
ELASTICSEARCH_BIGINT = 50000

MAPPINGS = PROJECT_ROOT.child('es_mappings')

SHEER_ELASTICSEARCH_SETTINGS = \
    {
        "settings": {
            "analysis": {
                "analyzer": {
                    "my_edge_ngram_analyzer": {
                        "tokenizer": "my_edge_ngram_tokenizer"
                    },
                    "tag_analyzer": {
                       "tokenizer": "keyword",
                       "filter": "lowercase"
                    }
                },
                "tokenizer": {
                    "my_edge_ngram_tokenizer": {
                        "type": "edgeNGram",
                        "min_gram": "2",
                        "max_gram": "5",
                        "token_chars": [
                            "letter",
                            "digit"
                        ]
                    }
                }
            }
        }
    }


#LEGACY APPS

STATIC_VERSION = ''

MAPBOX_ACCESS_TOKEN = os.environ.get('MAPBOX_ACCESS_TOKEN')
HOUSING_COUNSELOR_S3_PATH_TEMPLATE = (
    'a/assets/hud/{format}s/{zipcode}.{format}'
)


HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'search.backends.CFGOVElasticsearch2SearchEngine',
        'URL': SHEER_ELASTICSEARCH_SERVER,
        'INDEX_NAME': os.environ.get('HAYSTACK_ELASTICSEARCH_INDEX',
                                     SHEER_ELASTICSEARCH_INDEX+'_haystack'),
        'INCLUDE_SPELLING': True,
    }
}
ELASTICSEARCH_INDEX_SETTINGS = {
    'settings': {
        'analysis': {
            'analyzer': {
                'ngram_analyzer': {
                    'type': 'custom',
                    'tokenizer': 'lowercase',
                    'filter': ['haystack_ngram']
                },
                'edgengram_analyzer': {
                    'type': 'custom',
                    'tokenizer': 'lowercase',
                    'filter': ['haystack_edgengram']
                },
                'synonym_en' : {
                    'tokenizer' : 'whitespace',
                    'filter' : ['synonyms_en']
                },
                'synonym_es' : {
                    'tokenizer' : 'whitespace',
                    'filter' : ['synonyms_es']
                },
            },
            'tokenizer': {
                'haystack_ngram_tokenizer': {
                    'type': 'nGram',
                    'min_gram': 3,
                    'max_gram': 15,
                },
                'haystack_edgengram_tokenizer': {
                    'type': 'edgeNGram',
                    'min_gram': 3,
                    'max_gram': 15,
                    'side': 'front'
                },
            },
            'filter': {
                'haystack_ngram': {
                    'type': 'nGram',
                    'min_gram': 3,
                    'max_gram': 15
                },
                'haystack_edgengram': {
                    'type': 'edgeNGram',
                    'min_gram': 3,
                    'max_gram': 15
                },
                'synonyms_en': {
                    'type': 'synonym',
                    'synonyms_path' : 'analysis/synonyms_en.txt'
                },
                'synonyms_es': {
                    'type': 'synonym',
                    'synonyms_path' : 'analysis/synonyms_es.txt'
                },
            }
        }
    }
}
ELASTICSEARCH_DEFAULT_ANALYZER = 'snowball'

# S3 Configuration
# https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html#settings
AWS_LOCATION = 'f'  # A path prefix that will be prepended to all uploads
AWS_QUERYSTRING_AUTH = False  # do not add auth-related query params to URL
AWS_S3_FILE_OVERWRITE = False
AWS_S3_SECURE_URLS = True  # True = use https; False = use http
AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')
AWS_DEFAULT_ACL = None  # Default to using the ACL of the bucket

if os.environ.get('S3_ENABLED', 'False') == 'True':
    AWS_S3_ACCESS_KEY_ID = os.environ['AWS_S3_ACCESS_KEY_ID']
    AWS_S3_SECRET_ACCESS_KEY = os.environ['AWS_S3_SECRET_ACCESS_KEY']
    if os.environ.get('AWS_S3_CUSTOM_DOMAIN'):
        AWS_S3_CUSTOM_DOMAIN=os.environ['AWS_S3_CUSTOM_DOMAIN']
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    MEDIA_URL = os.path.join(os.environ.get('AWS_S3_URL'), AWS_LOCATION, '')

# Govdelivery
GOVDELIVERY_ACCOUNT_CODE = os.environ.get('GOVDELIVERY_ACCOUNT_CODE')

# LOAD OPTIONAL APPS
# code from https://gist.github.com/msabramo/945406

for app in OPTIONAL_APPS:
    try:
        __import__(app["import"])
        for name in app.get("apps", ()):
            if name not in INSTALLED_APPS:
                INSTALLED_APPS += (name,)
        MIDDLEWARE_CLASSES += app.get("middleware", ())
    except ImportError:
        pass

WAGTAIL_ENABLE_UPDATE_CHECK = False  # Removes wagtail version update check banner from admin page.

# Email
ADMINS = admin_emails(os.environ.get('ADMIN_EMAILS'))

if DEPLOY_ENVIRONMENT:
    EMAIL_SUBJECT_PREFIX = u'[{}] '.format(DEPLOY_ENVIRONMENT.title())

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
WAGTAILADMIN_NOTIFICATION_FROM_EMAIL = os.environ.get(
    'WAGTAILADMIN_NOTIFICATION_FROM_EMAIL')


# Password Policies
# cfpb_common password rules
CFPB_COMMON_PASSWORD_RULES = [
    [r'.{12,}', 'Minimum allowed length is 12 characters'],
    [r'[A-Z]', 'Password must include at least one capital letter'],
    [r'[a-z]', 'Password must include at least one lowercase letter'],
    [r'[0-9]', 'Password must include at least one digit'],
    [r'[@#$%&!]', 'Password must include at least one special character (@#$%&!)'],
]
# cfpb_common login rules
# in seconds
LOGIN_FAIL_TIME_PERIOD = os.environ.get('LOGIN_FAIL_TIME_PERIOD', 120 * 60)
# number of failed attempts
LOGIN_FAILS_ALLOWED = os.environ.get('LOGIN_FAILS_ALLOWED', 5)
LOGIN_REDIRECT_URL = '/login/welcome/'
LOGIN_URL = "/login/"

# When we generate an full HTML version of the regulation, we want to
# write it out somewhere. This is where.
OFFLINE_OUTPUT_DIR = ''

DATE_FORMAT = 'n/j/Y'

GOOGLE_ANALYTICS_ID = ''
GOOGLE_ANALYTICS_SITE = ''

# Regulations.gov environment variables
REGSGOV_BASE_URL = os.environ.get('REGSGOV_BASE_URL')
REGSGOV_API_KEY = os.environ.get('REGSGOV_API_KEY')

# Akamai
ENABLE_AKAMAI_CACHE_PURGE = os.environ.get('ENABLE_AKAMAI_CACHE_PURGE', False)
if ENABLE_AKAMAI_CACHE_PURGE:
    WAGTAILFRONTENDCACHE = {
        'akamai': {
            'BACKEND': 'v1.models.akamai_backend.AkamaiBackend',
            'CLIENT_TOKEN': os.environ.get('AKAMAI_CLIENT_TOKEN'),
            'CLIENT_SECRET': os.environ.get('AKAMAI_CLIENT_SECRET'),
            'ACCESS_TOKEN': os.environ.get('AKAMAI_ACCESS_TOKEN')
        },
    }


# CSP Whitelists

# These specify what is allowed in <script> tags.
CSP_SCRIPT_SRC = ("'self'",
                  "'unsafe-inline'",
                  "'unsafe-eval'",
                  '*.google-analytics.com',
                  '*.googletagmanager.com',
                  'tagmanager.google.com',
                  'optimize.google.com',
                  'ajax.googleapis.com',
                  'search.usa.gov',
                  'api.mapbox.com',
                  'js-agent.newrelic.com',
                  'dnn506yrbagrg.cloudfront.net',
                  'bam.nr-data.net',
                  '*.youtube.com',
                  '*.ytimg.com',
                  'trk.cetrk.com',
                  'universal.iperceptions.com',
                  'cdn.mouseflow.com',
                  'n2.mouseflow.com',
                  'about:',
                  'connect.facebook.net',
                  'www.federalregister.gov',
                  'storage.googleapis.com'
                  )

# These specify valid sources of CSS code
CSP_STYLE_SRC = (
    "'self'",
    "'unsafe-inline'",
    'fast.fonts.net',
    'tagmanager.google.com',
    'optimize.google.com',
    'api.mapbox.com',
    'fonts.googleapis.com',)

# These specify valid image sources
CSP_IMG_SRC = (
    "'self'",
    'www.ecfr.gov',
    's3.amazonaws.com',
    'www.gstatic.com',
    'ssl.gstatic.com',
    'stats.g.doubleclick.net',
    'files.consumerfinance.gov',
    'img.youtube.com',
    '*.google-analytics.com',
    'trk.cetrk.com',
    'searchstats.usa.gov',
    'gtrk.s3.amazonaws.com',
    '*.googletagmanager.com',
    'tagmanager.google.com',
    'maps.googleapis.com',
    'optimize.google.com',
    'api.mapbox.com',
    '*.tiles.mapbox.com',
    'stats.search.usa.gov',
    'data:',
    'www.facebook.com',
    'www.gravatar.com')

# These specify what URL's we allow to appear in frames/iframes
CSP_FRAME_SRC = (
    "'self'",
    '*.googletagmanager.com',
    '*.google-analytics.com',
    'optimize.google.com',
    'www.youtube.com',
    '*.doubleclick.net',
    'universal.iperceptions.com',
    'www.facebook.com',
    'staticxx.facebook.com',
    'mediasite.yorkcast.com')

# These specify where we allow fonts to come from
CSP_FONT_SRC = ("'self'", "data:", "fast.fonts.net", "fonts.google.com", "fonts.gstatic.com")

# These specify hosts we can make (potentially) cross-domain AJAX requests to.
CSP_CONNECT_SRC = ("'self'",
                   '*.google-analytics.com',
                   '*.tiles.mapbox.com',
                   'bam.nr-data.net',
                   'files.consumerfinance.gov',
                   's3.amazonaws.com',
                   'public.govdelivery.com',
                   'api.iperceptions.com')

# Feature flags
# All feature flags must be listed here with a dict of any hard-coded
# conditions or an empty dict. If the conditions dict is empty the flag will
# only be enabled if database conditions are added.
FLAGS = {
    # Ask CFPB search spelling correction support
    # When enabled, spelling suggestions will appear in Ask CFPB search and
    # will be used when the given search term provides no results.
    'ASK_SEARCH_TYPOS': {},

    # Beta banner, seen on beta.consumerfinance.gov
    # When enabled, a banner appears across the top of the site proclaiming
    # "This beta site is a work in progress."
    'BETA_NOTICE': {'environment is': 'beta'},

    # When enabled, include a recruitment code comment in the base template.
    'CFPB_RECRUITING': {},

    # When enabled, display a "technical issues" banner on /complaintdatabase.
    'CCDB_TECHNICAL_ISSUES': {},

    # When enabled, use Wagtail for /company-signup/ (instead of selfregistration app)
    'WAGTAIL_COMPANY_SIGNUP': {},

    # IA changes to mega menu for user testing
    # When enabled, the mega menu under "Consumer Tools" is arranged by topic
    'IA_USER_TESTING_MENU': {},

    # Fix for margin-top when using the text inset
    # When enabled, the top margin of full-width text insets is increased
    'INSET_TEST': {},

    # When enabled, serves `/es/` pages from this
    # repo ( excluding /obtener-respuestas/ pages ).
    'ES_CONV_FLAG': {},

    # The next version of the public consumer complaint database
    'CCDB5_RELEASE': {},

    # To be enabled when mortgage-performance data visualizations go live
    'MORTGAGE_PERFORMANCE_RELEASE': {},

    # Google Optimize code snippets for A/B testing
    # When enabled this flag will add various Google Optimize code snippets.
    # Intended for use with path conditions.
    'AB_TESTING': {},

    # Email popups.
    'EMAIL_POPUP_OAH': {'boolean': True},
    'EMAIL_POPUP_DEBT': {'boolean': True},

    # Wagtail menu
    'WAGTAIL_MENU': {},

    # The release of new Whistleblowers content/pages
    'WHISTLEBLOWER_RELEASE': {},

    # Search.gov API-based site-search
    'SEARCH_DOTGOV_API': {},

    # The release of the new Financial Coaching pages
    'FINANCIAL_COACHING': {},

    # Teacher's Digital Platform Customer Review Tool
    'TDP_CRTOOL': {'environment is': 'beta'},

    # Teacher's Digital Platform Search Interface Tool
    'TDP_SEARCH_INTERFACE': {'environment is': 'beta'},

    # Teacher's Digital Platform Static Pages
    'TDP_STATIC_PAGE': {'environment is': 'beta'},

    # Teacher's Digital Platform Building Blocks Tool
    'TDP_BB_TOOL': {'environment is': 'beta'},

    # Turbolinks is a JS library that speeds up page loads
    # https://github.com/turbolinks/turbolinks
    'TURBOLINKS': {},

    # Ping google on page publication in production only
    'PING_GOOGLE_ON_PUBLISH': {'environment is': 'production'},

    'LEGACY_HUD_API': {'environment is': 'production'},

    # To be enabled when switching the site to use the BCFP logo
    'BCFP_LOGO': {},

    # Improvements to Find A Housing Counselor page
    # (UI Improvements project, Fall 2018)
    'HUD_TOOL_IMPROVEMENTS': { 'environment is': 'local' },
}


# Watchman tokens, used to authenticate global status endpoint
WATCHMAN_TOKENS = os.environ.get('WATCHMAN_TOKENS', os.urandom(32))

# This specifies what checks Watchman should run and include in its output
# https://github.com/mwarkentin/django-watchman#custom-checks
WATCHMAN_CHECKS = (
    'watchman.checks.databases',
    'watchman.checks.storage',
    'watchman.checks.caches',
    'alerts.checks.check_clock_drift',
)

# Used to check server's time against in check_clock_drift
NTP_TIME_SERVER = 'north-america.pool.ntp.org'

# If server's clock drifts from NTP by more than specified offset
# (in seconds), check_clock_drift will fail
MAX_ALLOWED_TIME_OFFSET = 5

# Search.gov values
SEARCH_DOT_GOV_AFFILIATE = os.environ.get('SEARCH_DOT_GOV_AFFILIATE')
SEARCH_DOT_GOV_ACCESS_KEY = os.environ.get('SEARCH_DOT_GOV_ACCESS_KEY')

# We want the ability to serve the latest drafts of some pages on beta.
# This value is read by v1.wagtail_hooks.
SERVE_LATEST_DRAFT_PAGES = []

# To expose a previously-published page's latest draft version on beta,
# add its primary key to the list below.
if DEPLOY_ENVIRONMENT == 'beta':
    SERVE_LATEST_DRAFT_PAGES = []

# Email popup configuration. See v1.templatetags.email_popup.
EMAIL_POPUP_URLS = {
    'debt': [
        '/ask-cfpb/what-is-a-statute-of-limitations-on-a-debt-en-1389/',
        '/ask-cfpb/what-is-the-best-way-to-negotiate-a-settlement-with-a-debt-collector-en-1447/',
        '/ask-cfpb/what-should-i-do-when-a-debt-collector-contacts-me-en-1695/',
        '/consumer-tools/debt-collection/',
    ],
    'oah': [
        '/owning-a-home/',
        '/owning-a-home/mortgage-estimate/',
    ],
}

REGULATIONS_REFERENCE_MAPPING = [
    (
        r'(?P<section>[\w]+)-(?P<paragraph>[\w-]*-Interp)',
        'Interp-{section}',
        '{section}-{paragraph}'
    ),
]

# Optionally enable cache for general template fragments
if os.environ.get('ENABLE_DEFAULT_FRAGMENT_CACHE'):
    CACHES = {
        'default_fragment_cache': {
            'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
            'LOCATION': 'default_fragment_cache',
            'TIMEOUT': None,
        }
    }
else:
    CACHES = {
        'default_fragment_cache': {
            'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
            'TIMEOUT': 0,
        }
    }

PARSE_LINKS_BLACKLIST = [
    '/admin/',
    '/django-admin/',
    '/policy-compliance/rulemaking/regulations/1002/',
    '/policy-compliance/rulemaking/regulations/1003/',
    '/policy-compliance/rulemaking/regulations/1004/',
    '/policy-compliance/rulemaking/regulations/1005/',
    '/policy-compliance/rulemaking/regulations/1010/',
    '/policy-compliance/rulemaking/regulations/1011/',
    '/policy-compliance/rulemaking/regulations/1012/',
    '/policy-compliance/rulemaking/regulations/1013/',
    '/policy-compliance/rulemaking/regulations/1024/',
    '/policy-compliance/rulemaking/regulations/1026/',
    '/policy-compliance/rulemaking/regulations/1030/',
]

# Required by django-extensions to determine the execution directory used by
# scripts executed with the "runscript" management command.
# See https://django-extensions.readthedocs.io/en/latest/runscript.html.
BASE_DIR = 'scripts'
