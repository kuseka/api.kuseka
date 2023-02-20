from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('', TransactionsView.as_view(),name="Trasactions"),
    path('<int:id>/', TransactionView.as_view(),name="Trasaction"),
]
