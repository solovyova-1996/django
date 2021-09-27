from django.shortcuts import render, HttpResponseRedirect
from users.models import User
from mainapp.models import Product
from .models import Basket
from django.contrib.auth.decorators import login_required

@login_required
def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)
    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
@login_required
def basket_remove(request,product_id):
    Basket.objects.get(id=product_id).delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
