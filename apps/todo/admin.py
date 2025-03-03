from django.contrib import admin

# Register your models here.
from .models import User, Todo

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'phone_number', 'created_at', 'age')
    search_fields = ('username', 'email', 'phone_number')
    list_filter = ('created_at',)
    ordering = ('-created_at',)

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_completed', 'created_at')
    search_fields = ('title', 'description')
    list_filter = ('is_completed', 'created_at')
    ordering = ('-created_at',)

