from django.db import models
from django.contrib.auth.models import AbstractUser
from utils.base.models import Timestampble


class User(AbstractUser, Timestampble):
    first_name = None
    last_name = None

    email = models.EmailField(
        verbose_name="Email",
        unique=True,
        max_length=200,
    )
    category = models.ManyToManyField(
        'orders.Category',
        verbose_name="Категория"
    )
