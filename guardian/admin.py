from django.contrib import admin
from guardian import models

admin.site.register(models.Student)
admin.site.register(models.ProgramRegistration)
