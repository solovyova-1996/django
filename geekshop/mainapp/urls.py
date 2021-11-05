from django.urls import path
from .views import ProductListview, ProductDetail

app_name = 'products'

urlpatterns = [

    path('', ProductListview.as_view(), name='index'),
    path('category/<int:category_id>/', ProductListview.as_view(), name='category'),
    path('category-discharge/<discharge>/', ProductListview.as_view(), name='category_discharge'),
    path('detail/<int:pk>/', ProductDetail.as_view(), name='detail')

]
