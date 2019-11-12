`self` и `__self__`
=

`self` - это ссылка на конкретный экземпляр класса, которая предоставляет методам доступ к атрибутам этого экземпляра.
Стоит отметить:

- Если метод вызвать через класс - то это обычный объект, экзепляр класса `function`.
- Если метод вызвать через экземпляр - то мы получим новый объект- `bound method` - связанный метод, 
который и позволяет объединить в себе сам экземпляр и функцию.


```

>>> 
>>> class A:
...     def foo(self):
...         pass
...     
... 
>>> a = A()
>>> a
<__main__.A object at 0x7fa7e1624470>
>>> # вызовем функцию со стороны класса, это будет функция
>>> A.foo
<function A.foo at 0x7fa7e16316a8>
>>> 
>>> # вызовем функцию со стороны экземпляра, это будет связанный метод
>>> a.foo
<bound method A.foo of <__main__.A object at 0x7fa7e1624470>>
>>> # в котором написано что функция A.foo связана с экземпляром класса А, который "живёт" под таким идентификатором 0x7fa7e1624470 !!!
>>> 
>>> # посмотрим экземпляром какого класса является этот связанный метод
>>> a.foo.__class__
<class 'method'>
>>> 
>>> # теперь посмотрим какие атрибуты есть у связанного метода, там должны быть ссылки на наш экземпляр класса А и функцию
>>> for i in dir(a.foo): print(i)
... 
__call__
__class__
__delattr__
__dir__
__doc__
__eq__
__format__
__func__     # здесь функция A.foo
__ge__
__get__
__getattribute__
__gt__
__hash__
__init__
__init_subclass__
__le__
__lt__
__ne__
__new__
__reduce__
__reduce_ex__
__repr__
__self__     # здесь экземпляр а
__setattr__
__sizeof__
__str__
__subclasshook__
>>> 
>>> # мы видим два метода: __self__ и __func__, вызовем их
>>> a.foo.__func__
<function A.foo at 0x7fa7e16316a8>
>>> # __func__ - ссылка на объект функции foo 
>>> 
>>> a.foo.__self__
<__main__.A object at 0x7fa7e1624470>
>>> # ссылка на объект "а" класса А

```  