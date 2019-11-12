`Multi-table`
==

При использовании multi-table наследования - каждая модель соответствует таблице в базе данных.
В дочерних моделях неявно создаётся OneToOne связь с родительской.
Со стороны дочернего класса связь один-к-одному осуществляется через указатель [имя родительского класса]_ptr
Перед обращением к дочерней таблице, выполняется JOIN с родительской, как следствие доп.расходы производительности.
```
# multi-table модель, или multi-table наследование
class BaseContent(models.Model):
    # определяем общие поля для дочерних моделей, которые будут храниться в этой таблице
    title = models.CharField(max_length=120)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
 
    # переопределяем вывод на экран
    def __str__(self):
        return self.title


# наследуемся от BaseContent
class Message(BaseContent):
    body = models.TextField()
    # неявно создаётся OneToOne связь с родительской моделью
```

Воспроизведём наши Игрища в консоли:

```python
from models_app.models import BaseContent, Message

```


```python
# создаём сообщение
Message.objects.create(title="message title", body="message body")
```




    <Message: message title>




```python
# проверяем что при создании сообщения, заголовок создался в таблице BaseContent,
# а body - в таблице Message
b = BaseContent.objects.get(title="message title")
b
```




    <BaseContent: message title>




```python
# теперь проверяем связь один-к-одному с таблицей Message
message = b.message
message.body
```




    'message body'




```python
# проверим связь со стороны message
message.basecontent_ptr, message.basecontent_ptr_id
```




    (<BaseContent: message title>, 5)




```python

```

