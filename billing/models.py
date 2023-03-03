from django.db import models
import uuid

# Create your models here.
class Plan(models.Model):
    id = models.UUIDField(primary_key = True,default = uuid.uuid4,editable = False)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    amount = models.DecimalField(decimal_places=2,max_digits=10)
    transaction_id =  models.UUIDField(default="")
    userid=  models.UUIDField(default="")
    transaction_date = models.DateTimeField()