from django.urls import path
from boards.views import BoardView, BoardAdd, BoardNameUpdate, ListView, ListAdd, CardAdd, CardView, ListNameUpdate


app_name = "boards"

urlpatterns = [
    path('', BoardView.as_view()),
    path('add', BoardAdd.as_view()),
    path('update', BoardNameUpdate.as_view()),
    path('lists', ListView.as_view()),
    path('add/list', ListAdd.as_view()),
    path('update/list', ListNameUpdate.as_view()),
    #path('archive/list', CardAdd.as_view()),
    path('cards', CardView.as_view()),
    path('add/card', CardAdd.as_view()),
    #path('archive/card', CardAdd.as_view()),
]