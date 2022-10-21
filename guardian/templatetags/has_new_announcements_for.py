from django.template import Library

from accounts.models import LECUser
from org_admin.models import Program

register = Library()

@register.filter
def has_new_announcements_for(program: Program, user: LECUser):
    for announcement in program.announcements.all():
        if user not in announcement.read_by.all():
            return True
    return False
