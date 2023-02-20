from django.shortcuts import render,HttpResponse
from django.views import View
from .models import *
# Create your views here.

class TransactionsView(View):
    def get(self,request):
        transactions = Transactions.objects.all()
        return HttpResponse("Hello")