from django.db import models
import uuid

# Create your models here.

class Transaction(models.Model):
    CURRENCY_CHOICES = [
        ("GHANA", 'GH₵'),
        ("NIGERIA", 'NGN'),
        ("KENYA", 'KSH')
    ]

    id = models.UUIDField(primary_key = True,default = uuid.uuid4,editable = False)
    transaction_date = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(decimal_places=2,max_digits=10,default=True,blank=True)
    currency = models.CharField(choices=CURRENCY_CHOICES,max_length=20,default="NIGERIA")
    status = models.TextField(default=True,blank=False)
    idempotency_token =  models.TextField(default="")
    note = models.TextField(default="")

    def __str__(self) -> str:
        return self.uuid