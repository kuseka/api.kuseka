from django.db import models
import uuid
from resellers.models import Job
from transactions.models import Transaction
from utils.models import Software,TrainingResource

# Create your models here.


class Campaign(models.Model):
    id = models.UUIDField(primary_key = True,default = uuid.uuid4,editable = False)
    name = models.CharField(max_length=255,null=False)
    description = models.TextField(default="")
    type_of_software = models.TextField(default="")
    license_type = models.TextField(default="")
    created_on = models.DateTimeField(auto_now_add=True)
    start_date = models.DateTimeField(null=True)
    end_date = models.DateTimeField(null=True)
    resellers_requested = models.IntegerField()
    resellers_experince = models.IntegerField()
    transaction = models.ForeignKey(Transaction,on_delete=models.PROTECT,related_name="transaction",null=True)
    resellers_average_rating= models.DecimalField(decimal_places=2,max_digits=10,null=True)
    softwares = models.ManyToManyField(Software,related_name="campaign_softwares",blank=True)
    training_resources = models.ManyToManyField(TrainingResource,related_name="training_resources",blank=True)
    amount = models.DecimalField(decimal_places=2,max_digits=10,null=True)
    industry = models.TextField()
    commissions = models.DecimalField(decimal_places=2,max_digits=10)
    is_draft = models.BooleanField(default=True)
    is_active = models.BooleanField(default=False)
    duration = models.DecimalField(decimal_places=2,max_digits=10,default=1)
    goal = models.TextField(default="")
    target_audience = models.TextField(default="")
    estimated_reach = models.DecimalField(decimal_places=2,max_digits=10)
    jobs = models.ManyToManyField(Job,related_name="campaign_jobs",blank=True)


