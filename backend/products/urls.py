from django.urls import path
from . import views

urlpatterns = [
    path("<int:pk>/", views.alt_view),
    path("", views.alt_view),

]