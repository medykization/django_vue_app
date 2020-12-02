from django.urls import path
from tables.views import BoardsView, BoardsAdd, BoardsUpdate


app_name = "tables"

urlpatterns = [
    path('all', BoardsView.as_view()),
    path('add', BoardsAdd.as_view()),
    path('update', BoardsUpdate.as_view()),
]
