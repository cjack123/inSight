from django.db import models
from inSightapi.models.card_holder import Card_Holder

class Card(models.Model):
    card_holder = models.ForeignKey('card_holder', on_delete=models.CASCADE)
    card_number = models.PositiveSmallIntegerField()
    card_type = models.CharField(max_length=50)
    expiration_date = models.PositiveSmallIntegerField()
    security_code = models.PositiveSmallIntegerField()
    start_balance = models.DecimalField(max_digits=3, decimal_places=2)
    current_balance = models.DecimalField(max_digits=3, decimal_places=2)
    QRcode = models.CharField(max_length=500)