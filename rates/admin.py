from django.contrib import admin
from .models import USDRateRequest

@admin.register(USDRateRequest)
class USDRateRequestAdmin(admin.ModelAdmin):
    list_display = ('rate', 'created_at')