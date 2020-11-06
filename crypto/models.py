from django.db import models

# Create your models here.

class Crypto(models.Model):
  name = models.CharField(max_length=150)
  symbol = models.CharField(max_length=5)
  price = models.DecimalField(max_digits=19, decimal_places=10)
  market_cap = models.DecimalField(max_digits=19, decimal_places=2)
