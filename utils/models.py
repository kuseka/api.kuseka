from django.db import models
import uuid
# Create your models here.
class Address(models.Model):
    id = models.UUIDField(primary_key = True,default = uuid.uuid4,editable = False)
    street = models.CharField(max_length=255)
    building =models.CharField(max_length=255)
    city =models.CharField(max_length=255)
    country =models.CharField(max_length=255)

class Software(models.Model):
    id = models.UUIDField(primary_key = True,default = uuid.uuid4,editable = False)
    title = models.CharField(max_length=255)
    targets = models.TextField()
    links = models.TextField()
    sreenshots = models.TextField()
    license_type = models.TextField()
    software_type = models.TextField()

class TrainingResource(models.Model):
    id = models.UUIDField(primary_key = True,default = uuid.uuid4,editable = False)
    title = models.TextField(max_length=255)
    description = models.TextField()
    link = models.TextField()