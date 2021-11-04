from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from geekshop.mixin import BaseClassContextMixin
from .models import Product, ProductCategory
from django.conf import settings
from django.core.cache import cache


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
        context['products'] = self.get_link_product()
        return context

    def get_queryset(self):
        if self.kwargs:
            if 'category_id' in self.kwargs.keys():
                return Product.objects.filter(category=self.kwargs['category_id'])
            elif 'discharge' in self.kwargs.keys():
                return self.get_link_product()
        else:
            return self.get_link_product()
    @staticmethod
    def get_link_product():
        if settings.LOW_CACHE:
            key = 'links_product'
            link_products = cache.get(key)
            if link_products is None:
                link_products = Product.objects.all()
                cache.set(key, link_products)
            return link_products
        else:
            return Product.objects.all().select_related('category')


# def get_links_category():
#     if settings.LOW_CACHE:
#         key = 'links_category'
#         link_category = cache.get(key)
#         if link_category is None:
#             link_category = ProductCategory.objects.all()
#             cache.set(key,link_category)
#         return link_category
#     else:
#         return ProductCategory.objects.all()
