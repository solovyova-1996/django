from django.db import models

from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy


class User(AbstractUser):
    image = models.ImageField(upload_to='users_image', blank=True)
