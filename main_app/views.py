from django.shortcuts import render, redirect
from .models import Product

# Create your views here.

def home(request):
    return render(request, 'home.html')


def learn(request):
    return render(request, 'learn.html')

def products_index(request):
    products = Product.objects.all()
    return render(request, 'products/index.html', {
        'products': products
    })
    

