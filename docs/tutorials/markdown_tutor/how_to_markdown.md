# Заголовки

# H1 - `# H1`
## H2 - `## H2`
### H3 - `### H3`
#### H4 - `#### H4`
##### H5 - `##### H5`
###### H6 - `###### H6`

или

H1 - `H1 подчёркивание =` 
=
    
    
H2 - `H2 подчёркивание -`
-

Выделение
=

_курсив_ - `_курсив_` или `*курсив*`

__полужирный__ - `__полужирный__` или `**полужирный**`

~~зачёркнутый текст~~ - `~~зачёркнутый текст~~`

Списки
=

#### Нумерованный

1. раз - `1. раз`
2. два - `2. два`
3. три - `3. три`
4. четыре - `4. четыре`

#### Ненумерованный

- раз - `- раз`
- два - `- два`
- три - `- три`
- четыре - `- четыре`


Ссылки
=

[ссылка](https://ya.ru) - `[ссылка](https://ya.ru)`

[ссылка с подсказкой при наведении](https://ya.ru "сайт Яндекс") - `[ссылка с подсказкой при наведении](https://ya.ru "сайт Яндекс")`

[относительная ссылка на документ](../markdown_tutor/how_to_markdown.md) - `[относительная ссылка на документ](../markdown_tutor/how_to_markdown.md)`

http://github.com - `http://github.com `

Изображения
=

Внутри строки:  
![alt-текст](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Текст заголовка логотипа 1") - `Внутри строки:  
![alt-текст](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Текст заголовка логотипа 1")`


В сноске:  
![alt-текст][logo] - `![alt-текст][logo]`

[logo]: https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Текст заголовка логотипа 2"
`[logo]: https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Текст заголовка логотипа 2"
`


Код
=

```python

class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    
    def __str__(self):
        return f'{self.first_name}'
```
`last_name = models.CharField(max_length=50)`

<pre><code class="python">

class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    
    def __str__(self):
        return f'{self.first_name}'
</pre>

Цитаты
=

As Kanye West said:

> We're living the future so 
> the present is our past.

```
As Kanye West said:

> We're living the future so 
> the present is our past.
```

Таблицы
=

Таблицы не являются частью Markdown, но многие обработчики, 
например Markdown Here и Github, поддерживают их. 
Они позволяют легко добавить таблицы в электронное письмо -- 
в других случаях для этого нужно копировать их из другого приложения.

Вертикальные линии обозначают столбцы.

| Таблицы       | Это                | Круто |
| ------------- |:------------------:| -----:|
| столбец 3     | выровнен вправо    | $1600 |
| столбец 2     | выровнен по центру |   $12 |
| зебра-строки  | прикольные         |    $1 |


```
Вертикальные линии обозначают столбцы.

| Таблицы       | Это                | Круто |
| ------------- |:------------------:| -----:|
| столбец 3     | выровнен вправо    | $1600 |
| столбец 2     | выровнен по центру |   $12 |
| зебра-строки  | прикольные         |    $1 |

```

HTML
=

Часто Markdown понимает чистый HTML.

<ul>
    <li>1</li>
    <li>2</li>
    <li>3</li>
</ul>
```
<ul>
    <li>1</li>
    <li>2</li>
    <li>3</li>
</ul>
```
