from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from apps.accounts.models import User
from django.utils.translation import gettext_lazy as _



@admin.register(User)
class CustomUserAdmin(UserAdmin):
    """
    Административная панель для модели User.

    Здесь можно настроить отображение и редактирование пользователей.
    """
    fieldsets = (
        (None, {'fields': (
            'username',
            'category',
            'email',
            'password',
        )}),
        (_('Permissions'), {'fields': (
            'is_superuser',
            'groups',
            'user_permissions'
        )}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'username',
                'category',
                'email',
                'password1',
                'password2',
            ),
        }),
    )
    list_display = (
        'username',
        'email',
    )
    autocomplete_fields = (
        "category",
    )
    search_fields = ('username',)
    ordering = ('username',)
