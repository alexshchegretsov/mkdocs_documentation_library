`GenericForeignKey`
=

Если обычный ForeignKey используется для того, чтобы связаться с ОДНОЙ таблицей,
то GenericForeignKey позволяет иметь связи с НЕСКОЛЬКИМИ таблицами.

Для реализации этих связей нам понадобится:

- класс ContentType, который хранит в себе все модели, созданные в джанго в нашем проекте.
- object_id - первичный ключ(id конкретной строки) из таблицы с именем object_type
- object_type - ForeignKey на таблицу из ContentType
- класс GenericForeignKey, который и указывает на конкретную строчку(object_id) из конкретной таблицы(object_type)

```
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class Person(models.Model):
    name = models.CharField(max_length=30)


class Group(models.Model):
    name = models.CharField(max_length=30)
    creator = models.ForeignKey(Person, on_delete=models.PROTECT)


class Task(models.Model):
    description = models.CharField(max_length=100)

    # owner_id и owner_type формируют GFK
    owner_id = models.PositiveIntegerField()
    owner_type = models.ForeignKey(ContentType, on_delete=models.PROTECT)
    owner = GenericForeignKey("owner_type", "owner_id")
```
