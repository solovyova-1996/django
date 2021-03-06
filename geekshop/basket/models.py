from django.db import models
from users.models import User
from mainapp.models import Product


# class BasketQuerySet(models.QuerySet):
#
#     def delete(self, *args, **kwargs):
#         for item in self:
#             item.product.quantity += item.quantity
#             item.product.save()
#         super(BasketQuerySet, self).delete()


class Basket(models.Model):
    # objects = BasketQuerySet.as_manager()
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

    @staticmethod
    def get_item(pk):
        return Basket.objects.get(pk=pk).quantity

    # def delete(self, using=None, keep_parents=False):
    #     self.product.quantity += self.quantity
    #     self.save()
    #     super(Basket, self).delete()
    #
    # def save(self, force_insert=False, force_update=False, using=None,
    #          update_fields=None):
    #     if self.pk:
    #         self.product.quantity -= self.quantity - self.get_item(int(self.pk))
    #     else:
    #         self.product.quantity -= self.quantity
    #     self.product.save()
    #     super(Basket, self).save()
