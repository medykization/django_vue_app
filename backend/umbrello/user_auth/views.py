from django.shortcuts import render

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authtoken.views import ObtainAuthToken 
from rest_framework.authtoken.models import Token

from django.contrib.auth.models import User
from user_auth.serializers import UserSerializer
import json

# Create your views here.
@api_view(['POST'])
def user_auth_register(request):
    data = json.loads(request.body)
    serializer = UserSerializer(data = data['body'])
    if serializer.is_valid(raise_exception=True):
        serializer.create(serializer.validated_data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class user_auth_login(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        serializer = self.get_serializer(data=data['body'])
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})