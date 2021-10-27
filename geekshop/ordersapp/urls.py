from django.urls import path
from .views import OrderDelete, OrderDetail, OrderUpdate, OrderCreate, OrderList, get_product_price

app_name = 'orders'

urlpatterns = [
    path('', OrderList.as_view(), name='list'),
    path('create/', OrderCreate.as_view(), name='create'),
    path('update/<int:pk>/', OrderUpdate.as_view(), name='update'),
    path('read/<int:pk>/', OrderDetail.as_view(), name='read'),
    path('delete/<int:pk>/', OrderDelete.as_view(), name='delete'),
    path('forming_complete/<int:pk>/', OrderUpdate.order_forming_complete, name='forming_complete'),
    path('product/<int:pk>/price/', get_product_price, name='product_price'),

]
