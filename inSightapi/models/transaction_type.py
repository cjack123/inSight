from django.db import models

class TransactionType(models.Model):
    type = models.CharField(max_length=7)