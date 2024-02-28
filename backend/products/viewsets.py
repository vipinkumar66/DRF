from rest_framework import viewsets, mixins
from .models import Product
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    """
    This one will have all the methods: (get, post, delete, update, patch)
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"


class ProductGenericViewset(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
    ):
    """
    This one supports only two type:
    get and retrieve
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"

# These two can be used as an individual view and combine it with the separate urls
generic_view_list = ProductGenericViewset.as_view({"get":"list"})
generic_view_retrieve = ProductGenericViewset.as_view({"get":"retrieve "})
