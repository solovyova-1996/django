from django.urls import path
from .views import ProductListview

app_name = 'products'

urlpatterns = [

    path('', ProductListview.as_view(), name='index'),
    path('category/<int:category_id>/', ProductListview.as_view(), name='category'),
    path('category-discharge/<discharge>/', ProductListview.as_view(), name='category_discharge'),

]
