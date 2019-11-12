related_name
=

Ссылка обратной связи с моделью, в которой прописана связь.
Если related_name не указан, то django автоматически создаёт ссылку с названием вида [CLASS NAME RELATED]_set

- В OneToOne - ссылка на объект. Прямая ссылка на другой объект.
- В ManyToOne(ForeignKey) - это ссылка на объект со стороны Многих. И менеджер с методами, который возвращает QuerySet, со стороны Одного.
- В ManyToMany - это два менеджера.
- При использовании Абстрактного класса - необходима конструкция %(app_label)s и %(class)s - для идентификации дочерних классов.  

```
# OneToOne , прямые ссылки
class Address(models.Model):
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)


class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.PositiveSmallIntegerField()
    # создаём у Person ссылку на Address - address, создаём у Address ссылку на Person - pers
    address = models.OneToOneField(Address, related_name="pers", on_delete=models.CASCADE)



>>> p = Person.objects.get(first_name__startswith="a")
>>> p.address
# объект
<Address: Address object (1)>
>>> a = Address.objects.get(id=1)
>>> a.pers
# объект
<Person: Person object (1)>

```
```
# ManyToOne(ForeignKey), Many - Comment, Post. One - User
from django.db import models
from django.contrib.auth.models import User


class BaseMessage(models.Model):
    # чтобы уникально идентифицировать каждый класс со стороны Многих
    # используют %(app_label)s и %(class)s в related_name, т.е. имя приложения, в котором находится класс,
    # и имя самого класса, такая конструкция используется только с Абстрактными классами
    # здесь у класса User создаётся два менеджера для работы с Comment и Post
    # а у Post и Comment - ссылки с именем user на объект User.
    user = models.ForeignKey(User,
                             related_name="%(app_label)s_%(class)s_related",
                             on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Comment(BaseMessage):
    body = models.TextField(max_length=100)

    def __str__(self):
        return f'{self.body} | {self.user}'


class Post(BaseMessage):
    title = models.CharField(max_length=100)
    body = models.TextField()

    def __str__(self):
        return self.title



>>> c = Comment.objects.get(id=1)
>>> type(c.user)
<class 'django.contrib.auth.models.User'>
>>> 
>>> u = User.objects.get(id=1)
>>> type(u.mod_comment_related)
<class 'django.db.models.fields.related_descriptors.create_reverse_many_to_one_manager.<locals>.RelatedManager'>
>>> type(u.mod_post_related)
<class 'django.db.models.fields.related_descriptors.create_reverse_many_to_one_manager.<locals>.RelatedManager'>

# можно копнуть чуть глубже, и посмотреть что это за relatedManager
# иногда кажется что в django миллионы иерархий и всё запутано, из-за того что всё происходит под капотом
>>> for i in User.mod_comment_related.related_manager_cls.mro(): print(i)
... 
<class 'django.db.models.fields.related_descriptors.create_reverse_many_to_one_manager.<locals>.RelatedManager'>
<class 'django.db.models.manager.Manager'>
<class 'django.db.models.manager.BaseManagerFromQuerySet'>
<class 'django.db.models.manager.BaseManager'>
<class 'object'>
    

```


```
# ManyToMany
# здесь у класса Student появляется relatedManager под именем course_related
# у класса Course - relatedManager под именем student

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=100)
    # создаём связь с моделью Student, и создаём у Student менеджера для работы с Course
    student = models.ManyToManyField(Student, related_name="course_related")

    def __str__(self):
        return self.name

>>> s = Student.objects.get(name__istartswith="a")
>>> type(s.course_related)
<class 'django.db.models.fields.related_descriptors.create_forward_many_to_many_manager.<locals>.ManyRelatedManager'>
>>> 
>>> s.course_related.all()
<QuerySet [<Course: English>, <Course: Python>, <Course: Algorithms and data structures>, <Course: django>, <Course: OOP>]>
>>> 
>>> c = Course.objects.get(name__istartswith="e")
>>> type(c.student)
# Менеджер ManyRelatedManager
<class 'django.db.models.fields.related_descriptors.create_forward_many_to_many_manager.<locals>.ManyRelatedManager'>
>>> c.student.all()
# возвращает QuerySet
<QuerySet [<Student: Alex Shchegretsov>]>
>>> 
# та же иерархия
>>> Course.student.related_manager_cls
<class 'django.db.models.fields.related_descriptors.create_forward_many_to_many_manager.<locals>.ManyRelatedManager'>
>>> for i in Course.student.related_manager_cls.mro(): print(i)
... 
<class 'django.db.models.fields.related_descriptors.create_forward_many_to_many_manager.<locals>.ManyRelatedManager'>
<class 'django.db.models.manager.Manager'>
<class 'django.db.models.manager.BaseManagerFromQuerySet'>
<class 'django.db.models.manager.BaseManager'>
<class 'object'>

```
