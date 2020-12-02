from django.urls import path
from tables.views import BoardsView  # , boards_all


app_name = "tables"

urlpatterns = [
    path('all', BoardsView.as_view()),
    #path('add', boards_create),
]
