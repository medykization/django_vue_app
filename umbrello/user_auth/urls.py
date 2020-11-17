from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from user_auth.views import(
    user_auth_register,
)

app_name="user_auth"

urlpatterns = [
    path('login', obtain_auth_token, name="login"),
    path('register', user_auth_register, name="user_auth_register"),
]