from django.db import models
from inSightapi.models.card_holder import CardHolder


class Card(models.Model):
    cardholder = models.ForeignKey(CardHolder, on_delete=models.CASCADE)
    card_number = models.PositiveBigIntegerField()
    card_type = models.CharField(max_length=50)
    expiration_date = models.DateField()
    security_code = models.PositiveBigIntegerField()
    start_balance = models.DecimalField(max_digits=5, decimal_places=2)
    current_balance = models.DecimalField(max_digits=5, decimal_places=2)
    QRcode = models.CharField(max_length=500)