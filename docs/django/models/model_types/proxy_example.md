В домашнем задании я, используя прокси модели, попытался запрограммировать начисление заработной платы
работникам предприятия с разными специальностями, ставками, тарифами, окладами.
Создал одну таблицу Employee(работник) и для каждой специальности создал менеджера, отвечающего за работу только со своей прокси моделью.
Модель далеко не идеальная и носит чисто презентативный характер.

Вначале код, после - проверка работы в юпитере.

```
from django.db import models

# кадровик, бизнесс аналитик, сеньор разработчик и тд..
specialization = (
    ("HR", "Human Resources"),
    ("BA", "Business Analyst"),
    ("SR", "Senior Developer"),
    ("M", "Middle Developer"),
    ("JR", "Junior Developer"),
)

# тариф оплаты
bet = (
    (1.1, 1.1),
    (1.25, 1.25),
    (1.5, 1.5),
    (2.0, 2.0),
)


# класс работник
class Employee(models.Model):
    full_name = models.CharField(max_length=100)
    salary = models.PositiveSmallIntegerField()
    bet = models.FloatField(choices=bet, default=1.25)
    worker_type = models.CharField(choices=specialization, max_length=3, default="JR")

    def __str__(self):
        return self.full_name


# создам менеджера для HR (отдел кадров)
class HRManager(models.Manager):
    # переопределяем родительский метод получения всех экземпляров модели, добавив фильтрацию
    def get_queryset(self):
        # вызов родительского метода get_queryset с нашей фильтрацией по полю worker_type
        return super().get_queryset().filter(worker_type="HR")

    # переопределяем метод создания работника под отдел кадров
    def create(self, **kwargs):
        # определяем тип работника - отдел кадров
        kwargs.update(worker_type="HR")
        # определяем ставку для отдела кадров
        kwargs.update(bet=1.1)
        return super().create(**kwargs)

    # добавляем менеджеру свой метод по вычислению зарплаты работнику из отдела кадров
    def show_payment(self):
        for worker in self.get_queryset():
            # вычисление зарплаты
            salary = int(worker.bet * worker.salary)
            print(f"{worker.full_name}, {worker.worker_type},bet: {round(worker.bet, 1)} salary is: {salary}")

    # метод который всем работникам отдела поднимает ставку на 0.3
    def raise_bet_all(self):
        for worker in self.get_queryset():
            worker.raise_bet()
            worker.save()

    # метод который уменьшает всем работникам ставку на 0.3
    def decrease_bet_all(self):
        for worker in self.get_queryset():
            worker.decrease_bet()
            worker.save()


# менеджер для работы с junior разработчиками
class JRManager(models.Manager):
    # переопределяем родительский метод, добавляя фильрацию по полю work_type
    def get_queryset(self):
        # вызов родительского get_queryset + наша фильтрация
        return super().get_queryset().filter(worker_type="JR")

    # переопределяем метод создание нового работника
    def create(self, **kwargs):
        # устанавливаем свою ставку
        kwargs.update(bet=1.5)
        kwargs.update(worker_type="JR")
        # вызываем родительский метод, и передаём в него отредактированные данные
        return super().create(**kwargs)

    def show_payment(self):
        for worker in self.get_queryset():
            # вычисление зарплаты
            salary = int(worker.bet * worker.salary)
            print(f"{worker.full_name}, {worker.worker_type},bet: {round(worker.bet, 1)} salary is: {salary}")

    # поднимаем тариф всем джуниор разработчикам
    def raise_bet_all(self):
        for worker in self.get_queryset():
            worker.raise_bet()
            worker.save()

    # уменьшаем тариф всем джуниор разрабтчикам
    def increase_bet(self):
        for worker in self.get_queryset():
            worker.increase_bet()
            worker.save()


class ProxyJR(Employee):
    # назначаем для нашей прокси модели менеджера
    jr_manager = JRManager()

    # определяем метаданные
    class Meta:
        # превращаем нашу модель в прокси для Employee
        proxy = True
        # сортировка от самого большого тарифа к меньшему
        ordering = ["-bet"]
        # определение имени модели во множественном числе в админке
        verbose_name_plural = "junior proxies"

    # поднять тариф на 0.5
    def raise_bet(self):
        self.bet = round(self.bet + 0.5, 1)

    # уменьшить тариф на 0.5
    def decrease_bet(self):
        if self.bet > 0.5:
            self.bet = round(self.bet - 0.5, 1)


# прокси модель для отдела кадров
class ProxyHR(Employee):
    # назначаем менеджера для прокси-модели
    objects = HRManager()

    # определяем метаданные
    class Meta:
        # превращаем модель в прокси для модели Employee
        proxy = True
        # сортируем по убыванию от самого большого тарифа
        ordering = ["-bet"]
        # определение имени модели во множественном числе в админке
        verbose_name_plural = "hr proxies"

    # поднять тариф работнику
    def raise_bet(self):
        self.bet = round(self.bet + 0.3, 1)

    # уменьшить тариф работнику
    def decrease_bet(self):
        if self.bet > 0.3:
            self.bet = round(self.bet - 0.3, 1)

```

Проверяем в юпитере, проверял только отдел HR, по аналогии можно дописывать менеджеры для любых отделов, модифицируя, изменяя поведение.


```python
from proxy.models import Employee, ProxyHR, ProxyJR
# заметим, что по умолчанию ставка = 1.25, и специализация=JR
```


```python
# создадим несколько работников в отдел HR
hr = [("Виолетта Францевна", 300), ("Лариса Антоновна", 320), ("Эльвира Марковна", 385)]
for data in hr:
    full_name, salary = data
    ProxyHR.objects.create(full_name=full_name, salary=salary)
```


```python
# проверяем
ProxyHR.objects.all()
```




    <QuerySet [<ProxyHR: Виолетта Францевна>, <ProxyHR: Лариса Антоновна>, <ProxyHR: Эльвира Марковна>]>




```python
# проверяем ставки отдела HR, должны быть отличные от 1.25
for i in ProxyHR.objects.all(): print(i.bet, end=" ")
```

    1.1 1.1 1.1 


```python
# теперь премируем рабтника и поднимем ему ставку
hr = ProxyHR.objects.get(full_name__startswith="Э")
hr.raise_bet()
hr.save()
hr, hr.bet
```




    (<ProxyHR: Эльвира Марковна>, 1.4)




```python
# теперь премируем всех 
ProxyHR.objects.raise_bet_all()
```


```python
# проверяем ставки отдела HR
for i in ProxyHR.objects.all(): print(round(i.bet, 1), end=" ")
```

    1.7 1.4 1.4 


```python
# рассчитаем каждому работнику зарплату, через метод, который добавили менеджеру
ProxyHR.objects.show_payment()
```

    Эльвира Марковна, HR,bet: 1.7 salary is: 654
    Виолетта Францевна, HR,bet: 1.4 salary is: 420
    Лариса Антоновна, HR,bet: 1.4 salary is: 448



```python
# то же самое можно сделать и для junior разработчиков, только со своей спецификой, ставками
```

