"""
Django settings for jobapp project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

PROD = False

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
if PROD:
    SECRET_KEY = 'xuv@g@))^^9azukf9q$a^%2ozqz8*wr#y28j@@z)jxsdmx&03o'
else:
    SECRET_KEY = 'xs!x*iowf$n$^j#dnr*#ko*xvo8kk!csr-n)h%lp-r$5)cm9@f'

# SECURITY WARNING: don't run with debug turned on in production!
if PROD:
    DEBUG = False
else:
    DEBUG = True

if PROD:
    SITE_URL = 'http://www.doornox.com'
else:
    SITE_URL = 'http://zatalyst.fwd.wf'

if PROD:
    S3_BUCKET = 'doornox-prod'
else:
    S3_BUCKET = 'doornox'

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['.doornox.com', 'jobapp-env.elasticbeanstalk.com']

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'jobapp'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'jobapp.urls'

WSGI_APPLICATION = 'jobapp.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ['RDS_DB_NAME'],
        'USER': os.environ['RDS_USERNAME'],
        'PASSWORD': os.environ['RDS_PASSWORD'],
        'HOST': os.environ['RDS_HOSTNAME'],
        'PORT': os.environ['RDS_PORT'],
    }
}

# Logging
# thanks to http://stackoverflow.com/questions/5739830/simple-log-to-file-example-for-django-1-3

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'standard': {
            'format' : "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt' : "%d/%b/%Y %H:%M:%S"
        },
    },
    'handlers': {
        'null': {
            'level':'DEBUG',
            'class':'django.utils.log.NullHandler',
        },
        'console':{
            'level':'INFO',
            'class':'logging.StreamHandler',
            'formatter': 'standard'
        },
    },
    'loggers': {
        'django': {
            'handlers':['console'],
            'propagate': True,
            'level':'WARN',
        },
        'django.db.backends': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Email Config

EMAIL_HOST = 'box788.bluehost.com'
EMAIL_PORT = 465
EMAIL_HOST_USER = 'contact@doornox.com' 
EMAIL_HOST_PASSWORD = 'Zatalyst123!@#'
EMAIL_USE_SSL = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

STATIC_ROOT = os.path.join(BASE_DIR, "public", "static")

AWS_ACCESS_KEY_ID = 'AKIAJJ7XXSRDYYBB2EQQ'
AWS_SECRET_ACCESS_KEY = '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'

FB_GRAPH_URL = 'https://graph.facebook.com/me'
