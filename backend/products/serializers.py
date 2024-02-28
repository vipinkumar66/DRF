from rest_framework import serializers
from products.models import Product

class ProductSerializer(serializers.ModelSerializer):
    # this is a way to add a custom field
    my_discount = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Product
        fields = [
            "pk",
            "title",
            "price",
            "content",
            "sale_price",
            "my_discount"
        ]

    def get_my_discount(self, obj):
        # so we can see that this serializer recieves our instance of model and we can grab all the details
        if not hasattr(obj, "id"):
            return None
        if not isinstance(obj, Product):
            return None
        return obj.get_discount()