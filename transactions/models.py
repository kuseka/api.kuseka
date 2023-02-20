from django.db import models

# Create your models here.

class Transactions(models.Model):
    uuid = models.UUIDField()
    transaction_date = models.DateField(auto_now_add=True)