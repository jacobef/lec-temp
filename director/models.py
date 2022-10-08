from django.db import models
from parent.models import Student


class Program(models.Model):
    students = models.ManyToManyField(to=Student, related_name="programs", blank=True)
    description = models.TextField(max_length=5000)
