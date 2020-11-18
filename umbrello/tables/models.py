from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Board(models.Model):
    id = models.IntegerField(primary_key = True) 
    name = models.CharField(max_length=30)
    owner_id = models.ForeignKey(User,  on_delete=models.CASCADE)
