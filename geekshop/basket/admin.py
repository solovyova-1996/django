from django.contrib import admin

from basket.models import Basket


class BasketAdmin(admin.TabularInline):
    model = Basket
    fields = ('product', 'quantity', 'created_timestamp', 'update_timestamp')
    readonly_fields = ('created_timestamp', 'update_timestamp')
    extra = 0
