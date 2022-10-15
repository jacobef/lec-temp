from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView

from guardian.forms import ProgramRegistrationForm
from guardian.models import ProgramRegistration, Student
from org_admin.models import Program


def programs(request):
    return render(request, "guardian/view_programs.html", {'programs': Program.objects.all()})

def children(request):
    return render(request, "guardian/view_children.html", {'children': Student.objects.filter(guardian=request.user)})

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
