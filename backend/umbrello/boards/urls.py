from django.urls import path
from boards.views import BoardsView, BoardsAdd, BoardsUpdate, ListView, ListAdd, CardAdd


app_name = "boards"

urlpatterns = [
    path('', BoardsView.as_view()),
    path('add', BoardsAdd.as_view()),
    path('update', BoardsUpdate.as_view()),
    path('lists', ListView.as_view()),
    path('add/list', ListAdd.as_view()),
    path('add/card', CardAdd.as_view()),
]