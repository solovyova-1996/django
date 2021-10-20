from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, CreateView


class OrderList(ListView):
    pass

class OrdersItemsCreate(CreateView):
    pass