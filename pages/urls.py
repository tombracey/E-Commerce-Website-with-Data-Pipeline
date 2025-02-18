from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path('discover-oud/', views.discover_oud, name='discover_oud'),
    path("products/", views.products, name="products"),
    path('contact/', views.contact_us, name='contact_us'),
]