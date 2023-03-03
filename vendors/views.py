from users.models import User
from .serializers import *
from rest_framework import generics,status
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
# Create your views here.

class BecomeVendor(generics.CreateAPIView):
    serializer_class = VendorProfileSerializer
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)

    def create(self, request):
        user =request.user
        serializer = self.get_serializer(data=request.data)            
        if serializer.is_valid():
            if not user.vendor:
                instance =serializer.save() 
                user.vendor = instance
                user.save()      
                return Response({"message":"User is now a vendor"}, status=status.HTTP_200_OK)
            else:
                return Response({"message":"User is already a vendor"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"errors":serializer.errors,"message":"User failed to become a vendor"}, status=status.HTTP_400_BAD_REQUEST)
