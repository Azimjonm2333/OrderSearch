from django.db import models


class Permalinkable(models.Model):
    slug = models.SlugField(
        db_index=True
    )

    class Meta:
        abstract = True


class Timestampble(models.Model):
    created_at = models.DateTimeField(verbose_name="Время создания", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Время изменения", auto_now=True)

    class Meta:
        abstract = True
