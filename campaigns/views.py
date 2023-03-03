from vendors.models import VendorProfile
from .serializers import *
from rest_framework import generics,status
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

# Create your views here.

class Campaign(generics.ListCreateAPIView):
    serializer_class = CampaignSerializer
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Campaign.objects.all()
    

    def create(self, request):
        user =request.user
        vendor_uuid =user.vendor_id
        serializer = self.get_serializer(data=request.data) 
        if not vendor_uuid:
            return Response({"message":"Only vendors can create campaigns, upgrade your account"}, status=status.HTTP_401_UNAUTHORIZED)
        if serializer.is_valid():            
            vendor = VendorProfile.objects.get(id=vendor_uuid)  
            if vendor.campaigns.count()<10:
                instance =serializer.save() 
                instance.is_draft = True
                instance.save()
                vendor.campaigns.add(instance)
                vendor.save()      
                return Response({"message":"Campaign successfully created"}, status=status.HTTP_201_CREATED)
            else:
                return Response({"message":"You have reached your limit"}, status=status.HTTP_401_UNAUTHORIZED)
        return Response({"errors":serializer.errors,"message":"There is missing data to add the campaign"}, status=status.HTTP_400_BAD_REQUEST)