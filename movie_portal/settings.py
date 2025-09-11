from pathlib import Path
import os
import dj_database_url
import cloudinary

if os.path.isfile('env.py'):
    import env

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY")


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get("DEBUG")

ALLOWED_HOSTS = []
CSRF_TRUSTED_ORIGINS = []

host = os.environ.get("HOST")
if host:
    ALLOWED_HOSTS.append(host)
    CSRF_TRUSTED_ORIGINS.append(f"https://{host}")


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cloudinary_storage',
    'cloudinary',
    'crispy_forms',
    'crispy_bootstrap5',
    'home',
    'bookings',
    'menu',
    'films',
    'user_account',
    'management',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
]


AUTHENTICATION_BACKENDS = [
    'allauth.account.auth_backends.AuthenticationBackend',
    'django.contrib.auth.backends.ModelBackend'
]

SITE_ID = 1
ACCOUNT_LOGOUT_REDIRECT_URL = '/'
LOGIN_REDIRECT_URL = '/'


ACCOUNT_LOGIN_METHODS = {"email"}


ACCOUNT_SIGNUP_FIELDS = [
    'first_name*', 'last_name*', 'email*', 'password1*', 'password2*'
    ]


ACCOUNT_FORMS = {
    'signup': 'user_account.forms.CustomSignupForm',
}


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = 'movie_portal.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR],
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


WSGI_APPLICATION = 'movie_portal.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators


validators = [
    'UserAttributeSimilarityValidator',
    'MinimumLengthValidator',
    'CommonPasswordValidator',
    'NumericPasswordValidator'
    ]


AUTH_PASSWORD_VALIDATORS = [
    {'NAME': f'django.contrib.auth.password_validation.{v}'}
    for v in validators
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

cloudinary.config(
    secure=True
)