Установка/запуск jupyter notebook в django
==

Предполагается что установлено виртуальное окружение, django

1. pip install django-extensions
2. pip install jupyterlab
3. ./manage.py shell_plus --notebook
4. Если браузер блокирует - нажать advanced(mozilla) и продолжить

Документ можно перевести в pdf, md, py, html, tex, asciidoc, ipynb - нажатием file -> download as

Вот результат перевода в markdown:

```python
from mod.models import Comment, Post
from django.contrib.auth.models import User
```

поищем кое-чего при помощи mro
в отличии от bpython - здесь не нужно использовать цикл для человеческого построчного вывода


```python
User.mod_comment_related.related_manager_cls.mro()
```

    [django.db.models.fields.related_descriptors.create_reverse_many_to_one_manager.<locals>.RelatedManager,
     django.db.models.manager.Manager,
     django.db.models.manager.BaseManagerFromQuerySet,
     django.db.models.manager.BaseManager,
     object]

```

Пока без цветной индикации

