from django.db import models
from accounts.models import LECUser
from org_admin.models import Program


class Student(models.Model):
    name = models.CharField(max_length=500)
    pronouns = models.CharField(max_length=50)
    allergies = models.TextField(max_length=1000)
    guardian = models.ForeignKey(to=LECUser, related_name="children", on_delete=models.CASCADE)
    additional_info = models.TextField(max_length=1000)

    def __str__(self):
        return self.name

class ProgramRegistration(models.Model):
    students = models.ManyToManyField(to=Student, related_name="program_registrations")
    program = models.ForeignKey(to=Program, on_delete=models.CASCADE, related_name="registrations")
    emergency_contact_name = models.CharField(max_length=200)
    emergency_contact_phone_number = models.CharField(max_length=25)
