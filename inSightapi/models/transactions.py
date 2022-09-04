from django.db import models
from inSightapi.models.card_holder import CardHolder
from inSightapi.models.card import Card
from inSightapi.models.transaction_type import TransactionType
from inSightapi.models.store import Store

class Transactions(models.Model):
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    card_holder = models.ForeignKey(CardHolder, on_delete=models.CASCADE)
    transaction_type = models.ForeignKey(TransactionType, on_delete=models.CASCADE)
    store = models.ManyToManyField(Store)
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    transaction_date = models.DateTimeField()


