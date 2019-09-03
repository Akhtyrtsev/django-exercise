from django.contrib import admin
from .models import Organization, Department, Employee, Status
from rest_framework.authtoken.admin import TokenAdmin

TokenAdmin.raw_id_fields = ['user']

admin.site.register(Organization)
admin.site.register(Department)
admin.site.register(Employee)
admin.site.register(Status)

# Register your models here.
