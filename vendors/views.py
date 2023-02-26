from users.models import User
from .serializers import *
from rest_framework import generics,status
from rest_framework.permissions import AllowAny,IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
# Create your views here.

class BecomeVendor(generics.CreateAPIView):
    serializer_class = VendorProfileSerializer
    authentication_classes = (JWTAuthentication,)
    permission_classes = (AllowAny,)

    def create(self, request):
        serializer = self.get_serializer(data=request.data)        
        if serializer.is_valid():
            instance =serializer.save() 
            user = User.objects.get(id="f3a417d4-3ae2-43d7-9b2a-6b9c0b9d5dba")  
            if not user.vendor:
                user.vendor = instance
                user.save()      
                return Response({"message":"User is now a vendor"}, status=status.HTTP_200_OK)
            else:
                return Response({"message":"User is already a vendor"}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"message":"User failed to become a vendor"}, status=status.HTTP_400_BAD_REQUEST)
