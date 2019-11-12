`Proxy model`
==

Прокси-модель — это модель, отнаследованная от существующей модели без создания новой таблицы в базе данных.
Прокси-модель используется для расширения существующей модели, когда в базе данных не нужно хранить дополнительную информацию, 
а нужно добавить базовой модели дополнительные методы или изменить ее Manager, управляющий запросами к базе данных, другими словами
прокси-модель - это ещё один интерфейс(помимо родительского) для работы с таблицей родительского класса.

Аналогия из жизни:

Платёжная карточка — это proxy для пачки наличных. И карточка, и наличные привязаны к одному банковскому счёту(таблице в БД). 
Для покупателя польза в том, что не надо таскать с собой тонны наличных, 
а владелец магазина рад, что ему не нужно делать дорогостоящую инкассацию наличности в банк — деньги поступают к нему на счёт напрямую.

[шаблон Proxy](https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%BC%D0%B5%D1%81%D1%82%D0%B8%D1%82%D0%B5%D0%BB%D1%8C_(%D1%88%D0%B0%D0%B1%D0%BB%D0%BE%D0%BD_%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F))

Простой пример создания прокси-модели для класса User из django.contrib.auth.models(администраторы сайта), в котором мы сортируем
администраторов в порядке убывания по полю username:

```
from django.contrib.auth.models import User

class ProxyUser(User):
    # метаданные
    class Meta:
        # превращаем модель в прокси-модель
        proxy = True
        # определяем порядок по убыванию
        ordering = ("-username",)

```
Проверяем через консоль:

```python
from django.contrib.auth.models import User
from models_app.models import ProxyUser
```


```python
# проверим как упорядочены записи через класс User
User.objects.all()
```




    <QuerySet [<User: admin>, <User: alex>]>




```python
# проверим порядок через прокси модель
ProxyUser.objects.all()
```




    <QuerySet [<ProxyUser: alex>, <ProxyUser: admin>]>




```python
# работает!
```
Отметим, что User.objects.all() и ProxyUser.objects.all() будут обращаться к одной и той же таблице базы данных. 
Единственное различие заключается в поведении, которое определяется для прокси-модели. Вот и все.


Прокси-модель должна наследоваться ровно от одного неабстрактного класса модели. 
Вы не можете наследовать от нескольких неабстрактных моделей, так как прокси-модель не обеспечивает связи между строками в разных 
таблицах базы данных. 
Прокси-модель может наследоваться от любого количества классов абстрактной модели, при условии, что они не определяют какие-либо поля модели. 
Модель прокси может также наследоваться от любого количества моделей прокси, которые имеют общий неабстрактный родительский класс.


Если вы не задаете менеджеров моделей в прокси-модели, он наследует менеджеров от своих родительских моделей. 
Если вы определите менеджера в прокси-модели, он станет стандартным, хотя все менеджеры, определенные в родительских классах, 
все еще будут доступны.


На простом примере рассмотрим создание своего менеджера для прокси модели. Исполнитель -> Альбом -> Песня.
Не забудем про абстрактную модель, в неё поместим общее поле и переопределим метод `__str__`.
Вспомним настройку `default_related_name` и укажем её для песен, по отношению к исполнителю и альбому.
И создадим прокси-модель для альбомов, менеджер которой по-умолчанию будет выводить все альбомы позже 1990 года.

```
# создание абстрактной модели
class CommonInfo(models.Model):
    # общее поле для всех классов
    name = models.CharField(max_length=120)
    
    # метаданные
    class Meta:
        # обращаем модель в абстрактную
        abstract = True

    # переопределяем отображение
    def __str__(self):
        return self.name


class Artist(CommonInfo):
    birth_year = models.PositiveSmallIntegerField()


class Album(CommonInfo):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    year = models.PositiveSmallIntegerField()


class Song(CommonInfo):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    duration = models.DurationField()

    class Meta:
        # определим имя обратной связи со стороны artist и album
        default_related_name = "composition"


# создаём менеджер, возвращающий все альбомы старше 1990 года
class AlbumManagerGreaterThan1990(models.Manager):
    # переопределяем родительский get_queryset, добавляя фильтрацию
    def get_queryset(self):
        return super(AlbumManagerGreaterThan1990, self).get_queryset().filter(year__gt=1990)


# создаём прокси-модель для альбомов
class ProxyAlbum(Album):
    # назначаем менеджера для прокси-модели
    objects = AlbumManagerGreaterThan1990()

    # метаданные
    class Meta:
        # обращаем модель в прокси-модель
        proxy = True

```
Воспроизводим наши Игрища в консоле:

```python
from models_app.models import Album, ProxyAlbum
```


```python
# выводим все альбомы
Album.objects.all()
```




    <QuerySet [<Album: Kill'em All>, <Album: Ride the lightning>, <Album: Master of puppets>, <Album: And justice for all...>, <Album: Black>]>




```python
# Прокси должен вывести только один альбом, он 1991 года
ProxyAlbum.objects.all()
```




    <QuerySet [<ProxyAlbum: Black>]>




```python
# работает как и предполагалось!
```
