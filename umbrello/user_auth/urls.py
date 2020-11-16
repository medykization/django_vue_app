from django.urls import path
from user_auth.views import(
    user_auth_login,
)

app_name="user_auth"

urlpatterns = [
    path('login', user_auth_login, name="user_auth_login"),
]