from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from user_auth.views import user_auth_register,LogoutView


app_name="user_auth"

urlpatterns = [
    path('login', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/logout', LogoutView.as_view(), name='auth_logout'),
    path('register', user_auth_register),
]