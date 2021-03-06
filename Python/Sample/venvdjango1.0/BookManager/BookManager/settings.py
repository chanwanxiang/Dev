"""
Django settings for BookManager project.

Generated by 'django-admin startproject' using Django 1.11.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# __file__ 表示文件名称
# setting.py
# os.path.abspath 表示绝对路径
# os.path.dirname 表示文件目录

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'g$otf6x01uig-rzm13ad)*0_udbbb2h%l3jok*4*em-^skj017'

# SECURITY WARNING: don't run with debug turned on in production!
# 开发调试使用
DEBUG = True

# 安全机制
# 允许以哪个主机的形式访问
# 如果改变允许方式,需要将允许的IP/域名添加
ALLOWED_HOSTS = ['127.0.0.1','192.168.80.142']


# Application definition
# 安装注册子应用
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'login.apps.LoginConfig',
    'books.apps.BooksConfig',
    'payment.apps.PaymentConfig',
    # 子应用名
    # 子应用名.apps.子应用名Config
]

# 中间件
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # django默认开启了CSRF防护,会对POST,PUT,PATCH,DELETE进行CSRF防护验证
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 注册中间件
    # 请求前的执行顺序由注册顺序向下执行
    # 请求后的执行顺序由注册顺序向上执行
    'books.middleware.simpleMiddleware',

]

# 工程url的配置入口,默认是工程名.urls
ROOT_URLCONF = 'BookManager.urls'

# 模板相关配置信息
TEMPLATES = [
    {
        # 默认django自带模板
        # 'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 配置jinja2模板
        'BACKEND': 'django.template.backends.jinja2.Jinja2',
        # dirs 设置模板路径
        'DIRS': [os.path.join(BASE_DIR,'template')],
        'APP_DIRS': True,
        'OPTIONS': {
            # 默认
            # 'environment':'jinja2.Environment',
            # 指定jinja2环境
            'environment':'books.jinja2env.environment',
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'BookManager.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

# sqlite主要是一个嵌入式的关系型数据库,主要在移动端使用,属于小型关系型数据库
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': '127.0.0.1',
        'PORT': '3333',
        'USER': 'root',
        'PASSWORD': '123456',
        'NAME': 'bookmanager'
    }
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

LANGUAGE_CODE = 'zh-Hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

# 静态文件位置
STATICFILES_DIRS = [
    os.path.join(BASE_DIR,'static')
]