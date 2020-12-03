from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authtoken.models import Token
from rest_framework import generics
from tables.serializers import BoardSerializer, ListSerializer, AddListSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import GenericAPIView
from tables.models import Board, List
from django.db.models import Max
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


class BoardsUpdate(GenericAPIView):
    permission_classes = (IsAuthenticated,)

    def put(self, request, *args, **kwargs):
        user = request.user
        body = request.data
        old_name = body['old_name']
        new_name = body['new_name']
        if old_name == new_name:
            return Response("You enter the same name")
        try:
            board = Board.objects.get(owner_id = user, name = old_name)
            board.name = new_name
            board.save()
            return Response("Board name updated")
        except Board.DoesNotExist:
            return Response("Board doesn't exist")
        

class ListView(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)

    def get_queryset(self, board_name):
        board = Board.objects.get(name = board_name)
        return List.objects.filter(board_id=board)  # return all model objects

    def get(self, request, *args, **kwargs):  # GET request handler for the model
        board = request.data
        board = board['board']
        queryset = self.get_queryset(board)
        serializer = ListSerializer(queryset, many=True)
        return Response(serializer.data)

class ListAdd(GenericAPIView):
    permission_classes = (IsAuthenticated,)

    def get_queryset(self, user, board_name):
        board = Board.objects.get(owner_id = user, name = board_name)
        user_list = List.objects.filter(board_id = board).order_by('order').last()
        return board, user_list.order + 1

    def post(self, request, *args):
        user = request.user
        body = request.data
        input = {"name": body['name']}
        board, order = self.get_queryset(user,body['board_name'])
        serializer = AddListSerializer(data=input, board=board, order = order)
        if serializer.is_valid(raise_exception=True):
            serializer.create(serializer.validated_data)
            return Response("List added",status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)