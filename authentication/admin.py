from django.contrib import admin
from authentication.models import *

# Register your models here.
admin.site.register(Clinician)
admin.site.register(ClinicalInstructor)
admin.site.register(Patient)