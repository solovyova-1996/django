from django.db import connection
from django.db.models import F
from django.http import JsonResponse
from django.shortcuts import render, HttpResponseRedirect
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from users.models import User
from admins.forms import UserAdminRegisterForm, UserAdminProfileForm, ProductCategoryUpdateForm
from geekshop.mixin import CustomDispatchMixin, BaseClassContextMixin
from .forms import ProductCategoryEditForm, ProductForm
from mainapp.models import ProductCategory, Product


def db_profile_by_type(prefix, type, queries):
    update_queries = list(filter(lambda x: type in x['sql'], queries))
    print(f'db_profile {type} for {prefix}:')
    [print(query['sql']) for query in update_queries]


class AdminView(ListView, BaseClassContextMixin):
    template_name = 'admins/admin.html'
    title = 'Админка | Главная'

    def get_queryset(self):
        return


class UserListView(ListView, CustomDispatchMixin):
    model = User
    template_name = 'admins/admin-users-read.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserListView, self).get_context_data(**kwargs)
        context['title'] = 'Админка | Пользователи'
        return context


class UserCreateView(CreateView, CustomDispatchMixin):
    model = User
    template_name = 'admins/admin-users-create.html'
    form_class = UserAdminRegisterForm
    success_url = reverse_lazy('admins:admins_user')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Админка | Регистрация'
        return context


class UserUpdateView(UpdateView, CustomDispatchMixin):
    model = User
    template_name = 'admins/admin-users-update-delete.html'
    form_class = UserAdminProfileForm
    success_url = reverse_lazy('admins:admins_user')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Админка | Обновление пользователя'
        return context


class UserDeleteView(DeleteView, CustomDispatchMixin):
    model = User
    template_name = 'admins/admin-users-update-delete.html'
    success_url = reverse_lazy('admins:admins_user')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.is_active:
            self.object.is_active = False
        else:
            self.object.is_active = True
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class CategoriesListView(ListView, CustomDispatchMixin):
    model = ProductCategory
    template_name = 'admins/admin-categories-read.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CategoriesListView, self).get_context_data(**kwargs)
        context['title'] = 'Категории'
        context['objects'] = ProductCategory.objects.all()
        return context


class CategoriesCreateView(CreateView, CustomDispatchMixin):
    model = ProductCategory
    template_name = 'admins/admin-categories-create.html'
    form_class = ProductCategoryEditForm
    success_url = reverse_lazy('admins:admins_categories')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CategoriesCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Админка | Создание категорий'
        return context


class CategoriesUpdateView(UpdateView, CustomDispatchMixin):
    model = ProductCategory
    template_name = 'admins/admin-categories-update-delete.html'
    form_class = ProductCategoryUpdateForm
    success_url = reverse_lazy('admins:admins_categories')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Админка | Редактирование категории'
        return context

    def form_valid(self, form):
        if 'discount' in form.cleaned_data:
            discount = form.cleaned_data['discount']
            if discount:
                print(f'применяется скидка {discount}% к товарам категории {self.object.name}')
                self.object.product_set.update(price=F('price') * (1 - discount / 100))
                db_profile_by_type(self.__class__, 'UPDATE', connection.queries)
        return HttpResponseRedirect(self.get_success_url())


class CategoriesDeleteView(DeleteView, CustomDispatchMixin):
    model = ProductCategory
    template_name = 'admins/admin-categories-read.html'
    success_url = reverse_lazy('admins:admins_categories')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.is_active:
            self.object.is_active = False
            self.object.product_set.update(is_active=False)
        else:
            self.object.is_active = True
            self.object.product_set.update(is_active=True)
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class ProductListView(ListView, CustomDispatchMixin):
    model = Product
    template_name = 'admins/admin-products-read.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context['title'] = 'Админка | Продукты'
        context['objects'] = Product.objects.all()
        return context


class ProductCreateView(CreateView, CustomDispatchMixin):
    model = Product
    template_name = 'admins/admin-products-create.html'
    form_class = ProductForm
    success_url = reverse_lazy('admins:admins_products')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Админка | Редактирование продукта'
        return context


class ProductUpdateView(UpdateView, CustomDispatchMixin):
    model = Product
    template_name = 'admins/admin-products-update-delete.html'
    form_class = ProductForm
    success_url = reverse_lazy('admins:admins_products')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Админка | Редактирование продукта'
        return context


class ProductDeleteView(DeleteView, CustomDispatchMixin):
    model = Product
    template_name = 'admins/admin-products-update-delete.html'
    # success_url = reverse_lazy('admins:admins_products')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.is_active:
            self.object.is_active = False
        else:
            self.object.is_active = True
        self.object.save()
        # result = render_to_string('admins/inc.html', request=request)
        # return JsonResponse({'result': result})
        # return HttpResponseRedirect(self.get_success_url())
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
