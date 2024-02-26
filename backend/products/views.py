# Single item data => Generic Views

from rest_framework import generics, mixins, permissions, authentication
from .models import Product
from . import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .permissions import IsStaffEditorPermissions
from .authentication import TokenAuthentication


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

class ProductUpdateView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductSerializer
    lookup_field = "pk"

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title

class ProductDeleteView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductSerializer
    lookup_field = "pk"

    def perform_destroy(self, instance):
        # if we want to do any thing with the instance we can do it here
        return super().perform_destroy(instance)


class ProductMixinView(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    generics.GenericAPIView
):
    # This mixin allows us to do this here
    queryset = Product.objects.all()
    serializer_class = serializers.ProductSerializer
    lookup_field = "pk"
    authentication_classes = [
        authentication.SessionAuthentication,
        TokenAuthentication
        ]
    permission_classes = [permissions.IsAdminUser, IsStaffEditorPermissions]

    def get(self, request, *args, **kwargs):
        """
        If we use the post method also still it is going to
        """
        pk = kwargs.get("pk")
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        """
        This is one of the method which is only given to the createapiview
        and it takes two arguments: Instance and the serializer
        """
        title = serializer.validated_data.get("title")
        content = serializer.validated_data.get("content") or None
        if content is None:
            content = "This is a single view doing cool stuff"
        serializer.save(content=content)

product_mixin_view = ProductMixinView.as_view()