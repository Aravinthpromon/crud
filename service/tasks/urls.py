from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.product_list, name='product_list'),  # URL for listing products
    path('products/<int:product_id>/', views.product_detail, name='product_detail'),  # URL for specific product details
]
