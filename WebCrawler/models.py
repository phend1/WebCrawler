from django.db import models

# Create your models here.

class Bank(models.Model):
    bank_name = models.TextField()
    bank_short_name = models.CharField(max_length=3)

    class Meta:
        db_table = "Bank"

class Currency(models.Model):
    date = models.DateField()
    bank_short_name = models.CharField(max_length=3, default='')
    currency = models.CharField(max_length=3, default='')
    buy = models.DecimalField(max_digits=8, decimal_places=5)
    sell = models.DecimalField(max_digits=8, decimal_places=5)

    class Meta:
        db_table = "Currency"

