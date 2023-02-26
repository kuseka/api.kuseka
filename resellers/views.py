from resellers.models import ResellerProfile
from .serializers import *
from .models import *
from users.models import User
from rest_framework import generics,status
from rest_framework.permissions import AllowAny,IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

# Create your views here.

class BecomeReseller(generics.CreateAPIView):
    serializer_class = ResellerProfileSerializer
    authentication_classes = (JWTAuthentication,)
    permission_classes = (AllowAny,)
    

    def create(self, request):
        serializer = self.get_serializer(data=request.data)        
        if serializer.is_valid():
            instance =serializer.save() 
            user = User.objects.get(id="f3a417d4-3ae2-43d7-9b2a-6b9c0b9d5dba")  
            if not user.reseller:
                user.reseller = instance
                user.save()      
                return Response({"message":"User is now a reseller"}, status=status.HTTP_200_OK)
            else:
                return Response({"message":"User is already a reseller"}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"message":"User failed to become a reseller"}, status=status.HTTP_400_BAD_REQUEST)
   
class JobsView(generics.ListCreateAPIView):
    serializer_class = JobSerializer
    authentication_classes = (JWTAuthentication,)
    permission_classes = (AllowAny,)
    queryset = Job.objects.all()

    def create(self, request):
        job = Job()
        serializer = self.get_serializer(data=request.data)        
        if serializer.is_valid():
            instance =serializer.save() 
            reseller = ResellerProfile.objects.get(id="2c13c544-b913-430f-98ae-b4016f898b37")  
            if not reseller.jobs:
                reseller.jobs = instance
                reseller.save()      
                return Response({"message":"You have successfully gotten the job. You can start the course"}, status=status.HTTP_200_OK)
            else:
                return Response({"message":"You can only take on one job for now"}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"message":"Couldn't get job"}, status=status.HTTP_400_BAD_REQUEST)