from django.shortcuts import render
import json
import os
from .models import ProductCategory, Product


def index(request):
    context = {'title': 'geekshop'}
    return render(request, 'mainapp/index.html', context)


def products(request):
    context = {
        'title': 'catalog',
        'categories': ProductCategory.objects.all(),
        'products': Product.objects.all()
    }

    return render(request, 'mainapp/products.html', context)
