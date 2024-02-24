from django.urls import path
from . import views

urlpatterns = [
    path("<int:pk>/", views.ProductRetrieveView.as_view()),
    path("", views.ProductCreateView.as_view()),

]