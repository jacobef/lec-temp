from django import forms
from django.core.exceptions import ValidationError

from guardian.models import ProgramRegistration, Student


class ProgramRegistrationForm(forms.ModelForm):
    class Meta:
        model = ProgramRegistration
        # "students" is also a field, but it's rendered and validated manually
        fields = ["program", "emergency_contact_name", "emergency_contact_phone_number"]

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super().__init__(*args, **kwargs)

    def clean(self):
        for student_pk in self.data.getlist("students"):
            student = Student.objects.get(pk=student_pk)
            if student.guardian != self.user:
                # TODO make error message friendlier and send them to report page or something
                raise ValidationError(f"Internal error: Child \"{student}\" does not belong to user.")
        return super().clean()

