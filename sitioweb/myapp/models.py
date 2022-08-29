from django.db import models

from django.contrib.auth.models import User

from django.utils import timezone

class familia(models.Model):
    name= models.CharField(max_length=128)
    fecha_nacimiento= models.DateField()
    edad= models.IntegerField()
    date_added = models.DateTimeField(auto_now_add= True)