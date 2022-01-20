from django.shortcuts import render
from .models import *
# Create your views here.

def list_products(request):
    products= Product.objects.all()
    context ={
        'products':products
    }
    return render(request, 'products.html', context)

def product_details(request, pk):
    data = Product.objects.get(pk=pk)

    ctx= {
        'data':data,
    }
    return render(request, 'details.html', ctx)