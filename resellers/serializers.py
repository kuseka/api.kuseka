from rest_framework import serializers


from .models import *

class ResellerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResellerProfile
        fields= '__all__'
        
class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields= '__all__'
        
    