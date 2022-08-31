from django.db import models

class Transaction_Type(models.Model):
    type = models.CharField(max_length=7)