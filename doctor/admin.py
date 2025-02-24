from django.contrib import admin
from .models import DoctorDetails,DoctorDonor

@admin.register(DoctorDetails)
class DoctorDetailsAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialization', 'contact')  # Display fields in the admin list view
    search_fields = ('name', 'specialization__organ_name')  # Enable search by name and specialization
    list_filter = ('specialization',)  # Filter by specialization

admin.site.register(DoctorDonor)

