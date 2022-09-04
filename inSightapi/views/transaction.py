"""View module for handling requests about transactions"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from inSightapi.models import Transactions
from inSightapi.models import Card
from inSightapi.models import TransactionType
from inSightapi.models import CardHolder
from inSightapi.models import Store


class TransactionView(ViewSet):
    """Level up transactions view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single transaction

        Returns:
            Response -- JSON serialized transaction
        """
        # transaction = Transactions.objects.get(pk=pk)
        # serializer = TransactionSerializer(transaction)
        # return Response(serializer.data)
        try:
            transactions = Transactions.objects.get(pk=pk)
            serializer = TransactionSerializer(transactions)
            return Response(serializer.data)
        except Transactions.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND) 

    def list(self, request):
        """Handle GET requests to get all transactions

        Returns:
            Response -- JSON serialized list of transactions
        """
        # transactions = Transactions.objects.all()
        # serializer = TransactionSerializer(transactions, many=True)
        # return Response(serializer.data)
    
        transactions = Transactions.objects.all()

        # Add in the next 3 lines
        card = request.query_params.get('card', None)
        if card is not None:
            transactions = transactions.filter(card_id=card)

        serializer = TransactionSerializer(transactions, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized transaction instance
        """
        card_holder = CardHolder.objects.get(user=request.auth.user)
        transaction_type = TransactionType.objects.get(pk=request.data["transaction_type"])
        card = Card.objects.get(pk=request.data["card"])
        store = Store.objects.get(pk=request.data["store"])

        transaction = Transactions.objects.create(
            card=card,
            card_holder=card_holder,
            transaction_type=transaction_type,
            store=store,
            amount=request.data["amount"],
            transaction_date=request.data["transaction_date"]
        )
        serializer = TransactionSerializer(transaction)
        return Response(serializer.data)

    

class TransactionSerializer(serializers.ModelSerializer):
    """JSON serializer for transactions
    """
    class Meta:
        model = Transactions
        fields = ('id', 'card', 'card_holder', 'transaction_type', 'store', 'amount', 'transaction_date')
        depth = 2