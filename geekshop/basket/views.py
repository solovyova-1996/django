from django.http import JsonResponse
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import UpdateView, DeleteView, CreateView

from mainapp.models import Product
from .models import Basket


class BasketView(View):
    model = Basket
    template_name = 'mainapp/products_list.html'
    fields = ['product']
    success_url = reverse_lazy('products:index')

    def get(self, request, pk,**kwargs):
        product = Product.objects.get(id=pk)
        baskets = Basket.objects.filter(user=self.request.user, product=product)
        if not baskets.exists():
            Basket.objects.create(user=self.request.user, product=product, quantity=1)
        else:
            basket = baskets.first()
            basket.quantity += 1
            basket.save()
        return redirect(self.success_url)

# class BasketView(CreateView):
#     model = Basket
#     template_name = 'mainapp/products_list.html'
#     fields = ['product']
#     success_url = reverse_lazy('products:index')
#
#     def post(self, request, *args,**kwargs):
#         # product = Product.objects.get(id=kwargs['pk'])
#         product = self.get_object(Product.objects.filter()) #Product.objects.get(id=pk)
#         baskets = Basket.objects.filter(user=self.request.user, product=product)
#         if not baskets.exists():
#             Basket.objects.create(user=self.request.user, product=product, quantity=1)
#         else:
#             basket = baskets.first()
#             basket.quantity += 1
#             basket.save()
#         context = super().get_context_data(**kwargs)
#         context.update({'products': Product.objects.all()})
#         result = render_to_string('mainapp/products_list.html', context,request=request)
#         return JsonResponse({'result': result})

class BasketDeleteView(DeleteView):
    model = Basket
    template_name = 'users/profile.html'
    success_url = reverse_lazy('users:profile')


class BasketUpdateView(UpdateView):
    model = Basket
    template_name = 'users/profile.html'
    success_url = reverse_lazy('users:profile')
    fields = ['product']

    def get(self, request, *args, **kwargs):
        basket_id = kwargs['id']
        quantity = kwargs['quantity']
        if request.is_ajax():
            basket = Basket.objects.get(id=basket_id)
            if quantity > 0:
                basket.quantity = quantity
                basket.save()
            else:
                basket.delete()
            result = render_to_string('basket/basket.html', request=request)
            return JsonResponse({'result': result})
        return redirect(self.success_url)
