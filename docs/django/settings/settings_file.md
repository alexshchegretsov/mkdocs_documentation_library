```
# -*- coding: utf-8 -*-

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# Определяет путь до директории, в которой находится наш проект
#            4                3                2               1
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 1 __file__ - /home/alexander/Desktop/dev/spb_tut_ru/src/ENGINE_project/settings.py
# src.ENGINE_project.settings.__file__ == os.path.abspath(src.ENGINE_project.settings.__file__)
# 2 os.path.abspath(path) - абсолютный путь до path
# 3 os.path.dirname(path) - абсолютный путь до родительской директории в которой находится(аргумент)
# 4 см. # 3


# Безопасность нашего веб приложения
SECRET_KEY = 'qrm0ib1ma)3s6^px=zngop4au&w$q=oy&3p6s$e+p&&k3_*m^n'
# https://docs.djangoproject.com/en/2.1/ref/settings/#secret-key
# Используется для сессий, криптографических подписей(при общении с другими приложениями)

# Включает и отключает режим отладки проекта
DEBUG = True
# https://docs.djangoproject.com/en/2.1/ref/settings/#debug

# Для локалхост пойдёт и так
ALLOWED_HOSTS = ['*']
# https://docs.djangoproject.com/en/2.1/ref/settings/#allowed-hosts
# Список хостов, доменов для которых может работать наш сайт.
# сделано для безопасности, чтобы обезопасить от внедрения в куки или
# письма для сброса пароля ссылок на сторонний сайт подменив HTTP заголовок Host,
# Для реального сервера всё прописываем
# ALLOWED_HOSTS = ['https://spb-tut.ru', 'www.spb-tut.ru', 'spb-tut.ru']

# Здесь подключаются все приложения
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "django_extensions",
    "app",
    "index",
    "learn_models",
    "docs",

]
# https://docs.djangoproject.com/en/2.1/ref/settings/#installed-apps

# Подключение "промежуточных слоёв" - функций, которые могут обрабатывать запрос-ответ до и после вью-функций
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
# https://docs.djangoproject.com/en/2.1/topics/http/middleware/

# Путь до модуля, в котором находится диспетчер всех запросов, приходящих приложению
ROOT_URLCONF = 'ENGINE_project.urls'
# https://docs.djangoproject.com/en/2.1/ref/settings/#root-urlconf

# Настройки шаблонизатора
TEMPLATES = [
    {
        # Указывается шаблонизатор, который используется
        'BACKEND': 'django.template.backends.django.DjangoTemplates', # или Jinja2
        # Директории в которых шаблонизатор ищет шаблоны
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
            # если не будет видеть шаблоны приложения - добавлять вручную
            # хотя среда и якобы не видит наш путь, всё логично
            # и всё отрабатывает корректно,используя одну верхнюю настройку

            # os.path.join(BASE_DIR, 'app/templates'),
            # os.path.join(BASE_DIR, 'index/templates'),
            # os.path.join(BASE_DIR, 'learn_models/templates'),

        ],
        # Должен ли шаблонизатор искать файлы шаблонов в приложениях.
        'APP_DIRS': True,
        # доп. опции, для каждого шаблонизатора - разные
        'OPTIONS': {
            # список контекстных процессоров, которые вызываются при заполнении шаблона
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
# https://docs.djangoproject.com/en/2.1/ref/settings/#templates


# Путь к объекту WSGI приложения, которое будет использовать встроенный сервер Django
WSGI_APPLICATION = 'ENGINE_project.wsgi.application'
# https://docs.djangoproject.com/en/2.1/ref/settings/#wsgi-application


# Подключение базы данных и данные для входа в базу
import pymysql
pymysql.install_as_MySQLdb()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'test_db',
        'USER': 'testuser',
        'PASSWORD': 'Dexter89!',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

# Проверка паролей на надёжность
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
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

# Internationalization
# выбор языка для приложения
LANGUAGE_CODE = 'en-us'  # ru-ru
# https://docs.djangoproject.com/en/2.1/ref/settings/#language-code

# часовой пояс используемый в приложении
TIME_ZONE = 'Europe/Minsk' # utc + 3
# https://docs.djangoproject.com/en/2.1/ref/settings/#std:setting-TIME_ZONE

# Локализация
# При заданном USE_I18N = True, будут переведены основные элементы админки и вывод дат в шаблонах
USE_I18N = True
# https://docs.djangoproject.com/en/2.1/ref/settings/#use-i18n

# Когда включен параметр USE_L10N, django буде пытаться определить системную локаль пользователя,
# на основе заголовков Accept-Language, посылаемых браузером.
USE_L10N = True
# https://docs.djangoproject.com/en/2.1/ref/settings/#use-l10n

# указывает будет ли дата и время (datetime), которую мы будем использовать в приложении, привязана к вышеуказанному часовому поясу
USE_TZ = True
# https://docs.djangoproject.com/en/2.1/ref/settings/#use-tz

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

# Абсолютный путь к каталогу, в который collectstatic соберет все статические файлы.
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# https://docs.djangoproject.com/en/2.1/ref/settings/#static-root

# URL, указывающий на каталог со статическими файлами STATIC_ROOT.
STATIC_URL = '/static/'
# https://docs.djangoproject.com/en/2.1/ref/settings/#static-url



# каталоги со статическими файлами, которые будут найдены при использовании FileSystemFinder,
# например, при запуске команды collectstatic или findstatic
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'app/static'),
    os.path.join(BASE_DIR, 'index/static'),
    os.path.join(BASE_DIR, 'learn_models/static'),
]
# https://docs.djangoproject.com/en/2.1/ref/settings/#staticfiles-dirs

# джанго-утилиты по нахождению статики
STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
)
# https://docs.djangoproject.com/en/2.1/ref/settings/#staticfiles-finders


# Абсолютный путь к каталогу, в котором хранятся медиа-файлы
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# https://docs.djangoproject.com/en/2.1/ref/settings/#media-root

# URL который указывает на каталог MEDIA_ROOT
MEDIA_URL = '/media/'
# https://docs.djangoproject.com/en/2.1/ref/settings/#media-url

# Mkdocs
# https://www.mkdocs.org/#theming-our-documentation

# полный путь до нашего cайта документации
DOCS_DIR = os.path.join(BASE_DIR, 'docs/static/project_docs_build')

# сама папка в которой находится сайт документации
DOCS_STATIC_NAMESPACE = os.path.basename(DOCS_DIR)

# BASE_DIR = '/home/alexander/Desktop/dev/spb_tut_ru/src'
# DOCS_DIR = '/home/alexander/Desktop/dev/spb_tut_ru/src/docs/static/project_docs_build'
# DOCS_STATIC_NAMESPACE = 'project_docs_build'

# если хотим ограничить доступ к докам через @login_required
# прописать соответствующие имена для вью в урлах
from django.urls import reverse_lazy  # путь с версии 2
# старый путь до вресии 2 -from django.core.urlresolvers import reverse_lazy
# LOGIN_REDIRECT_URL = reverse_lazy('dasboard')
# LOGIN_URL = reverse_lazy('login')
# LOGOUT_URL = reverse_lazy('logout')

# Mkdocs end

```
