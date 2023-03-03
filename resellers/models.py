from django.db import models
import uuid
from utils.helpers import *
from utils.models import Software,TrainingResource



class Rating(models.Model):
    id = models.UUIDField(primary_key = True,default = uuid.uuid4,editable = False)
    value = models.DecimalField(decimal_places=2,max_digits=10)
class Renewal(models.Model):
    id = models.UUIDField(primary_key = True,default = uuid.uuid4,editable = False)
    amount_renewed = models.DecimalField(decimal_places=2,max_digits=10)
    commissions = models.DecimalField(decimal_places=2,max_digits=10)
    refferal_code = models.CharField(max_length=255)

class JobConversion(models.Model):
    id = models.UUIDField(primary_key = True,default = uuid.uuid4,editable = False)
    # refferal_code = models.CharField(max_length=255,unique=True,default=generate_hex_string(5))
    activation_date = models.DateTimeField()
    renewal_date = models.DateTimeField()
    last_subscription_date = models.DateTimeField()
    activation_location = models.TextField(null=True)
    renewals = models.ForeignKey(Renewal, related_name="renewals",on_delete=models.PROTECT,null=True)

class Job(models.Model):
    id = models.UUIDField(primary_key = True,default = uuid.uuid4,editable = False)
    training_resources = models.ForeignKey(TrainingResource,related_name="courses",on_delete=models.PROTECT,null=True,blank=True)
    training_completion = models.DecimalField(decimal_places=2,max_digits=10,default=0)
    softwares = models.ForeignKey(Software,related_name="softwares",on_delete=models.PROTECT,null=True,blank=True)
    refferal_code = models.CharField(max_length=255,unique=True,default=generate_hex_string(6))
    commissions = models.DecimalField(decimal_places=2,max_digits=10,null=True,default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    conversions = models.ForeignKey(JobConversion,related_name="conversions",on_delete=models.PROTECT,null=True,blank=True)

class ResellerProfile(models.Model):
    currency_choices = (
        ("NGN","Nigeria Naira"),
        ("GHS","Ghana Cedi"),
        ("KSH","Kenya Shilling"),
        ("UGX","Uganda Shilling"),
    )
    id = models.UUIDField(primary_key = True,default = uuid.uuid4,editable = False)
    currency = models.TextField(max_length=10,choices=currency_choices)
    ratings = models.ForeignKey(Rating,related_name="ratings",on_delete=models.PROTECT,null=True)
    experience_periods = models.DecimalField(decimal_places=2,max_digits=10)
    has_finished_basic_training = models.BooleanField(default=False)
    basic_training_completion = models.DecimalField(decimal_places=2,max_digits=10,default=0)
    bio = models.TextField(default="")
    is_available = models.BooleanField(default=False)
    off_days = models.IntegerField(default=0)
    jobs = models.ManyToManyField(Job,related_name="jobs",blank=True)
    push_notification_id = models.TextField(null=True)


    


