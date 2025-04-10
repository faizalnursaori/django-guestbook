from django.contrib import admin

from .models import Guest


# Register your models here.
@admin.register(Guest)
class GuestAdmin(admin.ModelAdmin):
    list_display = ("name", "institution", "visit_date")
    search_fields = ("name", "institution")
    list_filter = ("visit_date",)
