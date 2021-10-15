from django.db import models
from users.models import User
from mainapp.models import Product


class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    update_timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Корзина для {self.user.username} | Продукт {self.product.name}'

    def sum(self):
        return self.quantity * self.product.price

    @staticmethod
    def total_quantity(user):
        total_quantity = 0
        baskets = Basket.objects.filter(user=user)
        for basket in baskets:
            total_quantity += basket.quantity
        return total_quantity
    @staticmethod
    def total_sum(user):
        total_sum = 0
        baskets = Basket.objects.filter(user=user)
        for basket in baskets:
            total_sum += basket.sum()
        return total_sum
