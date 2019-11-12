`deploy to heroku`
=

- install gunicorn, psycopg2==2.7.5, dj-database-url, whitenoise (for images)
- setup postgresql in django
- import dj_databse_url in settings.py and add `db_from_env = dj_database_url.config()` and `DATABASES[‘default’].update(db_from_env)`
- create Procfile `web: gunicorn ENGINE.wsgi`
- Procfile and requirements.txt must be in manage.py directory
- `heroku login` - login to your heroku account
- `heroku create [app_name]` - create heroku app and git repo
- 'git remote add heroku [git repo heroku create previous]'- add heroku repo to our remote
- modified ALLOWED_HOSTS = ['0.0.0.0','your-herokuapp.com', 'www.your-herokuapp.com']
- `heroku config:set DJANGO_SECRET_KEY='dfsdf'` - add env variables to heroku app
- `STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')` - set static root and create statuc and media directories for collectstatic
```
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# https://docs.djangoproject.com/en/2.1/ref/settings/#static-root

# URL, указывающий на каталог со статическими файлами STATIC_ROOT.
STATIC_URL = '/static/'
# https://docs.djangoproject.com/en/2.1/ref/settings/#static-url

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# каталоги со статическими файлами, которые будут найдены при использовании FileSystemFinder,
# например, при запуске команды collectstatic или findstatic
STATICFILES_DIRS = [

]
# https://docs.djangoproject.com/en/2.1/ref/settings/#staticfiles-dirs

# джанго-утилиты по нахождению статики
STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
)

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
```
- в middleware добавляем после security.middleware  `'whitenoise.middleware.WhiteNoiseMiddleware'`
- ./manage.py collectstatic - собираем всю статику, создаст автоматически директорию staticfiles, которая нужна в heroku
- run `heroku run python manage.py makemigrations`
- run `heroku run python manage.py migrate`
- if need `heroku run python manage.py createsuperuser`

