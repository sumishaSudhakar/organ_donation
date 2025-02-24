from django.contrib import admin
from django.utils.html import format_html  # To style admin fields
from .models import Organ, BloodGroup

# Register BloodGroup and Organ Models with Custom Admin Display
@admin.register(BloodGroup)
class BloodGroupAdmin(admin.ModelAdmin):
    list_display = ("blood_group",)  # Display blood group name
    search_fields = ("blood_group",)

@admin.register(Organ)
class OrganAdmin(admin.ModelAdmin):
    list_display = ("organ_name",)
    search_fields = ("organ_name",)