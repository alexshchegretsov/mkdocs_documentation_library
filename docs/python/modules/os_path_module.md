#### basename

```python
# определяет поледнюю точку в пути
os.path.basename(f"{os.getcwd()}")
```




    'src'



#### abspath

```python
# возвращает полный путь до папки или файла
os.path.abspath("afafasd")
```




    '/home/alexander/Desktop/django_test/src/afafasd'



#### dirname

```python
# возвращает путь к родительской директории
os.path.dirname(f"{os.getcwd()}/ENGINE/settings.py")
```




    '/home/alexander/Desktop/django_test/src/ENGINE'



#### exists

```python
# существует ли указанный путь
os.path.exists("/home/alexander")
```




    True


#### expanduser

```python
# возвращает путь к пользовательской папке
os.path.expanduser("~")
```




    '/home/alexander'


#### getatime

```python
# возвращает время последнего доступа к файлу или папке, в виде количесвта секунд, прошедших с начала эпохи.
os.path.getatime(f"{os.getcwd()}/ENGINE/settings.py")
```




    1570149039.7123177


#### getctime

```python
# возвращает дату создания файла или папки, в виде количества секунд, прошедших с начала эпохи
os.path.getctime(f"{os.getcwd()}/ENGINE/settings.py")
```




    1570148564.3467007


#### getmtime

```python
# возвращает время последнего внесения изменения в файл или папку, в виде количесвта секунд, прошедших с начала эпохи
os.path.getmtime(f"{os.getcwd()}/ENGINE")
```




    1570150090.0043964


#### getsize

```python
# возвращает размер файла или папки
os.path.getsize(f"{os.getcwd()}")
```




    4096


#### join

```python
# объединяет пути
new_path = os.path.join(os.getcwd(), "foo/bar/buzz")
print(new_path)
```

    /home/alexander/Desktop/django_test/src/foo/bar/buzz


#### isabs

```python
# проверяет путь на абсолютность
os.path.isabs("src/ENGINE")
```




    False




```python
os.path.isabs("/home/alexander/Desktop/django_test/src/ENGINE")
```




    True



#### isdir
```python
# является ли указанный путь катологом
os.path.isdir(os.getcwd())
```




    True




```python
os.path.isdir(f"{os.getcwd()}/ENGINE/settings.py")
```




    False



#### isfile

```python
# проверяет, указывает ли путь к файлу
os.path.isfile(f"{os.getcwd()}/ENGINE/settings.py")
```




    True


#### islink

```python
# проверяет, указывает ли путь к символической ссылке
os.path.islink(f"{os.getcwd()}/ENGINE/symlink_settings")
```




    True



#### realpath

```python
# возвращает путь к файлу символьной ссылки
os.path.realpath(f"{os.getcwd()}/ENGINE/symlink_settings")
```




    '/home/alexander/Desktop/django_test/src/ENGINE/settings.py'


#### split

```python
# возвращает кортеж из пары строк - (путь к родителской папке, название файла).
os.path.split('/home/alexander/Desktop/django_test/src/ENGINE/settings.py')
```




    ('/home/alexander/Desktop/django_test/src/ENGINE', 'settings.py')


#### splitext

```python
# возвращает кортеж из пары строк - (путь к файлу без расширения, расширение файла)
os.path.splitext('/home/alexander/Desktop/django_test/src/ENGINE/settings.py')
```




    ('/home/alexander/Desktop/django_test/src/ENGINE/settings', '.py')




```python

```
