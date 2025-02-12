from django.contrib import admin

from users.models import User

# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """ Панель администратора """
    list_display = ('username', 'email', 'is_staff', 'created_at')
    search_fields = ['username', 'email']
    list_filter = ['is_staff', 'created_at']
