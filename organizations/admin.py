from django.contrib import admin
from .models import Organization, CustomUser

@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'is_main')
    search_fields = ('name',)

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'organization', 'role')
    search_fields = ('username', 'email', 'organization__name')
    list_filter = ('organization', 'role')
