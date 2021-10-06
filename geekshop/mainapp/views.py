from django.shortcuts import render

from .models import ProductCategory, Product


def index(request):
    context = {'title': 'geekshop'}
    return render(request, 'mainapp/index.html', context)


def products(request, category_id=None):
    products = Product.objects.filter(category_id=category_id) if category_id != None else Product.objects.all()
    context = {
        'title': 'catalog',
        'categories': ProductCategory.objects.all(),
        'products': products
    }

    return render(request, 'mainapp/products.html', context)
