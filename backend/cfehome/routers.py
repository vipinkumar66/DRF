from rest_framework.routers import DefaultRouter
from products.viewsets import ProductViewSet, ProductGenericViewset

router  = DefaultRouter()
router.register(r'products-abc', ProductGenericViewset, basename="products")

urlpatterns =  router.urls