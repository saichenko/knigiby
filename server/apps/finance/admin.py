from django.contrib import admin

from .models.models import DollarValue


@admin.register(DollarValue)
class TestAdmin(admin.ModelAdmin):
    readonly_fields = (
        'last_modified',
    )
