from django.urls import path
from tables.views import (
    board_create,
    #boards_all,
)

app_name="tables"

urlpatterns = [
    path('add', board_create),
    #path('all', boards_all),
]