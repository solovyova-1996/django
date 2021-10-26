from django.urls import path
from .views import AdminView, UserListView, UserUpdateView, UserCreateView, UserDeleteView, CategoriesListView, \
    CategoriesCreateView, CategoriesUpdateView, CategoriesDeleteView, ProductCreateView, ProductListView, \
    ProductDeleteView, ProductUpdateView

app_name = 'admins'

urlpatterns = [
    path('', AdminView.as_view(), name='index'),
    path('users/', UserListView.as_view(), name='admins_user'),
    path('users-create/', UserCreateView.as_view(), name='admins_user_create'),
    path('users-update/<int:pk>/', UserUpdateView.as_view(), name='admins_user_update'),
    path('users-delete/<int:pk>/', UserDeleteView.as_view(), name='admins_user_delete'),
    path('categories/', CategoriesListView.as_view(), name='admins_categories'),
    path('categories-create/', CategoriesCreateView.as_view(), name='admins_categories_create'),
    path('categories-update/<int:pk>/', CategoriesUpdateView.as_view(), name='admins_categories_update'),
    path('categories-delete/<int:pk>/', CategoriesDeleteView.as_view(), name='admins_categories_delete'),
    path('products/', ProductListView.as_view(), name='admins_products'),
    path('products-create/', ProductCreateView.as_view(), name='admins_products_create'),
    path('products-update/<int:pk>/', ProductUpdateView.as_view(), name='admins_products_update'),
    path('products-delete/<int:pk>/', ProductDeleteView.as_view(), name='admins_products_delete'),
]
