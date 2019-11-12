Разрешение конфликтов с related_name в Абстрактном классе.
====

#### Пример

```
from django.contrib.auth.models import User


class BaseMessage(models.Model):
    user = models.ForeignKey(User,
    # фиксируем related_name="message" - вызовет исключение
                             related_name="message",
                             on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Comment(BaseMessage):
    body = models.TextField(max_length=101)


class Post(BaseMessage):
    title = models.CharField(max_length=100)
    body = models.TextField()
```

- Если зафиксировать related_name(без app_label или class), то при попытки миграций выскочит исключение SystemCheckError:
```
SystemCheckError: System check identified some issues:

ERRORS:
mod.Comment.user: (fields.E304) Reverse accessor for 'Comment.user' clashes with reverse accessor for 'Post.user'.
        HINT: Add or change a related_name argument to the definition for 'Comment.user' or 'Post.user'.
...
...
...
```
#### Которое говорит о том, что со стороны Одного к каждому классу из Многих обратная ссылка должна быть уникальной.
 
Поскольку определив related_name как "message", и, написав User.message - django не поймёт, это мы обращаемся к Post или к Comment, поэтому выбрасывается исключение.

- Если просто сменить имя дочернего класса - ничего не даст, та же ошибка по той же причине, что и выше.
- Если изменить related_name - ничего не даст, та же ошибка, по той же причине.
- Если сменить и название класса и related_name - ничего не даст. Ошибка та же: поскольку у Одного только одна
ссылка на два класса (пусть в примере у Многих два класса), а должно быть равно количеству классов у Многих.

Выходом будет использование %(class)s в related_name, при условии что наши модели из одного приложения(app),
и использование %(app_label) вместе с %(class)s - если у нас есть импорты из других приложений, поскольку 
в разных приложениях название классов может совпадать, в то время как имена приложений всегда уникальны в рамках проекта.
