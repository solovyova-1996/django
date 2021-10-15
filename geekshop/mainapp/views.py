from django.shortcuts import render
from django.views.generic import ListView

from .models import ProductCategory, Product



def index(request):
    context = {'title': 'geekshop'}
    return render(request, 'mainapp/index.html', context)


class ProductListview(ListView):
    model = Product
    template_name = 'mainapp/products.html'
    title = 'catalog'
    paginate_by = 3
    ordering = ['-id']

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super(ProductListview, self).get_context_data(**kwargs)
    #     context['categories'] = ProductCategory.objects.all()
    #     return context

    def get_queryset(self):
        if self.kwargs:
            if 'category_id' in self.kwargs.keys():
                return Product.objects.filter(category=self.kwargs['category_id'])
            elif 'discharge' in self.kwargs.keys():
                return Product.objects.all()
        else:
            return Product.objects.all()
