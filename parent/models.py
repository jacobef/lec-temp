from django.db import models
from accounts.models import LECUser


class Student(models.Model):
    name = models.CharField(max_length=500)
    pronouns = models.CharField(max_length=50)
    allergies = models.TextField(max_length=1000)
    parent = models.ForeignKey(to=LECUser, related_name="children", on_delete=models.CASCADE)


class ProgramRegistration(models.Model):
    student_name = models.CharField(max_length=500)
    student_pronouns = models.CharField(max_length=50)
    student_allergies = models.TextField(max_length=1000)
    parent_name = models.CharField(max_length=500)
    parent_email = models.EmailField(max_length=320)
    emergency_contact_name = models.CharField(max_length=200)
    emergency_contact_phone_number = models.CharField(max_length=25)

