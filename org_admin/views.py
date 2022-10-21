from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from org_admin.models import Program, ProgramAnnouncement


class AddProgram(CreateView):
    model = Program
    fields = "__all__"
    template_name = "org_admin/add_program.html"
    success_url = reverse_lazy("org_admin:programs")

class MakeAnnouncement(CreateView):
    model = ProgramAnnouncement
    fields = ["title", "content"]
    template_name = "org_admin/make_announcement.html"
    success_url = reverse_lazy("org_admin:programs")

    def form_valid(self, form):
        form.instance.program = Program.objects.get(pk=int(self.kwargs["program_pk"]))
        form.instance.save()
        return super().form_valid(form)

def view_announcements(request, program_pk):
    return render(request, "org_admin/view_announcements.html",
                  {'announcements': ProgramAnnouncement.objects.filter(program__pk=program_pk)})

def programs(request):
    return render(request, "org_admin/view_programs.html", {"programs": Program.objects.all()})
