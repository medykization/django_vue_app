from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authtoken.models import Token
from rest_framework import generics
from boards.serializers import BoardSerializer, ListSerializer, AddListSerializer, AddCardSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import GenericAPIView
from boards.models import Board, List, Card
from django.db.models import Max
from django.contrib.auth.models import User
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

    def get_queryset(self, id):
        board = Board.objects.get(id = id)
        return List.objects.filter(board_id=board)  # return all model objects

    def post(self, request, *args, **kwargs):  # GET request handler for the model
        board = request.data
        id = board['board_id']
        queryset = self.get_queryset(id)
        serializer = ListSerializer(queryset, many=True)
        return Response(serializer.data)

class ListAdd(GenericAPIView):
    permission_classes = (IsAuthenticated,)

    def get_queryset(self, user, board_id):
        board = Board.objects.get(owner_id = user, id = board_id)
        last_list = List.objects.filter(board_id = board).order_by('order').last()
        if last_list is None:
            return board, 1
        return board, user_list.order + 1

    def post(self, request, *args):
        user = request.user
        body = request.data
        input = {"name": body['name']}
        try:
            board, order = self.get_queryset(user,body['board_id'])
        except Board.DoesNotExist:
            return Response("Board doesn't exist")
        serializer = AddListSerializer(data=input, board=board, order = order)
        if serializer.is_valid(raise_exception=True):
            serializer.create(serializer.validated_data)
            return Response("List added",status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CardAdd(GenericAPIView):
    permission_classes = (IsAuthenticated,)

    def get_queryset(self, user, list_id):
        li = List.objects.get(id = list_id)
        last_card = Card.objects.filter(list_id = li).order_by('order').last()
        if last_card is None:
            return li, 1
        return li, last_card.order + 1

    def post(self, request, *args):
        user = request.user
        body = request.data
        input = {"name": body['name'], "description": body['description']}
        try:
            li, order = self.get_queryset(user,body['list_id'])
        except List.DoesNotExist:
            return Response("List doesn't exist")
        serializer = AddCardSerializer(data=input, list=li, order = order)
        if serializer.is_valid(raise_exception=True):
            serializer.create(serializer.validated_data)
            return Response("Card added",status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)