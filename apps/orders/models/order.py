from django.conf import settings
from django.db import models
from utils.base.models import Timestampble



class Order(Timestampble):
    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey(
        'orders.Category',
        verbose_name="Категория",
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name="Пользователь",
        on_delete=models.CASCADE
    )


    def __str__(self):
        return self.title


    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
