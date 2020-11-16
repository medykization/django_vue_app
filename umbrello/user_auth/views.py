from django.shortcuts import render

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.contrib.auth.models import User
from user_auth.serializers import UserSerializer

# Create your views here.
@api_view(['POST'])
def user_auth_login(request):
    serializer = UserSerializer(data = request.data)
    if serializer.is_valid(raise_exception=True):
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)