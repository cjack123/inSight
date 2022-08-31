from django.db import models
from inSightapi.models.store import Store

class Transactions(models.Model):
    card = models.ForeignKey('card', on_delete=models.CASCADE)
    card_user = models.ForeignKey('card_user', on_delete=models.CASCADE)
    transaction_type = models.ForeignKey('transaction_type', on_delete=models.CASCADE)
    store = models.ManyToManyField(Store)
    amount = models.DecimalField(max_digits=3, decimal_places=2)
    transaction_date = models.DateTimeField()

