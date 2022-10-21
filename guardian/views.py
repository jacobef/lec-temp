from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView

from guardian.forms import ProgramRegistrationForm
from guardian.models import ProgramRegistration, Student
from org_admin.models import Program, ProgramAnnouncement


def programs(request):
    return render(request, "guardian/view_programs.html", {'programs': Program.objects.all()})


def view_program(request, program_pk):
    return render(request, "guardian/view_program.html", {'program': Program.objects.get(pk=program_pk)})


def view_announcement(request, announcement_pk):
    announcement = ProgramAnnouncement.objects.get(pk=announcement_pk)
    announcement.read_by.add(request.user)
    announcement.save()
    return render(request, "guardian/view_announcement.html",
                  {'announcement': ProgramAnnouncement.objects.get(pk=announcement_pk)})


def children(request):
    return render(request, "guardian/view_children.html", {'children': Student.objects.filter(guardian=request.user)})


class AddChild(CreateView):
    model = Student
    fields = ["name", "pronouns", "allergies"]
    template_name = "guardian/add_child.html"
    success_url = reverse_lazy("guardian:children")

    def form_valid(self, form):
        form.instance.guardian = self.request.user
        return super().form_valid(form)


class RegisterForProgram(CreateView):
    model = ProgramRegistration
    form_class = ProgramRegistrationForm
    template_name = "guardian/register_for_program.html"
    success_url = reverse_lazy("guardian:programs")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_children'] = Student.objects.filter(guardian=self.request.user)
        return context

    def form_valid(self, form):
        form.instance.save()
        form.instance.students.set(self.request.POST.getlist("students"))
        return super().form_valid(form)
