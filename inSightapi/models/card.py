from django.db import models

class Card(models.Model):
    card_user = models.ForeignKey('card_user', on_delete=models.CASCADE)
    card_number = models.PositiveSmallIntegerField(max_length=16)
    card_type = models.CharField(max_length=50)
    expiration_date = models.PositiveSmallIntegerField(max_length=4)
    security_code = models.PositiveSmallIntegerField(max_length=3)
    start_balance = models.DecimalField(max_digits=3, decimal_places=2)
    current_balance = models.DecimalField(max_digits=3, decimal_places=2)
    QRcode = models.CharField(max_length=500)