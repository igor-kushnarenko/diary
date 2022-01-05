from django.contrib import admin

from users import models


@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'birthday', 'last_login',
                    'is_active', 'is_staff', 'is_admin',)
    readonly_fields = ('last_login',)
    search_fields = ('email', 'first_name', 'last_name',)
    list_filter = (
        ('is_active', admin.BooleanFieldListFilter),
        ('is_staff', admin.BooleanFieldListFilter),
        ('is_admin', admin.BooleanFieldListFilter),
        ('last_login', admin.DateFieldListFilter),
    )