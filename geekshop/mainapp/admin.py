from django.contrib import admin

from mainapp.models import ProductCategory, Product

# admin.site.register(Product)
admin.site.register(ProductCategory)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category')
    fields = ('name', 'image', ('price', 'quantity',), 'description', 'category',)
    readonly_fields = ('description',)
    ordering = ('name', 'price')
    search_fields = ('name',)
