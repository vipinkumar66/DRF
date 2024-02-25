from django.urls import path
from . import views

urlpatterns = [
    path("<int:pk>/", views.ProductRetrieveView.as_view()),
    # path("", views.ProductListCreateView.as_view()),
    path("", views.product_mixin_view),
    path("<int:pk>/update/", views.ProductUpdateView.as_view()),
    # path("<int:pk>/delete/", views.ProductDeleteView.as_view()),
    path("<int:pk>/delete/", views.product_mixin_view),



]