`MIDDLEWARE`
==
middleware - это  функция(или класс), которая(ый) может обрабатывать запросы до обработки вью, и ответы - после.

В django есть 5 видов промежуточных слоёв и у каждого своё назначение:

- request middleware - обработка пользовательского запроса перед роутингом на определённое вью
- view middleware - `process_view()` обработка запроса после роутинга, но перед вызовом конкретного вью(когда известно какое вью будет вызвано)
- exception middleware - `process_exception_by_middleware()` - выполняется когда возникает исключение во вью или при рендеринге шаблона
- template response middleware - `process_template_response()` - выполняется когда вью возвращает шаблон
- response middleware - финальная обработка ответа с последующей передачей серверу приложений -> веб-серверу -> пользователю

Пример простого middleware, который к объекту запроса добавляет аттрибут `comments` со списком всех комментариев:

```
# название слоя
def middleware_1(get_response):

    def wrapper(request):
        # СТОРОНА ПЕРЕД ВЬЮ
        # здесь будет выполняться всё то
        # что относится к слою request middleware

        # создаём у объекта request аттрибут comments
        request.comments = Comment.objects.all()
 

        response = get_response(request)
        # СТОРОНА ПОСЛЕ ВЬЮ
        # здесь будет выполняться всё то
        # что относится к слою response middleware
        
        # возвращаем ответ
        return response
    # возвращаем слой
    return wrapper
```
или тоже самое с использованием класса:

```

class Middleware_1:
    # __init__ - конструктор, отвечающий за инициализацию экземпляра
    # get_response - аргумент, который можно вызвать как функцию
    # если это не последний слой - то get_response - это следующий слой, иначе это вью
    def __init__(self, get_response):
        self.get_response = get_response

    # __сall__ - метод, позволяющий вызывать наш экземпляр как функцию
    # self - ссылка на экземпляр, через которую методы могут осуществлять операции с аттрибутами экземпляра
    # request - объект класса WSGI-request, который передаётся от сервера приложения(своеобразный объект-агрегатор,  
    # в который все middlewares могут поместить необходимую нам информацию про сессию, аутентификацию и авторизацию пользователя.)
    def __call__(self, request):
        # СТОРОНА ПЕРЕД ВЬЮ
        request.comments = Comments.objects.all()
	
	response = self.get_response(request) # ответ от вью
	# СТОРОНА ПОСЛЕ ВЬЮ
        
	# возвращаем ответ
        return response

```

Так выгледят вызовы трёх middleware с одинаковым функционалом и одного вью(CENTER):
```
before | middleware_1 | request is <WSGIRequest: GET '/'>
before | middleware_2 | request is <WSGIRequest: GET '/'>
before | middleware_3 | request is <WSGIRequest: GET '/'>
CENTER, запрос получен, отправляем ответ
after | middleware_3 | response is <HttpResponse status_code=200, "text/html; charset=utf-8">
after | middleware_2 | response is <HttpResponse status_code=200, "text/html; charset=utf-8">
after | middleware_1 | response is <HttpResponse status_code=200, "text/html; charset=utf-8">

```


