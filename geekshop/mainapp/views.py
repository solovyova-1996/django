from django.shortcuts import render
import json
import os
from .models import ProductCategory, Product


# Create your views here.
def index(request):
    context = {'title': 'geekshop'}
    return render(request, 'mainapp/index.html', context)


def products(request):
    product = Product.objects.all()
    context = {
        'title': 'catalog',
        'products': product
    }

    return render(request, 'mainapp/products.html', context)
