from django.contrib import admin
from .models import Details
# Register your models here.

class DetailsAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'gender', 'country', 'treatment_required')

    fieldsets = [
        ('Personal Details', {'fields': ['name', 'age', 'gender', 'country', 'state']}),
        ('Company Details', {'fields': ['self_employment', 'family_history', 'work_interfere', 'no_of_employee'
            , 'remote_work', 'tech_company']}),
        ('Health Conditions', {'fields': ['benefits', 'wellness', 'seek_help', 'anonymity', 'leave']}),
        ('Mental Health Conditions', {'fields': ['mental_health_consequence', 'phys_health_consequence', 'mental_health_interview', 'phys_health_interview', 'mental_vs_physical','obs_consequence']}),
        ('Results', {'fields': ['treatment_required']}),
    ]



admin.site.register(Details, DetailsAdmin)

