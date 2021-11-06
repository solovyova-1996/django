from django.urls import path
from django.views.decorators.cache import cache_page

from .views import ProductListview, ProductDetail

app_name = 'products'

urlpatterns = [

    path('', ProductListview.as_view(), name='index'),
    # path('category/<int:category_id>/', cache_page(3600)(ProductListview.as_view()), name='category'),
    path('category/<int:category_id>/', ProductListview.as_view(), name='category'),
    path('category-discharge/<discharge>/', ProductListview.as_view(), name='category_discharge'),
    path('detail/<int:pk>/', cache_page(ProductDetail.as_view()), name='detail')

]
