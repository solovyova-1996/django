from django.shortcuts import render
import json
import os


# Create your views here.
def index(request):
    context = {'title': 'geekshop'}
    return render(request, 'mainapp/index.html', context)


def products(request):
    name_path = os.path.join('mainapp', 'fixtures')
    name_file = os.path.join(name_path, 'db.json')
    with open(name_file, 'r', encoding='UTF-8') as f:
        product = json.load(f)

    context = {
        'title': 'catalog',
        'products': product
    }

    return render(request, 'mainapp/products.html', context)
