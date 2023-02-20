from django.db import models
import uuid

# Create your models here.

class Transactions(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    transaction_date = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(decimal_places=2,max_digits=10,default=True,blank=True)
    status = models.TextField(default=True,blank=False)