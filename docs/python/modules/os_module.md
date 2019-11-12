```python
# импортируем модуль по взаимодейcтвию с операционной системой
import os
```

### name

```python
# возвращает имя ОС
os.name
```




    'posix'



### environ


```python
# словарь переменных окружения. Изменяемый (можно добавлять и удалять переменные окружения).
os.environ
```

### getlogin
```python
# имя пользователя, вошедшего в терминал Unix
os.getlogin()
```




    'alexander'



### getpid

```python
# id текущего процесса
os.getpid()
```




    2369



### uname

```python
# информация об ОС
os.uname()
```




    posix.uname_result(sysname='Linux', nodename='nthng', release='4.15.0-64-generic', version='#73-Ubuntu SMP Thu Sep 12 13:16:13 UTC 2019', machine='x86_64')



### access

```python
# проверяет доступ к файлу у текущего пользователя -rwx------
# 0 - проверяет существует ли файл
# 1 - может ли пользователь запускать на исполнение(execute)
# 2 - может ли пользователь вносить изменение(write)
# 4 - может ли пользователь просто прочитать файл(read)
os.access("/home/alexander/test.py", 0)
```




    True
```
```
### getcwd

```python
# путь до директории в которой мы находимся, аналог pwd
path = os.getcwd()
print(path)
```

    /home/alexander/Desktop/django_test/src


### chdir

```python
# os.chdir - меняет рабочую директорию на указанную, так мы можем перемещаться по файловой системе, аналог cd
.chdir(f"{path}/ENGINE")
new_path = os.getcwd()
print(new_path)
```

    /home/alexander/Desktop/django_test/src/ENGINE


### listdir

```python
# os.listdir - показывает файлы в текущей директории, аналог ls -la
os.listdir(new_path)
```




    ['settings.py', 'urls.py', '__pycache__', 'wsgi.py', '__init__.py']



### mkdir

```python
# os.mkdir - создаёт директорию, аналог mkdir
os.mkdir(f"{new_path}/new_dir")
os.listdir(new_path)
```




    ['settings.py', 'urls.py', '__pycache__', 'new_dir', 'wsgi.py', '__init__.py']



### mkdirs

```python
os.makedirs - создаст все несуществующие директории по пути, аналог mkdir -p
```


### remove

```python
# os.remove - удаляет только файлы, не директории
path = f"{os.getcwd()}/new_dir"
os.remove(path)
os.listdir(new_path)
```


    ---------------------------------------------------------------------------

    IsADirectoryError                         Traceback (most recent call last)

    <ipython-input-19-e8a7fe7c5374> in <module>
          1 path = f"{os.getcwd()}/new_dir"
    ----> 2 os.remove(path)
          3 os.listdir(new_path)


    IsADirectoryError: [Errno 21] Is a directory: '/home/alexander/Desktop/django_test/src/ENGINE/new_dir'


### rmdir
```python
# Вручную создал в new-dir файл empty.py, его удалил при помощи os.remove
# и дальше удалили саму директорию new_dir при помощи os.rmdir, поскольку она удаляет
# только ПУСТЫЕ директории

path = f"{os.getcwd()}/new_dir"
os.remove(f"{path}/empty.py")
os.rmdir(path)
os.listdir(new_path)
```




    ['settings.py', 'urls.py', '__pycache__', 'wsgi.py', '__init__.py']




### rename

```python
# переименовываем new_dir в foo, аналог mv
os.rename(f"{os.getcwd()}/new_dir", "foo")
os.listdir(os.getcwd())

```




    ['settings.py', 'urls.py', '__pycache__', 'wsgi.py', 'foo', '__init__.py']


### removes

```python
# super-rename, переименовывает с созданием новых директорий по пути
os.renames(f"{os.getcwd()}/bar", f"{os.getcwd()}/foo/buzz")
os.listdir(os.getcwd())
```




    ['settings.py', 'urls.py', '__pycache__', 'wsgi.py', 'foo', '__init__.py']


### removedirs

```python
# удаляет директорию, затем пытается удалить родительские директории, и удаляет их рекурсивно, пока они пусты.
# здесь foo и buzz были пустыми, сначала удалили buzz, затем foo
os.removedirs(f"{os.getcwd()}/foo/buzz")
os.listdir(os.getcwd())
```




    ['settings.py', 'urls.py', '__pycache__', 'wsgi.py', '__init__.py']


### walk

```python
# генерация имён файлов в дереве каталогов, сверху вниз (если topdown равен True), 
# либо снизу вверх (если False). 
# Для каждого каталога функция walk возвращает кортеж (путь к каталогу, список каталогов, список файлов).
for i in os.walk(os.getcwd()): print(i)
```

    ('/home/alexander/Desktop/django_test/src/ENGINE', ['__pycache__'], ['settings.py', 'urls.py', 'wsgi.py', '__init__.py'])
    ('/home/alexander/Desktop/django_test/src/ENGINE/__pycache__', [], ['urls.cpython-37.pyc', 'settings.cpython-37.pyc', '__init__.cpython-37.pyc', 'wsgi.cpython-37.pyc'])

### truncate

```python
# обрезает файл до длины length.
 os.truncate(path, length)
```

### symlink

```python
# создание символической ссылки на файл с настройками, как "ярлык" в windows
os.symlink(f"{os.getcwd()}/settings.py", "symlink_settings")
os.listdir(os.getcwd())
```




    ['settings.py',
     'symlink_settings',
     'urls.py',
     '__pycache__',
     'wsgi.py',
     '__init__.py']


### system

```python
# забираем секретный ключ из файла настроек, в случае успешной операции - отдаёт 0
os.system("cat settings.py | grep SECRET_KEY > foo.py")
```




    0



 ### path

```python
# os.path - встроенный модуль по работе с путями
```
