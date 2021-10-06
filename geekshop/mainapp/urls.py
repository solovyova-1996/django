
from django.urls import path
from .views import products, categories_discharge

app_name = 'products'

urlpatterns = [

    path('', products, name='index'),
    path('category/<int:category_id>/', products, name='category'),
    path('category-discharge/', categories_discharge, name='category_discharge'),
    path('page/<int:page_id>/', products, name='page'),
]
