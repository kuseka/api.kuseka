from .serializers import *
from rest_framework import generics,status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
# Create your views here.

class TransactionsView(generics.ListAPIView):
    serializer_class = TransactionsSerializer

    def get_queryset(self):
        # You can add some filtering, ordering or pagination here if needed
        return Transaction.objects.all()
    
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        transaction = serializer.save()
        return Response(self.get_serializer(transaction).data, status=status.HTTP_201_CREATED)
    
class TransactionView(generics.RetrieveAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionsSerializer
    lookup_field = 'id' # or the field you want to use as the lookup parameter

    def retrieve(self, request, *args, **kwargs):
        transaction_id = kwargs['id'] # get the value of the id parameter from the URL
        queryset = self.get_queryset()
        transaction = queryset.filter(id=transaction_id).first() # filter the queryset by the id parameter
        serializer = self.get_serializer(transaction)
        return Response(serializer.data, status=status.HTTP_200_OK)