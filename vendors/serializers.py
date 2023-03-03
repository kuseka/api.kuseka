from rest_framework import serializers


from .models import *

class VendorProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendorProfile
        fields= '__all__'
        
    