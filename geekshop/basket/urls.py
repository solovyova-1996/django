from django.urls import path
from .views import BasketDeleteView, BasketUpdateView, BasketView

app_name = 'basket'

urlpatterns = [
    path('add/<int:pk>/', BasketView.as_view(), name='basket'),
    path('remove/<int:pk>/', BasketDeleteView.as_view(), name='basket_remove'),
    path('edit/<int:id>/<int:quantity>/', BasketUpdateView.as_view(), name='basket_edit'),
]
