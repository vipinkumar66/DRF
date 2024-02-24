# Single item data => Generic Views

from rest_framework import generics
from .models import Product
from . import serializers

class ProductRetrieveView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductSerializer
    # lookup_field = "pk"
