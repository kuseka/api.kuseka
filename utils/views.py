from rest_framework import generics,status
from django.conf import settings
import boto3
import botocore.exceptions
from .serializers import *
from rest_framework.response import Response
from rest_framework.permissions import AllowAny,IsAuthenticated
from drf_yasg.utils import swagger_auto_schema

class ImageUploadView(generics.CreateAPIView):
    serializer_class = ImageSerializer
    permission_classes = (IsAuthenticated,)

    @swagger_auto_schema(
                operation_description="This endpoint is to upload images for the platform"
            )
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Upload image to S3
        image = serializer.validated_data['image']
        location = serializer.validated_data['location'] 
        s3 = boto3.client('s3', aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
                          aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
                          region_name=settings.AWS_S3_REGION_NAME)
        
        key = f'images/{image.name}' if location is None else  f'images/{location}/{image.name}'
        try:
            s3.upload_fileobj(image, settings.AWS_STORAGE_BUCKET_NAME, key)
        except botocore.exceptions.ClientError as e:
            # Handle any errors that occur during the upload process
            error_message = f"Error uploading image to S3: {e}"
            return Response({"error": error_message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


        # Return URL of uploaded image
        url = f'https://{settings.AWS_S3_CUSTOM_DOMAIN}/{key}'
        return Response({'url': url})
