from vendors.models import VendorProfile
from .serializers import *
from rest_framework import generics,status
from rest_framework.permissions import AllowAny,IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

# Create your views here.

class Campaign(generics.ListCreateAPIView):
    serializer_class = CampaignSerializer
    authentication_classes = (JWTAuthentication,)
    permission_classes = (AllowAny,)
    queryset = Campaign.objects.all()
    

    def create(self, request):
        serializer = self.get_serializer(data=request.data) 
        if serializer.is_valid():
            instance =serializer.save() 
            vendor = VendorProfile.objects.get(id="c7e9ca0e-3f7d-4ea3-946a-0bd1fa8409e6")  
            if not vendor.campaigns:
                vendor.campaigns = instance
                vendor.save()      
                return Response({"message":"Campaign successfully created"}, status=status.HTTP_201_CREATED)
            else:
                return Response({"message":"You can't create more than one campaign"}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"message":"There is missing data to add the campaign"}, status=status.HTTP_400_BAD_REQUEST)