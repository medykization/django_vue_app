from django.urls import path
from tables.views import BoardsView, BoardsAdd, BoardsUpdate, ListView, ListAdd


app_name = "tables"

urlpatterns = [
    path('all', BoardsView.as_view()),
    path('add', BoardsAdd.as_view()),
    path('update', BoardsUpdate.as_view()),
    path('show_lists', ListView.as_view()),
    path('add_list', ListAdd.as_view()),
]