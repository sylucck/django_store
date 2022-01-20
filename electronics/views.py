from django.shortcuts import render, redirect
from .models import *
from .forms import *
import requests
import environ
# Initialise environment variables
env = environ.Env()
environ.Env.read_env()
# Create your views here.

def list_products(request):
    products= Product.objects.all()
    context ={
        'products':products
    }
    return render(request, 'products.html', context)

def product_details(request, pk):
    data = Product.objects.get(pk=pk)
    if request.method=='POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
             name=  form.cleaned_data['name']
             email = form.cleaned_data['email']
             amount = form.cleaned_data['amount']
             phone = form.cleaned_data['phone']
             return redirect(str(process_payment(name,email,amount,phone)))
    else:
        form = PaymentForm()
    ctx={
        'product':data,
        'form':form
    }
    return render(request, 'details.html', ctx)

def process_payment(name,email,amount,phone):
     auth_token= env('SECRET_KEY')
     hed = {'Authorization': 'Bearer ' + auth_token}
     data = {
                "tx_ref":''+str(math.floor(1000000 + random.random()*9000000)),
                "amount":amount,
                "currency":"KES",
                "redirect_url":"http://localhost:8000/callback",
                "payment_options":"card",
                "meta":{
                    "consumer_id":23,
                    "consumer_mac":"92a3-912ba-1192a"
                },
                "customer":{
                    "email":email,
                    "phonenumber":phone,
                    "name":name
                },
                "customizations":{
                    "title":"Supa Electronics Store",
                    "description":"Best store in town",
                    "logo":"https://getbootstrap.com/docs/4.0/assets/brand/bootstrap-solid.svg"
                }
                }
     url = ' https://api.flutterwave.com/v3/payments'
     response = requests.post(url, json=data, headers=hed)
     response=response.json()
     link=response['data']['link']
     return link