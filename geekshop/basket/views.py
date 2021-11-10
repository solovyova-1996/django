from django.db import connection
from django.db.models import F
from django.http import JsonResponse
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import UpdateView, DeleteView, CreateView, FormView
from django.views.generic.edit import FormMixin, ProcessFormView

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
            # basket.quantity += 1
            # F-объект работает напрямую с БД, берет актуальное количество(обновляет данные)
            basket.quantity = F('quantity')+1
            basket.save()
            # update_queries = list(filter(lambda x: 'UPDATE' in x['sql'], connection.queries))
            # print(f'basket_add{update_queries}')
        return redirect(self.success_url)

# class BasketView(CreateView):
#     model = Basket
#     template_name = 'mainapp/products_list.html'
#     fields = ['product']
#     success_url = reverse_lazy('products:index')
#
#     def __init__(self,*args,**kwargs):
#         super(BasketView, self).__init__(*args,**kwargs)
#
#     def get_context_data(self, **kwargs):
#         context = super(BasketView, self).get_context_data(**kwargs)
#         context['products'] = self.get_object().Product.objects.all()
#         return context
#     # def get_context_data(self,*, object_list=None, **kwargs):
#     #     context = super(BasketView, self).get_context_data(**kwargs)
#     #     return context
#
#     def get(self, request, *args,**kwargs):
#
#         product = Product.objects.get(id=kwargs['pk'])
#         # product = self.get_object()
#         # print(product,'g')
#         baskets = Basket.objects.filter(user=self.request.user, product=product)
#         if not baskets.exists():
#             Basket.objects.create(user=self.request.user, product=product, quantity=1)
#         else:
#             basket = baskets.first()
#             basket.quantity += 1
#             basket.save()
#         # page = {}
#         # page['page']=self.request.POST['page_obj']
#         context = super(BasketView, self).get_context_data(**kwargs)
#
#         # context.update({'page_obj': self.request.POST['page_obj']})
#         result = render_to_string('mainapp/products_list.html',context=context, request=request)
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
