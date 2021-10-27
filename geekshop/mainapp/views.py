from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from geekshop.mixin import BaseClassContextMixin
from .models import Product


class IndexView(ListView, BaseClassContextMixin):
    template_name = 'mainapp/index.html'
    title = 'geekshop'

    def get_queryset(self):
        return


class ProductListview(ListView, BaseClassContextMixin):
    model = Product
    template_name = 'mainapp/products.html'
    title = 'catalog'
    paginate_by = 3
    ordering = ['-id']

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductListview, self).get_context_data(**kwargs)
        context['products'] = Product.objects.all()
        return context

    def get_queryset(self):
        if self.kwargs:
            if 'category_id' in self.kwargs.keys():
                return Product.objects.filter(category=self.kwargs['category_id'])
            elif 'discharge' in self.kwargs.keys():
                return Product.objects.all()
        else:
            return Product.objects.all()
