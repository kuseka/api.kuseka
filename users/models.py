from django.db import models
import uuid
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from resellers.models import ResellerProfile

from utils.models import Address
from vendors.models import VendorProfile

class UserManager(BaseUserManager):
    def create_user(self, firstname,lastname, email,phone_number, username,password=None, **extra_fields):
        if not email:
            raise ValueError('Email address is required')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)
# Create your models here.
class User(AbstractBaseUser):
    id = models.UUIDField(primary_key = True,default = uuid.uuid4,editable = False)
    email = models.EmailField(unique=True,verbose_name="Email address")
    phone_number =models.CharField(max_length=20,verbose_name="Phone number")
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)    
    is_active = models.BooleanField(default=True)
    username = models.CharField(max_length=255,unique=True,null=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    address = models.ForeignKey(Address,related_name="address",on_delete=models.PROTECT,null=True)
    reseller = models.ForeignKey(ResellerProfile,related_name="reseller",on_delete=models.PROTECT,null=True)
    vendor = models.ForeignKey(VendorProfile,related_name="vendor",on_delete=models.PROTECT,null=True)


    USERNAME_FIELD = 'username'
    objects = UserManager()


    def __str__(self):
        return self.username
    

