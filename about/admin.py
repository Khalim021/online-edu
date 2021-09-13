from django.contrib import admin

# Register your models here.
from about.models import PartnerModel


@admin.register(PartnerModel)
class PartnerModelAdmin(admin.ModelAdmin):
    list_filter = ['updated_at']
