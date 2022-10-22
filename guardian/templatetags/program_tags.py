from django.db.models import QuerySet
from django.template import Library

from accounts.models import LECUser
from org_admin.models import Program

register = Library()


@register.filter
def has_unread_announcements_in(user: LECUser, program: Program):
    for announcement in program.announcements.all():
        if user not in announcement.read_by.all():
            return True
    return False

@register.filter
def has_children_in(user: LECUser, program: Program):
    for registration in program.registrations.all():
        for student in registration.students.all():
            if student in user.children.all():
                return True
    return False

@register.filter
def children_in(user: LECUser, program: Program):
    result = set()
    for registration in program.registrations.all():
        for student in registration.students.all():
            if student in user.children.all():
                result.add(student)
    return result
