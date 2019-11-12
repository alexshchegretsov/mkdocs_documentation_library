`CRUD with drf`
=

- pip install djangorestframework
- add to INSTALLED_APPS
- create new app and add it too, create urls.py, include it to main URL
- #MODELS. 
- start with models, create model and migrate them
```
class Quote(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    
    def __str__(self):
        return self.title
```
- #SERIALIZER. 
- create serializers.py, serializer translate TO and FROM json
```
from rest_framework import serializers
from .models import Quote

class QuotSerializer(serializers.ModelSerializer):
    class Meta:
        # указываем модель для сериализации
        model = Quote
        # выбираем поля для серилизации
        fields = ["id", "title", "description"]
```
- #VIEW. 
```
from rest_framework import viewsets
from .models import Quote
from .serializers import QuotSerializer

# ModelViewSet скрывает GET,POST,PUT,DELETE
class QuoteView(viewsets.ModelViewSet):
    # для работы с БД
    queryset = Quote.objects.all()
    # для трансляции
    serializer_class = QuotSerializer

```
- #URL.

```
from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
# роутер генерирует свои уже готовые урлы, котрые мы подключим с помощью path
router.register('quotes', views.QuoteView)

urlpatterns = [
    path('', include(router.urls)),
]

```
name in register is a name in url and json
```
HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "quotes": "http://127.0.0.1:8000/quotes/"
}
```
