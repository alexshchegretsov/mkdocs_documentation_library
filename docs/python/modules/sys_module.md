Модуль содержит переменные и функции, имеющие отношение к интерпретатору и его окружению.


#### api_version
```python
# Целочисленное представление версии C API интерпретатора Python. Используется при работе с модулями расширений.
sys.api_version
```




    1013



#### argv
```python
# Список параметров командной строки, передаваемых программе. Элемент argv[0] хранит имя программы.
sys.argv
```




    ['/home/alexander/Desktop/django_test/.venv/lib/python3.7/site-packages/ipykernel_launcher.py',
     '-f',
     '/home/alexander/.local/share/jupyter/runtime/kernel-b0ef57b7-478f-4a50-aaa9-0d897ec14491.json',
     '--ext',
     'django_extensions.management.notebook_extension']



#### builtin_module_names
```python
# Кортеж с именами модулей, встроенных в исполняемый файл интерпретатора Python.
sys.builtin_module_names[:5]
```




    ('_abc', '_ast', '_bisect', '_blake2', '_codecs')



#### byteorder
```python
# Порядок следования байтов, используемый аппаратной платформой: 
# little – обратный порядок следования байтов, big – прямой.
sys.byteorder
```




    'little'



#### copyright
```python
# Строка с текстом, содержащим упоминание об авторских правах.
sys.copyright
```




    'Copyright (c) 2001-2019 Python Software Foundation.\nAll Rights Reserved.\n\nCopyright (c) 2000 BeOpen.com.\nAll Rights Reserved.\n\nCopyright (c) 1995-2001 Corporation for National Research Initiatives.\nAll Rights Reserved.\n\nCopyright (c) 1991-1995 Stichting Mathematisch Centrum, Amsterdam.\nAll Rights Reserved.'



#### displayhook
```python
# Функция, отвечающая за отображение и вывод информации в интерпретаторе, сохраняет результат в переменную _
help(sys.__displayhook__)
```

    Help on built-in function displayhook in module sys:
    
    displayhook(...)
        displayhook(object) -> None
        
        Print an object to sys.stdout and also save it in builtins._
    


#### dont_write_bytecode
```python
# Логический флаг, который определяет, должен ли интерпретатор Python создавать файлы с байт-кодом 
# (с расширением .pyc или .pyo) при импортировании модулей. 
# Начальное значение True, если интерпретатор не был вызван с ключом -B. 
# Программа может изменять значение этой переменной по своему усмотрению.
sys.dont_write_bytecode
```




    False



#### excepthook
```python
# Функция, выводящая исключение на выход stderr
sys.__excepthook__
```




    <function sys.excepthook>



#### exec_prefix
```python
# Директория, в которую были установлены платформозависимые файлы, т.е. в текущее виртуальное окружение.
sys.exec_prefix
```




    '/home/alexander/Desktop/django_test/.venv'


#### executable

```python
# Имя исполняемого файла интерпретатора.
sys.executable
```




    '/home/alexander/Desktop/django_test/.venv/bin/python'



#### flags
```python
# Объект, представляющий различные параметры командной строки, 
# которые были переданы при запуске самому интерпретатору Python 
# usage: python3 [option] ... [-c cmd | -m mod | file | -] [arg] ...
sys.flags
```




    sys.flags(debug=0, inspect=0, interactive=0, optimize=0, dont_write_bytecode=0, no_user_site=0, no_site=0, ignore_environment=0, verbose=0, bytes_warning=0, quiet=0, hash_randomization=1, isolated=0, dev_mode=False, utf8_mode=0)


#### float_info

```python
# Хранит информацию о внутреннем представлении чисел с плавающей точкой.
sys.float_info
```




    sys.float_info(max=1.7976931348623157e+308, max_exp=1024, max_10_exp=308, min=2.2250738585072014e-308, min_exp=-1021, min_10_exp=-307, dig=15, mant_dig=53, epsilon=2.220446049250313e-16, radix=2, rounds=1)


#### hexversion

```python
# Целое число, в шестнадцатеричном представлении которого закодирована информация о номере версии, 
# содержащемся в переменной sys.version_info. 
# Значение этой переменной всегда гарантированно увеличивается с выходом новой версии интерпретатора.
sys.hexversion
```




    50791664


#### version_info

```python
# Версия интерпретатора 
sys.version_info
```




    sys.version_info(major=3, minor=7, micro=4, releaselevel='final', serial=0)


#### last_type

```python
# Тип последнего исключения. 
# Обратите внимание, что в многопоточных приложениях не гарантируется достоверность информации переменной, 
# поэтому рекомендуется пользоваться функцией sys.exc_info().
sys.last_type
```




    AttributeError



#### last_value
```python
# Экземпляр последнего исключения. 
# Обратите внимание, что в многопоточных приложениях не гарантируется достоверность информации переменной, 
# поэтому рекомендуется пользоваться функцией sys.exc_info().
sys.last_value
```




    AttributeError("module 'sys' has no attribute 'last_tracebak'")


#### last_traceback

