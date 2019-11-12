`setting Mkdocs with django`
=

1. Установить django, mkdocs, тему windwill(pip install mkdocs-windmill)
2. В проекте создать static, template директории
3. Создать приложение docs для документации, в нём создать static/docs_build папки
4. В главном урле прописать путь `path('docs/', include('docs.urls')),`
5. В docs создать urls и прописать:
```
from django.conf.urls import url
from .views import serve_docs

urlpatterns = [
    url(r'^(?P<path>.*)$', serve_docs),
]
```
6. Создать в views:
```
import os
from django.http import HttpResponse
from django.conf import settings
from django.contrib.staticfiles.views import serve
from django.shortcuts import render

def serve_docs(request, path):

    docs_path = os.path.join(settings.DOCS_DIR, path)
    if os.path.isdir(docs_path):
        path = os.path.join(path, 'index.html')

    path = os.path.join(settings.DOCS_STATIC_NAMESPACE, path)
    return serve(request, path, insecure=True)

```
7. Прописать в главных settings переменные:

```
# Абсолютный путь к каталогу, в который collectstatic соберет все статические файлы.
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# https://docs.djangoproject.com/en/2.1/ref/settings/#static-root

# URL, указывающий на каталог со статическими файлами STATIC_ROOT.
STATIC_URL = '/static/'
# https://docs.djangoproject.com/en/2.1/ref/settings/#static-url



# каталоги со статическими файлами, которые будут найдены при использовании FileSystemFinder,
# например, при запуске команды collectstatic или findstatic
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "docs/static"),
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
DOCS_DIR = os.path.join(BASE_DIR, 'docs/static/docs_build')

# сама папка в которой находится сайт документации
DOCS_STATIC_NAMESPACE = os.path.basename(DOCS_DIR)
```
8. Там же прописать папку templates
9. mkdocs new wiki
10. Конфигурация mkdocs.yml он берёт всё из wiki/docs и переносит в docs/static/docs_build при mkdocs build:
```
site_name: Weather app

docs_dir: "/home/alexander/Desktop/dev/weather_app/src/wiki/docs"
site_dir: "/home/alexander/Desktop/dev/weather_app/src/docs/static/docs_build"

nav:
    - index: "index.md"
    - description: "description/descr.md"     // создали в wiki/docs/descriptions/descr.md

theme:
    name: windmill

```
11. mkdocs build
12. ./manage.py collectstatic
13. ./manage.py runserver

Вроде бы так
