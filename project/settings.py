import os
DIRNAME = os.path.abspath(os.path.dirname(__file__).decode('utf-8'))

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

import dj_database_url
DATABASES = {'default': dj_database_url.config()}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
        'TIMEOUT': 3600
    }
}

# Localisation
TIME_ZONE = 'Europe/Dublin'
LANGUAGE_CODE = 'en-us'
DEFAULT_LANGUAGE_CODE = 'en'
USE_I18N = True
USE_L10N = True

# Name of the directory that uploaded files should be put in.
UPLOADS_DIRNAME = 'uploads'

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.normpath(os.path.join(DIRNAME, '..', UPLOADS_DIRNAME)) + os.path.sep

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/%s/' % UPLOADS_DIRNAME

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
STATIC_ROOT = 'staticfiles'

# URL prefix for static files.
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(DIRNAME, 'static'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
AWS_STORAGE_BUCKET_NAME = os.environ['AWS_STORAGE_BUCKET_NAME']
BOTO_S3_BUCKET = AWS_STORAGE_BUCKET_NAME
AWS_S3_SECURE_URLS = False
AWS_QUERYSTRING_AUTH = False
STATICFILES_STORAGE = 'customboto.FixedS3BotoStorage'
S3_URL = 'http://%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME
if not DEBUG:
    STATIC_URL = S3_URL

# Make this unique, and don't share it with anybody.
SECRET_KEY = os.environ['SECRET_KEY']

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.transaction.TransactionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
)

ROOT_URLCONF = 'urls'
WSGI_APPLICATION = 'wsgi.application'

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Regex patterns used in multiple url.py files.
DOMAIN_PATTERN = '(?P<domain>[\w-]+\.[\w.-]+)'
EMAIL_LHS_PATTERN = '(?P<email_lhs>[0-9A-Za-z\.+_\-]+)'

TEMPLATE_DIRS = (
    'templates',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.request',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.contrib.messages.context_processors.messages',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sites',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.humanize',
    'django.contrib.markup',

    # 3rd party apps
    'south',
    'crispy_forms',
    'compressor',
    'storages',

    # apps
    'main',
    'events',
    'utilities',
    'library'
)

# List of additional directories to look for fixtures in.
FIXTURE_DIRS = []
# Iterate all installed apps
for app_name in INSTALLED_APPS:
    # Determine the path to a 'fixtures_test' dir in the app.
    test_fixtures_dir = os.path.join(DIRNAME, app_name, 'fixtures_test')
    # If it exists, add it to the list of locations to look for fixtures in.
    if os.path.exists(test_fixtures_dir):
        FIXTURE_DIRS.append(test_fixtures_dir),

DEFAULT_FROM_EMAIL = 'ducss@csc.tcd.ie'
CONTACT_US_EMAIL = DEFAULT_FROM_EMAIL
TECH_ADMIN_EMAIL = 'admin@ducss.ie'

SITE_ID = 1
INTERNAL_IPS = ('127.0.0.1',)

CRISPY_FAIL_SILENTLY = not DEBUG

COMPRESS_ENABLED = True

# Try to import local_settings.
if DEBUG:
    try:
        from local_settings import *
    except ImportError:
        pass

# Try to import deployment_settings.
try:
    from deployment_settings import *
except ImportError:
    pass
