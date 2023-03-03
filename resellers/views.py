from django.shortcuts import get_object_or_404
from resellers.models import ResellerProfile
from campaigns.models import *
from .serializers import *
from .models import *
from users.models import User
from rest_framework import generics,status,viewsets
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from utils.helpers import *
from django.core.exceptions import ValidationError
# Create your views here.

class BecomeReseller(generics.CreateAPIView):
    serializer_class = ResellerProfileSerializer
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)
    

    def create(self, request):
        user =request.user
        serializer = self.get_serializer(data=request.data)        
        if serializer.is_valid():            
            if not user.reseller:
                instance =serializer.save() 
                user.reseller = instance
                user.save()      
                return Response({"message":"User is now a reseller"}, status=status.HTTP_200_OK)
            else:
                return Response({"message":"User is already a reseller"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"errors":serializer.errors,"message":"User failed to become a reseller"}, status=status.HTTP_400_BAD_REQUEST)
   
class JobsView(generics.ListCreateAPIView):
    """
        This view return or create jobs for a specific reseller
    """
    serializer_class = JobSerializer
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Job.objects.all()

    def get(self, request, *args, **kwargs):
        job_id = self.kwargs.get('id')
        if job_id:
            job = get_object_or_404(self.queryset, id=job_id)
            serializer = self.get_serializer(job)
            return Response(serializer.data)
        else:
            return super().get(request, *args, **kwargs)

    def create(self, request):
        user =request.user
        reseller_uuid =user.reseller_id
        data = request.data.copy()
        if not request.data:
            return Response({"message":"The campaign id is missing"}, status=status.HTTP_400_BAD_REQUEST)
        campaign_uuid = data.pop('campaign_uuid')
        if campaign_uuid == None or not campaign_uuid:
            return Response({"message":"Please select the campaign you want to join"}, status=status.HTTP_400_BAD_REQUEST)
        if not reseller_uuid:
            return Response({"message":"Only resellers can take on jobs, upgrade your account"}, status=status.HTTP_401_UNAUTHORIZED)
        serializer = self.get_serializer(data=request.data) 
        if serializer.is_valid():         
            reseller = ResellerProfile.objects.get(id=reseller_uuid)  
            campaign = Campaign.objects.get(id=campaign_uuid)  
            if not reseller and not campaign:
                return Response({"message":"The campaign you want to work for no longer exists"}, status=status.HTTP_400_BAD_REQUEST)
            if reseller.jobs.count()<5:
                instance=serializer.save()
                reseller.jobs.add(instance)
                campaign.jobs.add(instance)
                reseller.save()
                campaign.save()
            else:
                return Response({"message":"You have reached your limit"}, status=status.HTTP_401_UNAUTHORIZED)
            return Response({"message":"You have successfully gotten the job. You can start the course","job_id":instance.id}, status=status.HTTP_200_OK)
        return Response({"errors":serializer.errors,"message":"Failed to get the job"}, status=status.HTTP_400_BAD_REQUEST)
        
