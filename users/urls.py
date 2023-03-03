from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path("register",RegisterView.as_view(),name="Register"),
    path("login",LoginView.as_view(),name="Login")
]
