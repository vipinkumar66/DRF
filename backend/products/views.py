# Single item data => Generic Views

from rest_framework import generics
from .models import Product
from . import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

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

@api_view(["GET", "POST"])
def alt_view(request, pk=None, *args, **kwargs):
    """
    This is a function based view which we created for the LIST , CREATE AND RETRIEVE
    VIEW
    """
    method = request.method
    if method == "GET":
        if pk is not None:
            obj = get_object_or_404(Product, pk=pk)
            data = serializers.ProductSerializer(obj).data
            return Response(data)
        queryset = Product.objects.all()
        data = serializers.ProductSerializer(queryset, many=True).data
        return Response(data)
    if method == "POST":
        data = request.data
        serializer = serializers.ProductSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            title = serializer.validated_data.get("title")
            content = serializer.validated_data.get("content") or None
            if content is None:
                content = title
            serializer.save(content=content)
            data = serializer.data
            return Response(data)
