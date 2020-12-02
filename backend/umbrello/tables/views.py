from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authtoken.models import Token
from rest_framework import generics
from tables.serializers import BoardSerializer
from rest_framework.permissions import IsAuthenticated
from tables.models import Board
import json

"""
@api_view(['POST'])
def board_create(request):
    user = request.user
    body = request.data
    input = {"name": body['name']}
    serializer = BoardSerializer(data = input, user = user)
    if serializer.is_valid(raise_exception=True):
        serializer.create(serializer.validated_data)
        return Response(status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
"""


class BoardsView(generics.RetrieveAPIView):
    # checks if user is authenticated to view the model objects
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Board.objects.all()  # return all model objects

    def get(self, request, *args, **kwargs):  # GET request handler for the model
        queryset = self.get_queryset()
        serializer = BoardSerializer(queryset, many=True)
        return Response(serializer.data)


'''
@api_view(['GET'])
def boards_all(request):
    data = json.loads(request.body)
    serializer = UserSerializer(data=data['body'])
    if serializer.is_valid(raise_exception=True):
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
'''
