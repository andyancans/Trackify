from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Holding
from decimal import Decimal

@receiver(post_save, sender=User)
def create_default_holdings(sender, instance, created, **kwargs):
    if created:
        Holding.objects.create(user=instance, currency='BTC', amount=Decimal('0.00'))
        Holding.objects.create(user=instance, currency='ETH', amount=Decimal('0.00'))