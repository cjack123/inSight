"""View module for handling requests about cards"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from inSightapi.models import Card
from inSightapi.models import CardHolder


class CardView(ViewSet):
    """Level up cards view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single card

        Returns:
            Response -- JSON serialized card
        """
        # card = Card.objects.get(pk=pk)
        # serializer = CardSerializer(card)
        # return Response(serializer.data)
        
        try:
            card = Card.objects.get(pk=pk)
            serializer = CardSerializer(card)
            return Response(serializer.data)
        except Card.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle GET requests to get all cards

        Returns:
            Response -- JSON serialized list of cards
        """
        cards = Card.objects.all()
        serializer = CardSerializer(cards, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized card instance
        """
        cardholder = CardHolder.objects.get(user=request.auth.user)

        # card = Card.objects.create(
        #     cardholder=cardholder,
        #     card_number=request.data["card_number"],
        #     card_type=request.data["card_type"],
        #     expiration_date=request.data["expiration_date"],
        #     security_code=request.data["security_code"],
        #     start_balance=request.data["start_balance"],
        #     current_balance=request.data["current_balance"],
        #     QRcode=request.data["QRcode"],
        # )
        # serializer = CardSerializer(card)
        # return Response(serializer.data)

        serializer = CreateCardSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(cardholder=cardholder)
        
        cardId = serializer.data['id']
        card= Card.objects.get(pk=cardId )
        categories =  request.data['category']
        card.category.add(*categories)




        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        card = Card.objects.get(pk=pk)
        serializer = CreateCardSerializer(card, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        card = Card.objects.get(pk=pk)
        card.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
        

class CardSerializer(serializers.ModelSerializer):
    """JSON serializer for card holders
    """
    class Meta:
        model = Card
        fields = ('id', 'cardholder', 'card_number', 'card_type', 'expiration_date', 'security_code', 'start_balance', 'current_balance', 'category')
        depth = 1

class CreateCardSerializer(serializers.ModelSerializer):
    """JSON serializer for card holders
    """
    class Meta:
        model = Card
        fields = ('id', 'card_number', 'card_type', 'expiration_date', 'security_code', 'start_balance', 'current_balance', 'category')
