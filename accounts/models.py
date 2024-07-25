from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from decimal import Decimal

class Holding(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    currency = models.CharField(max_length=3, choices=[('BTC', 'Bitcoin'), ('ETH', 'Ethereum')])
    amount = models.DecimalField(max_digits=20, decimal_places=6, default=0.00)
    value = models.FloatField(default=0.00)

    def __str__(self):
        return f'{self.user.username} - {self.currency}: {self.amount}'