```python
# Объект с трассировочной информацией. 
# Обратите внимание, что в многопоточных приложениях не гарантируется достоверность информации переменной, 
# поэтому рекомендуется пользоваться функцией sys.exc_info().
sys.last_traceback
```




    <traceback at 0x7f77640857d0>


#### maxsize

```python
# Максимально возможное целое число, поддерживаемое типом size_t языка C в системе. 
# Это значение определяет максимально возможную длину строк, списков, словарей и других встроенных типов.
sys.maxsize
```




    9223372036854775807


#### maxunicode

```python
# Целое число, определяющее наибольший кодовый пункт Юникода, который может быть представлен. 
# По умолчанию имеет значение 65 535 для 16-битной кодировки UCS-2. 
# Если при сборке интерпретатор Python был настроен на использование кодировки UCS-4, это число будет больше.
sys.maxunicode
```




    1114111



#### modules
```python
# Словарь, который отображает имена модулей в объекты модулей.
sys.modules["sys"]
```




    <module 'sys' (built-in)>



#### path
```python
# Список строк, определяющих путь поиска модулей. 
# Первый элемент списка всегда содержит путь к каталогу, в котором находился сценарий, 
# использованный для запуска интерпретатора (если доступен).
sys.path
```




    ['/home/alexander/Desktop/django_test/src',
     '/home/alexander/Desktop/django_test/.venv/lib/python37.zip',
     '/home/alexander/Desktop/django_test/.venv/lib/python3.7',
     '/home/alexander/Desktop/django_test/.venv/lib/python3.7/lib-dynload',
     '/usr/lib/python3.7',
     '',
     '/home/alexander/Desktop/django_test/.venv/lib/python3.7/site-packages',
     '/home/alexander/Desktop/django_test/.venv/lib/python3.7/site-packages/IPython/extensions',
     '/home/alexander/.ipython']


#### platform

```python
# Строка, идентифицирующая платформу
sys.platform
```




    'linux'



#### ps1
```python
# Текст основного приглашения к вводу интерпретатора. >>>. 
# При назначении других значений для получения текста приглашения будут использоваться методы str() 
# назначенных объектов.
sys.ps1
```




    'In : '



#### ps2
```python
# Текст дополнительного приглашения к вводу интерпретатора. …. 
# При назначении других значений для получения текста приглашения будут использоваться методы str() 
# назначенных объектов.
sys.ps2
```




    '...: '


#### stdin

```python
# Объект файла, соответствующий потоку стандартного ввода. 
# Переменная используется функциями raw_input() и input(). 
# переменной можно назначить любые объекты, поддерживающие метод write(), 
# принимающий единственный строковый аргумент.
sys.stdin
```




    <_io.TextIOWrapper name='<stdin>' mode='r' encoding='UTF-8'>


#### stdout

```python
# Объекты файла, соответствующий потоку стандартного вывода. 
# Переменная используется инструкцией print для вывода значений аргументов и 
# функциями raw_input() и input() – для вывода приглашения к вводу. 
# переменной можно назначить любые объекты, поддерживающие метод write(), 
# принимающий единственный строковый аргумент.
sys.stdout
```




    <ipykernel.iostream.OutStream at 0x7f7768f44410>


#### stderr

```python
# Объекты файла, соответствующий потоку стандартного вывода сообщений об ошибках. 
# Переменная используется интерпретатором для вывода приглашения к вводу и сообщений об ошибках. 
# переменной можно назначить любые объекты, поддерживающие метод write(), 
# принимающий единственный строковый аргумент
sys.stderr
```




    <ipykernel.iostream.OutStream at 0x7f7768f44510>


#### version

```python
# Номер версии интерпретатора
sys.version
```




    '3.7.4 (default, Sep  2 2019, 20:47:34) \n[GCC 7.4.0]'


#### getrecursionlimit

```python
# Возвращает ограничение на количество рекурсивных вызовов функций.
sys.getrecursionlimit()
```




    3000


#### getrefcount

```python
# Возвращает значение счетчика ссылок на объект.
sys.getrefcount(True)
```




    5574



#### getsizeof
```python
# Возвращает размер объекта в байтах. 
# Вычисления выполняются с помощью специального метода __sizeof__() указанного объекта. 
# Если этот метод не определен, возбуждается исключение TypeError, 
# если не было указано значение по умолчанию в аргументе default. 
# Поскольку на реализацию методов __sizeof__() в объектах не накладывается никаких ограничений, 
# то нет никакой гарантии, что возвращаемое значение функции будет точно соответствовать объему занимаемой памяти. 
# Однако для встроенных типов, таких как списки или строки, функция возвращает корректное значение.
sys.getsizeof(sys.modules)
```




    36976



#### setrecursionlimit
```python
# Устанавливает ограничение на количество рекурсивных вызовов функций. 
# По умолчанию устанавливается значение 1000 (3000). 
# Обратите внимание, что операционная система может накладывать свои ограничения на размер стека, 
# поэтому установка слишком большого значения может вызывать аварийное завершение процесса интерпретатора Python 
# с сообщением «Segmentation Fault» (ошибка сегментации) или «Access Violation» (нарушение прав доступа).
 sys.setrecursionlimit(limit)
```

