from django.db import models
from django.contrib.auth.models import User

class Card_Holder(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT),
    city = models.CharField(max_length=55)
    state = models.CharField(max_length=2)
    zip = models.PositiveSmallIntegerField()
    

