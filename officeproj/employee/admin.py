from django.contrib import admin
from .models import department,role,employe

# Register your models here.
admin.site.register(department)
admin.site.register(role)
admin.site.register(employe)