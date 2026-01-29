from django.contrib import admin
from .models import Airport


@admin.register(Airport)
class AirportAdmin(admin.ModelAdmin):
    # Columns shown in admin list view
    list_display = (
        'airport_name',
        'airport_code',
        'position',
        'duration',
        'left',
        'right',
    )

    # Search bar fields
    search_fields = (
        'airport_name',
        'airport_code',
    )

    # Filters on right sidebar
    list_filter = (
        'position',
    )

    # Order by airport code
    ordering = (
        'airport_code',
    )

    # Fields arrangement in add/edit page
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

    # Improve dropdown usability for relations
    autocomplete_fields = (
        'left',
        'right',
    )
