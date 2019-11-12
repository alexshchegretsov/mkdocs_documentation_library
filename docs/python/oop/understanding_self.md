понимание `self`
=

Перед тем как начать разговор о `self`, нужно понять что такое переменные класса и переменные экземпляра(атрибуты экземпляра).

Переменные класса - это переменные с "общим" доступом, т.е. любой экземпляр этого класса может к ним обратиться,получить значение и 
для каждого экземпляра значение будет одинаковое("общее").

Пременные экземпляра(или его атрибуты) - наоборот, уникальны для каждого экземпляра.

Переменные класса в питоне пишутся сразу после определения класса:
```
class Foo:
    # инициализируем переменные класса
    var_1 = "class variable"
    var_2 = 100 
```

В отличии от переменных класса, переменные(атрибуты) экземпляров определяются при помощи метода:
```
`
class Foo:
    # инициализируем переменные класса
    var_1 = "class variable"
    var_2 = 100

    def __init__(self, param_1, param_2):
        # инициализируем атрибуты экземпляра
        self.instance_param_1 = param_1
        self.instance_param_2 = param_2
```

Теперь создадим пару экземпляров и проверим дступ к переменным класса:

```
>>> obj_1 = Foo("1", 11)
>>> obj_2 = Foo("2", 22)
>>> obj_1.var_1
'class variable'
>>> obj_2.var_1
'class variable'
```
При доступе к переменной класса var_1 - нам возвращается одно и тоже значение, что естественно для переменной класса.
Теперь проверим доступ к атрибутам экземпляров:

```
>>> obj_1.instance_param_1
'1'
>>> obj_2.instance_param_1
'2'
```
В отличии от переменных класса, аттрибуты у каждого экземпляра свои.

`методы классов и методы экземпляров`
=

Также как есть переменные класса и атрибуты экземпляра, так существуют и методы класса и методы экземпляров этого класса.
