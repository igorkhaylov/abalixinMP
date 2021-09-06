import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-v73yr-vj-m595_lrhj1k@nqjrq$c=ovc4on9c0l+ipvj4jf6(y'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'modeltranslation',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ckeditor',
    'ckeditor_uploader',
    'sorl.thumbnail',
    'main',
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

ROOT_URLCONF = 'abalixinMP.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
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

WSGI_APPLICATION = 'abalixinMP.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

MODELTRANSLATION_DEFAULT_LANGUAGE = 'ru'

gettext = lambda s: s
LANGUAGES = (
    ('ru', 'Russian'),
    # ('en', 'English'),
    ('uz', 'Uzbek'),
)


LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)


LANGUAGE_CODE = 'ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CKEDITOR_UPLOAD_PATH = "uploads/"


CKEDITOR_CONFIGS = {
    'skin': 'moono',
    'default': {
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['Bold', 'Italic', 'Underline'],
            ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'JustifyLeft', 'JustifyCenter',
             'JustifyRight', 'JustifyBlock'],
            ['Link', 'Unlink'],
            ['RemoveFormat', 'Source', "Youtube", "Image"]
        ],
        'extraPlugins': ','.join([
            'youtube',
        ]),
    },
    'my_config': {
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ["Source", "Templates", 'Format', 'Font', 'FontSize', 'Maximize', 'ShowBlocks'], '/',
            ['Image', 'Youtube', 'Table', 'Bold', 'Italic', 'Underline', 'Strike', 'Indent', 'Outdent',
             'HorizontalRule'],
            ['JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', 'Blockquote', 'NumberedList'],
            ['BulletedList', 'TextColor', 'BGColor', 'Link', 'Smiley', 'SpecialChar'], '/',
            ['Find', 'Subscript', 'Superscript'], '/',
            [], '/',
            [], '/',
        ],
        'extraPlugins': ','.join([
            'uploadimage',
            # 'youtube',
        ]),
    },
    'for_church': {
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ["Source", 'Font', 'FontSize', 'Maximize', 'ShowBlocks'], '/',
            ['Image', 'Youtube', 'Table', 'Bold', 'Italic', 'Underline', 'Strike', 'Indent', 'Outdent',
             'HorizontalRule'],
            ['JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', 'Blockquote', 'NumberedList'],
            ['BulletedList', 'TextColor', 'BGColor', 'Link', 'Smiley', 'SpecialChar'], '/',
            ['Find', 'Subscript', 'Superscript'], '/',
            [], '/',
            [], '/',
        ],
        'extraPlugins': ','.join([
            # 'uploadimage',
            'youtube',
        ]),
    },
    'schedule': {
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['Font',  'Maximize'], '/',
            ['Table', 'Bold', 'Italic', 'Underline',
             'HorizontalRule'],
            ['BulletedList', 'TextColor', 'BGColor', 'Link', 'Smiley', 'SpecialChar'], '/',
            ['Find', 'Subscript', 'Superscript'], '/',
            [], '/',
            [], '/',
        ],
    },
}

