from django.contrib import admin
from .models import Order, Category



@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """
    Административная панель для модели Order.
    """
    list_display = (
        'title',
        'description',
        'category',
        'user'
    )
    search_fields = (
        'title',
    )
    list_filter = (
        'category',
        'user'
    )
    autocomplete_fields = (
        'category',
        'user',
    )





@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Административная панель для модели Category.
    """
    list_display = (
        'name',
        'slug',
        'parent'
    )
    search_fields = (
        'name',
    )
    list_filter = (
        'parent',
    )
    autocomplete_fields = (
        "parent",
    )
    prepopulated_fields = {
        "slug": (
            "name",
        )
    }
