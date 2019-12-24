`restful api`
=

1. model
2. serializer
3. view
4. url


`serialization`
==

```
class CarDetailSerializer(ModelSerializer):
    class Meta:
        model = Car
        fields = "__all__"


class CarListSerializer(ModelSerializer):
    class Meta:
        model = Car
        fields = ("vin", "brand", "user")
```

`view`
==

- `generics.CreateAPIView` -  if we need to create entities
```
class CarCreateView(generics.CreateAPIView):
    serializer_class = CarDetailSerializer
```
- `generics.ListAPIView` - if we want to see all entities in db
```
class CarListView(generics.ListAPIView):
    serializer_class = CarListSerializer
    queryset = Car.objects.all()
```
- `generics.RetrieveUpdateDestroyAPIView` - if we need retrieve by one, update by one and delete by one entities
```
class CarDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CarDetailSerializer
    queryset = Car.objects.all()

    # we can override methods
    def get(self, request, *args, **kwargs):
        print("GET request called", request.query_params)
        return super().get(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        print("DELETE")
        return super().delete(request, *args, **kwargs)
```

`urls`
==

```
app_name = 'car'
urlpatterns = [
    path('car/create/', CarCreateView.as_view()),
    path('car/retrieve/', CarListView.as_view()),
    path('car/detail/<int:pk>/', CarDetailView.as_view()),

]

+ main url api/v1/cars/


```
