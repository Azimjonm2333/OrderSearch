from utils.base.models import Timestampble, Permalinkable
from django.db import models
from slugify import slugify



class Category(Timestampble, Permalinkable):
    name = models.CharField(
        verbose_name='Название',
        max_length=255
    )
    parent = models.ForeignKey(
        "self",
        verbose_name="Родитель",
        related_name='category_children',
        on_delete=models.SET_NULL,
        null=True, blank=True
    )

    def __str__(self):
        return self.name


    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

