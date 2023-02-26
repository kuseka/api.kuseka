from django.db import models
import uuid
from billing.models import Plan
from campaigns.models import Campaign
from utils.models import Software

# Create your models here.

class VendorProfile(models.Model):
    id = models.UUIDField(primary_key = True,default = uuid.uuid4,editable = False)
    currency = models.TextField(max_length=10)    
    # settings = models.UUIDField(default = uuid.uuid4,editable = False)
    plan = models.ForeignKey(Plan,related_name="plan",on_delete=models.PROTECT,null=True)
    industry = models.TextField(null=True)
    average_budget = models.DecimalField(decimal_places=2,max_digits=10,null=True)
    description = models.TextField()
    vendor_email = models.CharField(max_length=255,null=False)
    vendor_phone_number =models.CharField(max_length=20,null=False)
    campaigns = models.ForeignKey(Campaign,related_name="campaigns",on_delete=models.PROTECT,null=True)
    softwares = models.ForeignKey(Software,related_name="vendor_softwares",on_delete=models.PROTECT,null=True)




