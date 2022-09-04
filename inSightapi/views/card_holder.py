"""View module for handling requests about card holders"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from inSightapi.models import CardHolder


class CardHolderView(ViewSet):
    """Level up card holders view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single card holder

        Returns:
            Response -- JSON serialized card holder
        """
        # card_holder = CardHolder.objects.get(pk=pk)
        # serializer = CardHolderSerializer(card_holder)
        # return Response(serializer.data)

        try:
            card_holder = CardHolder.objects.get(pk=pk)
            serializer = CardHolderSerializer(card_holder)
            return Response(serializer.data)
        except CardHolder.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND) 

    def list(self, request):
        """Handle GET requests to get all card holders

        Returns:
            Response -- JSON serialized list of card holders
        """
        card_holders = CardHolder.objects.all()
        serializer = CardHolderSerializer(card_holders, many=True)
        return Response(serializer.data)


class CardHolderSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = CardHolder
        fields = ('user', 'city', 'state', 'zip')