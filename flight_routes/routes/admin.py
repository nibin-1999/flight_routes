from django.contrib import admin
from .models import Airport


@admin.register(Airport)
class AirportAdmin(admin.ModelAdmin):
    """
    Admin configuration for managing Airport records,
    including route connections and search optimization.
    """

    list_display = (
        'airport_name',
        'airport_code',
        'position',
        'duration',
        'left',
        'right',
    )

    search_fields = (
        'airport_name',
        'airport_code',
    )

    list_filter = (
        'position',
    )

    ordering = (
        'airport_code',
    )

    fieldsets = (
        ('Airport Information', {
            'fields': (
                'airport_name',
                'airport_code',
                'duration',
            )
        }),
        ('Route Connections', {
            'fields': (
                'position',
                'left',
                'right',
            )
        }),
    )

    autocomplete_fields = (
        'left',
        'right',
    )
