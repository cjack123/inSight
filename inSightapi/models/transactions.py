from django.db import models
from inSightapi.models.store import Store
from inSightapi.models.card import Card

class Transactions(models.Model):
    card = models.ForeignKey('card', on_delete=models.PROTECT)
    card_holder = models.ForeignKey('card_holder', on_delete=models.PROTECT)
    transaction_type = models.ForeignKey('transaction_type', on_delete=models.PROTECT)
    store = models.ManyToManyField(Store)
    amount = models.DecimalField(max_digits=3, decimal_places=2)
    transaction_date = models.DateTimeField()


