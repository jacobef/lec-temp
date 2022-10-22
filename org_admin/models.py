from django.db import models

# from guardian.models import Student  # Circular import?
# from org_admin.models import Program


class Survey(models.Model):
    name = models.CharField(max_length=100)
    is_active = models.BooleanField()
    # program = models.ForeignKey(to=Program, on_delete=models.CASCADE, related_name="registrations")
    question = models.TextField(max_length=1000)

class Program(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    is_active = models.BooleanField()
    # roster = models.ManyToManyField(to=Student, related_name="roster")  # Not sure this is correct
    surveys = models.ManyToManyField(to=Survey, related_name="surveys")
    grade_level = models.IntegerField()

    def __str__(self):
        return self.name
