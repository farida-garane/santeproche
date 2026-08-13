from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'role', 'telephone', 'is_staff')
    fieldsets = UserAdmin.fieldsets + (
        ('Informations santé', {'fields': ('role', 'telephone')}),
    )


admin.site.register(User, CustomUserAdmin)