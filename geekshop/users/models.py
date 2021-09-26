from django.db import models

from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy


# def validate_name(value):
#     if value == 'Станислав':
#         raise ValidationError(gettext_lazy(
#             'Запрещена регистрация пользователей с именем : %(value)s'),
#             code='invalid', params={'value': value}, )


class User(AbstractUser):
    image = models.ImageField(upload_to='users_image', blank=True)
    # first_name = models.CharField(max_length=40, validators=[validate_name])
