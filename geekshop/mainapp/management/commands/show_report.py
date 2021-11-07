from datetime import timedelta

from prettytable import PrettyTable
from django.core.management import BaseCommand
from django.db.models import Q, F, When, Case, IntegerField, DecimalField

from ordersapp.models import OrderItem


class Command(BaseCommand):
    def handle(self, *args, **options):
        ACTION_1 = 1
        ACTION_2 = 2
        ACTION_3 = 3
        # время прошедшее после оплаты товара
        action_1_time_delta = timedelta(hours=12)
        action_2_time_delta = timedelta(days=1)
        # Размер скидки
        action_1_discount = 0.3
        action_2_discount = 0.15
        action_3_discount = 0.05
        # считаем время между обновлением и созданием товара и создаем фильтрацию
        # lte - <=
        # получи дату изменения заказа если она меньше либо равна дате создания заказа + 12 часов
        action_1_condition = Q(order__update__lte=F('order__created') + action_1_time_delta)
        # gt - >, gte ->=
        # получи дату изменения заказа если она больше чем дата создания заказа +12 часов и меньше чем дата создания заказа + 1 день
        action_2_condition = Q(order__update__gt=F('order__created') + action_1_time_delta) & Q(
            order__update__lte=F('order__created') + action_2_time_delta)
        # получи дату изменения заказа если она больше чем дата создания + 1 день
        action_3_condition = Q(order__update__gt=F('order__created') + action_2_time_delta)

        # если условие верно, то назначается акция
        action_1_order = When(action_1_condition, then=ACTION_1)
        action_2_order = When(action_2_condition, then=ACTION_2)
        action_3_order = When(action_3_condition, then=ACTION_3)
        # если условиу соответствует то сформируем цену закаказа соответственно скидке для данного условия
        # product__price - цена продуста из таблицы Product quantity- кол-во продустов из заказа
        action_1_price = When(action_1_condition, then=F('product__price') * F('quantity') * action_1_discount)
        action_2_price = When(action_2_condition, then=F('product__price') * F('quantity') * -action_2_discount)
        action_3_price = When(action_3_condition, then=F('product__price') * F('quantity') * action_3_discount)
        # annote - добавление полей к информации из таблицы OrderItem
        test_orders = OrderItem.objects.annotate(
            # в один момент времени будет только одно значение из трех и case его использует
            action_order=Case(
                action_1_order,
                action_2_order,
                action_3_order,
                output_field=IntegerField(),
            )).annotate(  # запрос
            total_price=Case(
                action_1_price,
                action_2_price,
                action_3_price,
                output_field=DecimalField(),
            )).order_by('action_order', 'total_price').select_related()

        t_list = PrettyTable(['Заказ', 'Товар', 'Скидка', 'Время'])
        t_list.align = 'l'
        for orderitem in test_orders:
            t_list.add_row([f'{orderitem.action_order} заказ №{orderitem.pk}', f'{orderitem.product.name:15}',
                            f'{abs(orderitem.total_price):6.2f}руб.',
                            orderitem.order.update - orderitem.order.created])
        print(t_list)
