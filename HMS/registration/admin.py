from django.contrib import admin
from . models import patients, doctors

admin.site.register(patients)
admin.site.register(doctors)
