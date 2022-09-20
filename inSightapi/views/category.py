from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from inSightapi.models import Category

class CategoryView(ViewSet):
    """inSight Categories view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single Category

        Returns:
            Response -- JSON serialized Category
        """
        try:
            category = Category.objects.get(pk=pk)
            serializer = CategorySerializer(category)
            return Response(serializer.data)
        except Category.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND) 


    def list(self, request):
        """Handle GET requests to get all Categorys

        Returns:
            Response -- JSON serialized list of Categorys
        """
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data)


class CategorySerializer(serializers.ModelSerializer):
    """JSON serializer for Categorys
    """
    class Meta:
        model = Category
        fields = ('id', 'label')

class CreateCategorySerializer(serializers.ModelSerializer):
    """JSON serializer for transactions
    """
    class Meta:
        model = Category
        fields = ('id', 'label')