from django.urls import path
from . import views

urlpattern =[
    path('', views.list_products, name='list_products'),
    path('product/<int:pk>/', views.product_details, name='product_details'),
]