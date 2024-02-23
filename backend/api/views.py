import json
from django.forms.models import model_to_dict
from django.http import JsonResponse
from products.models import Product

from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.serializers import ProductSerializer


@api_view(["POST"])
def api_home(request, *args, **kwargs):

    request_data = request.data
    serializer = ProductSerializer(data=request_data)
    if serializer.is_valid(raise_exception=True):
        # data = serializer.save()
        print(serializer.data)
        return Response(serializer.data)