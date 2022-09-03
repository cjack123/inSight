from django.db import models
from django.contrib.auth.models import User

class CardHolder(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=55)
    state = models.CharField(max_length=2)
    zip = models.PositiveSmallIntegerField()
    

