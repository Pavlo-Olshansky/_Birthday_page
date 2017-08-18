import os
from django.core.exceptions import ImproperlyConfigured
from decouple import config

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Get ENV VARIABLES key
ENV_ROLE = config("ENV_ROLE")

#SECURITY WARNING: don't run with debug turned on in production!
SECRET_KEY = config('SECRET_KEY_Birthday_website')
DEBUG = config('DEBUG', default=False, cast=bool)


from decouple import config, Csv

ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    # 'django.contrib.humanize',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'disqus',
    'home',

]

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',

]

ROOT_URLCONF = 'Vitalik_birthday.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(os.path.dirname(__file__), 'templates'), ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'Vitalik_birthday.wsgi.application'
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'



# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases
if ENV_ROLE == 'development':
    DB_PASS_Birthday_website = config("DB_PASS_Birthday_website")
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'Vitalik_birthday',
            'USER': 'postgres',
            'PASSWORD': DB_PASS_Birthday_website,
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }
else:
    import dj_database_url
    DATABASES = {
    'default': dj_database_url.config(
        default=config('DATABASE_URL')
        )
    }



# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
    )

# # Disquas comments Settings
DISQUS_API_KEY = config("DISQUS_API_KEY")
DISQUS_WEBSITE_SHORTNAME = 'happy-birthday'


# # reCapch key settings
# GOOGLE_RECAPTCHA_SECRET_KEY='6LdglCgUAAAAAP_E36HbImYCOEhK00yXl7wvaWsD'
