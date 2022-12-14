"""View module for handling requests about stores"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from inSightapi.models import Store


class StoreView(ViewSet):
    """Level up stores view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single store

        Returns:
            Response -- JSON serialized store
        """

        # store = Store.objects.get(pk=pk)
        # serializer = StoreSerializer(store)
        # return Response(serializer.data)
        try:
            store = Store.objects.get(pk=pk)
            serializer = StoreSerializer(store)
            return Response(serializer.data)
        except Store.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND) 
        

    def list(self, request):
        """Handle GET requests to get all stores

        Returns:
            Response -- JSON serialized list of stores
        """
        store = Store.objects.all()
        serializer = StoreSerializer(store, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = CreateStoreSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        store = Store.objects.get(pk=pk)
        serializer = CreateStoreSerializer(store, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk):
        store = Store.objects.get(pk=pk)
        store.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)


class StoreSerializer(serializers.ModelSerializer):
    """JSON serializer for stores
    """
    class Meta:
        model = Store
        fields = ('id', 'name')

class CreateStoreSerializer(serializers.ModelSerializer):
    """JSON serializer for transactions
    """
    class Meta:
        model = Store
        fields = ('id', 'name')
