"""
Django settings for imagex project.

Generated by 'django-admin startproject' using Django 2.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'm&sd!*%d)rt&67n^6f1@r%gxhlwe9s5o4)_#*9mh^xjxopk%0u'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    # 'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    # 'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    # 'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'imagex.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates')
        ],
        'APP_DIRS': False,
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

WSGI_APPLICATION = 'imagex.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

# 创建图片存放路径
CHECK_IMG_PATH = os.path.join(BASE_DIR, 'check-img')
if not os.path.isdir(CHECK_IMG_PATH):
    os.mkdir(CHECK_IMG_PATH)

# 创建日志的路径
LOG_PATH = os.path.join(BASE_DIR, 'log')
# 如果地址不存在，则会自动创建log文件夹
if not os.path.isdir(LOG_PATH):
    os.mkdir(LOG_PATH)
LOGGING = {
    # version 值只能为1
    'version': 1,
    # True 表示禁用loggers
    'disable_existing_loggers': False,

    # < 格式化 >
    'formatters': {
        # 可以设置多种格式，根据需要选择保存的格式
        'default': {
            'format': '%(levelname)s %(funcName)s %(module)s %(asctime)s %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(module)s %(asctime)s %(message)s'
        }
    },

    # < 处理信息 >
    'handlers':{
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stdout',   # 文件重定向的配置，将打印到控制台的信息都重定向出去 python manage.py runserver >> /home/aea/log/test.log
            # 'stream': open('/home/aea/log/test.log','a'), # 虽然成功了，但是并没有将所有内容全部写入文件，目前还不清楚为什么
            'formatter': 'default'     # 制定输出的格式，注意 在上面的formatters配置里面选择一个，否则会报错
        },

        'stu_handlers': {
            'level': 'DEBUG',
            # 指定日志文件大小，若超过指定的文件大小，会再生成一个新的日志文件保存日志信息
            'class': 'logging.handlers.RotatingFileHandler',
            # 指定文件大小
            # 1M=1024kb 1kb=1024b
            'maxBytes': 5 * 1024 * 1024,
            # 文件地址
            'filename': '%s/log.txt' % LOG_PATH,
            # 指定保存格式
            'formatter': 'default'
        },
        # 'uauth_handlers': {
        #     'level': 'DEBUG',
        #     # 若日志超过指定文件的大小，会再生成一个新的日志文件保存日志信息
        #     'class': 'logging.handlers.RotatingFileHandler',
        #     # 指定文件大小
        #     # 1M=1024kb 1kb=1024b
        #     'maxBytes': 5 * 1024 * 1024,
        #     # 文件地址
        #     'filename': '%s/uauth_log.txt' % LOG_PATH,
        #     # 指定保存格式
        #     'formatter': 'simple'
        # }
    },
    'loggers': {
        'cmd': {
            'handlers': ['console', 'stu_handlers'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },

    'filters': {
        
    }
}