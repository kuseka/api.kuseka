from rest_framework import serializers


from .models import *

class TransactionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields= '__all__'
        