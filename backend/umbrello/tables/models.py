from django.db import models
from django.conf import settings
from django.contrib.auth.models import Group


class Board(models.Model):
    owner_id = models.ForeignKey(
        settings.AUTH_USER_MODEL, blank=False, null=False, on_delete=models.CASCADE)
    members_id = models.ForeignKey(
        Group, blank=True, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class List(models.Model):
    board_id = models.ForeignKey(Board,  on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    order = models.DecimalField(
        max_digits=30, decimal_places=15, blank=True, null=True)

    def __str__(self):
        return self.name


class Card(models.Model):
    list_id = models.ForeignKey(List,  on_delete=models.CASCADE)
    members_id = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=30)

    def __str__(self):
        return self.name
    