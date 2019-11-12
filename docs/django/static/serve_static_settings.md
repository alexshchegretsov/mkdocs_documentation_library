`serve static settings`
=

- `STATIC_ROOT` - this folder creates after `./manage.py collectstatic` command, which collect all staticfiles at one directory.
- `STATICFILES_DIRS` - list of additional directories with staticfiles which not included in traditional `my_app/static/my_app/main.js`.
This setting defines the additional locations the staticfiles app will traverse if the FileSystemFinder finder is enabled, e.g. 
if you use the collectstatic or findstatic management command or use the static file serving view.
- `STATIC_URL` - URL to use when referring to static files located in `STATIC_ROOT`.
- `STATICFILES_FINDERS` - The list of finder backends that know how to find static files in various locations.

```
STATIC_URL = '/static/'

# эта папка создастся после комманды collectstatic, здесь будут все статик файлы, которые должен отработать nginx
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# дополнительные директории, вне приложений типа my_app/static/my_app/test.js
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

# джанго-утилиты по нахождению статики
STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
)

```

Конфигурация статик файлов в docker-compose:

- в приложении создаём тома
- папка самого приложения отображается в контейнере, соотв. все изменеия в контейнере будут сразу отображатся на файловой системе
- докер создаст том static_volume и свяжет его с контейнером /app/staticfiles (куда команда ./manage.py collectstatic будет складывать файлы).
Папка staticfiles создастся и на хосте, поскольку до этого мы создали том `.src:/app`.
Сами статик файлы будут храниться в static_volume адрес которого можно узнать при помощи `docker volume inspect static_volume`.
- В контейнере nginx мапим стаику на директорию /static и отображаем работу сос статикой в default.conf:
```
server {
  listen 8989;              # биндим nginx на порт 8989
  server_name localhost;

  location / {
    proxy_pass       http://web:8001;    # контейнер с приложением и порт на котором принимает запросы сервер приложения
    proxy_set_header Host      $host;
    proxy_set_header X-Real-IP $remote_addr;
    }

  location /static/ {               # обработка статики
    autoindex on;
    alias /static/;
  }
}


```


```
# application
web:
  volumes:
    - ./src:/app # bind mount
    - static_volume:/app/staticfiles  # STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

nginx:
  volumes:
    - static_volume:/static

volumes:
  static_volume:
```
