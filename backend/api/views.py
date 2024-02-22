import json
from django.http import JsonResponse
from products.models import Product

def api_home(request, *args, **kwargs):
    product = Product.objects.all().order_by("?").first()
    data = {}
    if product:
        data["id"] = product.id
        data["title"] = product.title
        data["content"] = product.content
        data["price"] = product.price

    return JsonResponse(data)