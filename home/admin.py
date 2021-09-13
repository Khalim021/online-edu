from django.contrib import admin

from home.models import ContactModel, PagesModel


@admin.register(PagesModel)
class PagesModelAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title', 'short_description']
    list_filter = ['created_at']


@admin.register(ContactModel)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'message']
    search_fields = ['name', 'email', 'message']
    list_filter = ['created_at']
