from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'first_name', 'last_name', 'phone_number', 'is_active')
    search_fields = ('email', 'first_name', 'last_name', 'phone_number')
    list_filter = ('is_active',)
    ordering = ('id',)
