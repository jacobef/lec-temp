from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from org_admin.models import Program


class AddProgram(CreateView):
    model = Program
    fields = "__all__"
    template_name = "org_admin/add_program.html"
    success_url = reverse_lazy("org_admin:programs")

def programs(request):
    return render(request, "org_admin/view_programs.html", {"programs": Program.objects.all()})
