from django.contrib import admin

# Register your models here.
from cevents.models import EventsModel


@admin.register(EventsModel)
class EventsModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'event_location']
    search_fields = ['title', 'short_description', 'event_location']
    list_filter = ['created_at']
