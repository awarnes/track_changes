from django.contrib import admin

from .models import TrackChange
# Register your models here.

@admin.register(TrackChange)
class TrackChangeAdmin(admin.ModelAdmin):
    """To display information in a more readable format on the django admin."""

    list_display = ('changed_class', 'operation', 'changed_fields', 'changed_data', 'changed_pk', 'time_changed')
