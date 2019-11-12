abstract
=

Значение abstract = True - делает нашу модель абстрактной.

*подробнее про абстрактную модель* [см. здесь](../model_types/abstract_model.md)

```
class Foo(models.Model):
    # общие поля
    created = models.DatetimeField(auto_now_add=True)
    updated = models.DatetimeField(auto_now=True)
   
    class Meta:
        abstract = True
```
