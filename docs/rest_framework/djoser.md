`djoser`
==


- add `rest_framework.authtoken` and `djoser` to `INSTALLED_APPS`
- configure `urls.py`
```
urlpatterns = [
    (...),

    path(r'auth/', include('djoser.urls')),
    path(r'auth/', include('djoser.urls.authtoken')),
]
```
- add `rest_framework.authentication.TokenAuthentication`
```
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        (...)
    ),
}
```
- Run migrations - this step will create tables for auth and authtoken apps:
`./manage.py migrate`

- API endpoints:
```
auth/ ^users/$ [name='user-list']
auth/ ^users\.(?P<format>[a-z0-9]+)/?$ [name='user-list']
auth/ ^users/activation/$ [name='user-activation']
auth/ ^users/activation\.(?P<format>[a-z0-9]+)/?$ [name='user-activation']
auth/ ^users/me/$ [name='user-me']
auth/ ^users/me\.(?P<format>[a-z0-9]+)/?$ [name='user-me']
auth/ ^users/resend_activation/$ [name='user-resend-activation']
auth/ ^users/resend_activation\.(?P<format>[a-z0-9]+)/?$ [name='user-resend-activation']
auth/ ^users/reset_password/$ [name='user-reset-password']
auth/ ^users/reset_password\.(?P<format>[a-z0-9]+)/?$ [name='user-reset-password']
auth/ ^users/reset_password_confirm/$ [name='user-reset-password-confirm']
auth/ ^users/reset_password_confirm\.(?P<format>[a-z0-9]+)/?$ [name='user-reset-password-confirm']
auth/ ^users/reset_username/$ [name='user-reset-username']
auth/ ^users/reset_username\.(?P<format>[a-z0-9]+)/?$ [name='user-reset-username']
auth/ ^users/reset_username_confirm/$ [name='user-reset-username-confirm']
auth/ ^users/reset_username_confirm\.(?P<format>[a-z0-9]+)/?$ [name='user-reset-username-confirm']
auth/ ^users/set_password/$ [name='user-set-password']
auth/ ^users/set_password\.(?P<format>[a-z0-9]+)/?$ [name='user-set-password']
auth/ ^users/set_username/$ [name='user-set-username']
auth/ ^users/set_username\.(?P<format>[a-z0-9]+)/?$ [name='user-set-username']
auth/ ^users/(?P<pk>[^/.]+)/$ [name='user-detail']
auth/ ^users/(?P<pk>[^/.]+)\.(?P<format>[a-z0-9]+)/?$ [name='user-detail']
auth/ ^$ [name='api-root']
auth/ ^\.(?P<format>[a-z0-9]+)/?$ [name='api-root']
auth/ ^token/login/?$ [name='login']
auth/ ^token/logout/?$ [name='logout'] 
```
- create user(not admin):
`curl -X POST -d "username=foo&password=dexter1943" http://localhost:8000/auth/users/`
- login create token: `curl -X POST -d "username=foo&password=dexter1943" http://localhost:8000/auth/token/login/`
`{"auth_token":"c989581005c4b0e3032ec8c513eaea8460d05ecd"}`
- create: `curl -X POST -d "brand=gm&color=black" http://localhost:8000/api/v1/cars/create/ -H "Authorization: Token c989581005c4b0e3032ec8c513eaea8460d05ecd"`
- retrieve all: `curl -X GET http://localhost:8000/api/v1/cars/retrieve/ -H "Authorization: Token c989581005c4b0e3032ec8c513eaea8460d05ecd"` 
- retrive one: `curl -X GET http://localhost:8000/api/v1/cars/car/2/ -H "Authorization: Token c989581005c4b0e3032ec8c513eaea8460d05ecd"`
- update with PUT: `curl -X PUT -d "brand=bmw&color=black" http://localhost:8000/api/v1/cars/car/2/ -H "Authorization: Token c989581005c4b0e3032ec8c513eaea8460d05ecd"`
- update with PATCH: `curl -X PATCH -d "brand=fiat" http://localhost:8000/api/v1/cars/car/2/ -H "Authorization: Token c989581005c4b0e3032ec8c513eaea8460d05ecd"`
- delete: `curl -X DELETE http://localhost:8000/api/v1/cars/car/2/ -H "Authorization: Token c989581005c4b0e3032ec8c513eaea8460d05ecd"`
- logout destroy token: `curl -X POST http://localhost:8000/auth/token/logout/ -H "Authorization: Token c989581005c4b0e3032ec8c513eaea8460d05ecd"`

`hide user field`
=

```
class CarDetailSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Car
        fields = "__all__"
```

`permissions`
=

```
# IsAdminUser - check if request.user is Admin
# IsAuthenticated - check if request.user is authenticated in app by token comparison
# IsOwnerOrReadOnly - user can changes only entities that created and read foreign entities

# custom IsOwnerOrReadOnly permission

from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user

```
