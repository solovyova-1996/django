from django.test import TestCase

# Create your tests here.
from django.test.client import Client

from mainapp.models import ProductCategory, Product


class TestMainSmokeTest(TestCase):
    status_code_success = 200

    # создание данных для теста
    def setUp(self) -> None:
        category = ProductCategory.objects.create(name='Test')
        Product.objects.create(category=category, name='product_test', price=200)
        self.client = Client()

    # тест на проверку главной страницы
    # Для того чтобы запустить тест python manage.py test и в названии функции вначале test
    def test_products_pages(self):
        response = self.client.get('/')
        # Проверка на равенство
        self.assertEqual(response.status_code, self.status_code_success)

    def test_products_product(self):
        for product_item in Product.objects.all():
            response = self.client.get(f'/products/detail/{product_item.pk}/')
            self.assertEqual(response.status_code, self.status_code_success)

    # проверка есть ли перенаправление при входе в профил неавторизованного пользователя
    def test_products_basket(self):
        response = self.client.get('/users/profile/')
        self.assertEqual(response.status_code, 302)

    def tearDown(self) -> None:
        pass
