"""View module for handling requests about cards"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from inSightapi.models import Card


class CardView(ViewSet):
    """Level up cards view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single card

        Returns:
            Response -- JSON serialized card
        """
        card = Card.objects.get(pk=pk)
        serializer = CardSerializer(card)
        return Response(serializer.data)
        

    def list(self, request):
        """Handle GET requests to get all cards

        Returns:
            Response -- JSON serialized list of cards
        """
        cards = Card.objects.all()
        serializer = CardSerializer(cards, many=True)
        return Response(serializer.data)

class CardSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = Card
        fields = ('id', 'cardholder', 'card_number', 'card_type', 'expiration_date', 'security_code', 'start_balance', 'current_balance', 'QRcode')