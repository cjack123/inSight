"""View module for handling requests about transaction types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from inSightapi.models import TransactionType, transaction_type


class TransactionTypeView(ViewSet):
    """Level up transaction types view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single transaction type

        Returns:
            Response -- JSON serialized game type
        """
        # transaction_type = TransactionType.objects.get(pk=pk)
        # serializer = TransactionTypeSerializer(transaction_type)
        # return Response(serializer.data)
        try:
            transaction_type = TransactionType.objects.get(pk=pk)
            serializer = TransactionTypeSerializer(transaction_type)
            return Response(serializer.data)
        except TransactionType.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND) 
        

    def list(self, request):
        """Handle GET requests to get all transaction types

        Returns:
            Response -- JSON serialized list of transaction types
        """
        transaction_types = TransactionType.objects.all()
        serializer = TransactionTypeSerializer(transaction_types, many=True)
        return Response(serializer.data)

class TransactionTypeSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = TransactionType
        fields = ('id', 'type')


