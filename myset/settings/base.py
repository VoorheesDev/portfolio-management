import os
import dj_database_url
from django.utils.crypto import get_random_string
from decouple import config, Csv


BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROJECT_NAME = config('PROJECT_NAME')

SECRET_KEY = config("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django_extensions',

    # 'mptt',
    # 'easy_thumbnails',
    # 'django_select2',
    # 'rest_framework',
    # 'rest_framework.authtoken',

    # installed
    'social_django',
    'import_export',
    'django_select2',

    # custom apps
    'apps.core',
    'apps.accounts',
    'apps.projects',
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


ROOT_URLCONF = '%s.urls' % PROJECT_NAME

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, PROJECT_NAME, 'templates'),
        ],
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ],
        },
    },
]
FORM_RENDERER = 'django.forms.renderers.TemplatesSetting'

WSGI_APPLICATION = '%s.wsgi.application' % PROJECT_NAME


# Database
DATABASES = {
    'default': dj_database_url.config(default=config('DATABASE_URL')),
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    # {
    #     'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    # },
]


# Internationalization
LANGUAGE_CODE = config('LANGUAGE_CODE', default='en')

LANGUAGES = [
    ('en', 'English'),
]

TIME_ZONE = config('TIME_ZONE', default='UTC')

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = config('STATIC_ROOT', default=os.path.join(BASE_DIR, 'staticfiles'))

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, PROJECT_NAME, 'static'),
)

MEDIA_ROOT = config('MEDIA_ROOT', default=os.path.join(BASE_DIR, 'media'))
MEDIA_URL = '/media/'


AUTH_USER_MODEL = 'accounts.User'
AUTHENTICATION_BACKENDS = (
    'social_core.backends.linkedin.LinkedinOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/login/'
LOGIN_URL = '/login/'
LOGOUT_URL = '/logout/'

LOCALE_PATHS = [
    # os.path.join(BASE_DIR, PROJECT_NAME, 'locale'),
]

SESSION_COOKIE_DOMAIN = config('SESSION_COOKIE_DOMAIN', default=None)
CSRF_COOKIE_SAMESITE = None
SESSION_COOKIE_SAMESITE = None

# THUMBNAIL_BASEDIR = 'thumbs'
# THUMBNAIL_ALIASES = {
#     '': {
#         'avatar': {
#             'size': (200, 200),
#             'background': '#cccccc',
#         },
#     },
# }

# REST_FRAMEWORK = {
#     'DEFAULT_AUTHENTICATION_CLASSES': [
#         'rest_framework.authentication.SessionAuthentication',
#         'rest_framework.authentication.TokenAuthentication',
#     ]
# }

DEFAULT_FROM_EMAIL = config('DEFAULT_FROM_EMAIL', default='noreply@ex.com')
EMAIL_BCC_ADDRESSES = config('EMAIL_BCC_ADDRESSES', default='', cast=Csv())

PROJECT_CONFIGURATION = config('DJANGO_SETTINGS_MODULE', default='').split('.')[-1]
USE_HTTPS = False

# Google integration
GOOGLE_TAG_MANAGER = os.environ.get('GOOGLE_TAG_MANAGER', '')

ELASTICSEARCH_URLS = config('ELASTICSEARCH_URLS', default='http://localhost:9200').split(',')
# ELASTICSEARCH_INDICES_PREFIX = config('ELASTICSEARCH_INDICES_PREFIX', default=PROJECT_NAME)

SITE_URL = config('SITE_URL', default='')

SOCIAL_AUTH_JSONFIELD_ENABLED = True
SOCIAL_AUTH_LINKEDIN_OAUTH2_KEY = config('LINKEDIN_CLIENT_ID')
SOCIAL_AUTH_LINKEDIN_OAUTH2_SECRET = config('LINKEDIN_CLIENT_SECRET')
SOCIAL_AUTH_LINKEDIN_OAUTH2_SCOPE = ['r_liteprofile', 'r_emailaddress']
SOCIAL_AUTH_LINKEDIN_OAUTH2_FIELD_SELECTORS = ['emailAddress', 'formatted-name']
SOCIAL_AUTH_LINKEDIN_OAUTH2_EXTRA_DATA = [
    ('id', 'id'),
    ('formattedName', 'name'),
    ('emailAddress', 'email'),
]
SOCIAL_AUTH_USERNAME_IS_FULL_EMAIL = True
SOCIAL_AUTH_USER_FIELDS = ['email', 'name']
SOCIAL_AUTH_USER_FIELD_MAPPING = {'first_name': '', 'last_name': '', 'fullname': 'name'}
SOCIAL_AUTH_PIPELINE = (
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.auth_allowed',
    'social_core.pipeline.social_auth.social_user',
    'social_core.pipeline.user.get_username',
    'social_core.pipeline.social_auth.associate_by_email',
    'social_core.pipeline.user.create_user',
    'apps.accounts.pipeline.user.confirm_email',  # email is already verified by LinkedIn. Set `email_confirmed` to True
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details',
)

IMPORT_EXPORT_USE_TRANSACTIONS = True

PAGE_SIZE = 25

# Messages
from django.contrib.messages import constants as messages
MESSAGE_TAGS = {
    messages.ERROR: 'danger'
}

CACHES = {
    "select2": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/2",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    },
}
# Tell select2 which cache configuration to use:
SELECT2_CACHE_BACKEND = "select2"
