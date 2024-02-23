import json
from django.forms.models import model_to_dict
from django.http import JsonResponse
from products.models import Product

from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.serializers import ProductSerializer


@api_view(["GET"])
def api_home(request, *args, **kwargs):
    instance = Product.objects.all().order_by("?").first()
    data = {}
    if instance:
        data = ProductSerializer(instance).data
        # data = model_to_dict(product, fields=["id", "title", "content", "price"])
    return Response(data)