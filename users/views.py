from .serializers import *
from .models import User
from rest_framework import generics,status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.contrib.auth import authenticate, login

from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from drf_yasg.utils import swagger_auto_schema
# Create your views here.

class RegisterView(generics.CreateAPIView):
    serializer_class  = UserSerializer
    authentication_classes = []
    permission_classes = (AllowAny,)
    
class LoginView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer
    authentication_classes = (JWTAuthentication,)

    @swagger_auto_schema(
            operation_description="This endpoint logins a user and returns a token for authentiation"
        )
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        # password = make_password(password)
        try:
            user = User.objects.get(username=username)
            is_user =user.check_password(password)
            if is_user:
                login(request, user)
                refresh = RefreshToken.for_user(user)
                return Response({"message":"Login successful","refresh": str(refresh), "access": str(refresh.access_token)}, status=status.HTTP_200_OK)
            else:
                return Response({"message":"Wrong username and password combination. Try again"}, status=status.HTTP_401_UNAUTHORIZED)
        except User.DoesNotExist:
            return Response({"message":"Wrong username and password combination. Try again"}, status=status.HTTP_401_UNAUTHORIZED)
    