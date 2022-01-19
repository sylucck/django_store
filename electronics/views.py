from django.shortcuts import render
from .models import *
# Create your views here.

def list_products(request):
    products=Product.objects.all()
    ctx={
        'products':products
    }
    return render(request, 'products.html', ctx)
