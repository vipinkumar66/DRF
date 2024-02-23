from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=99.99)
    content = models.TextField(blank=True, null=True)

    @property
    def sale_price(self):
        # After giving 20% discount
        return "%.2f" %(float(self.price) * 0.8)

    def get_discount(self):
        return "122"