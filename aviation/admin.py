from django.contrib import admin
from .models import Aircraft


@admin.register(Aircraft)
class AircraftAdmin(admin.ModelAdmin):
    list_display = ('aircraft', 'status', 'priority', 'type', 'errors_count', 'info_count',)
    search_fields = ('aircraft',)
