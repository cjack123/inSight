"""View module for handling requests about transactions"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from inSightapi.models import Transactions


class TransactionView(ViewSet):
    """Level up transactions view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single transaction

        Returns:
            Response -- JSON serialized transaction
        """
        transaction = Transactions.objects.get(pk=pk)
        serializer = TransactionSerializer(transaction)
        return Response(serializer.data)

    def list(self, request):
        """Handle GET requests to get all transactions

        Returns:
            Response -- JSON serialized list of transactions
        """
        transactions = Transactions.objects.all()
        serializer = TransactionSerializer(transactions, many=True)
        return Response(serializer.data)

class TransactionSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = Transactions
        fields = ('id', 'card', 'card_holder', 'transaction_type', 'store', 'amount', 'transaction_date')