from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('join',BecomeVendor.as_view(),name="Reseller"),
]
