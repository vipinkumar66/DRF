# Single item data => Generic Views

from rest_framework import generics
from .models import Product
from . import serializers

class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductSerializer

    def perform_create(self, serializer):
        """
        This is one of the method which is only given to the createapiview
        and it takes two arguments: Instance and the serializer
        """
        title = serializer.validated_data.get("title")
        content = serializer.validated_data.get("content") or None
        if content is None:
            content = title
        serializer.save(content=content)

class ProductRetrieveView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductSerializer
    # lookup_field = "pk"
