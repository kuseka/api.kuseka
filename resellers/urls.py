from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('join',BecomeReseller.as_view(),name="Reseller"),
    path('jobs',JobsView.as_view(),name="Jobs"),
]
