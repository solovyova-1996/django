from django.urls import path
from .views import OrderDelete, OrderDetail, OrderUpdate, OrdersItemsCreate, OrderList, order_forming_complete

app_name = 'orders'

urlpatterns = [
    path('', OrderList.as_view(), name='list'),
    path('create/', OrdersItemsCreate.as_view(), name='create'),
    path('update/<int:pk>/', OrderUpdate.as_view(), name='update'),
    path('read/<int:pk>/', OrderDetail.as_view(), name='read'),
    path('delete/<int:pk>/', OrderDelete.as_view(), name='delete'),
    path('delete/<int:pk>/', order_forming_complete, name='forming_complete'),

]
