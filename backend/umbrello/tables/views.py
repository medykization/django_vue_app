from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authtoken.models import Token
from rest_framework import generics
from tables.serializers import BoardSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import GenericAPIView
from tables.models import Board
import json


class BoardsView(generics.RetrieveAPIView):
    # checks if user is authenticated to view the model objects
    permission_classes = (IsAuthenticated,)

    def get_queryset(self, user):
        return Board.objects.filter(owner_id=user)  # return all model objects

    def get(self, request, *args, **kwargs):  # GET request handler for the model
        user = request.user
        queryset = self.get_queryset(user)
        serializer = BoardSerializer(queryset, user=user, many=True)
        return Response(serializer.data)


class BoardsAdd(GenericAPIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args):
        user = request.user
        body = request.data
        input = {"name": body['name']}
        serializer = BoardSerializer(data=input, user=user)
        if serializer.is_valid(raise_exception=True):
            serializer.create(serializer.validated_data)
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
