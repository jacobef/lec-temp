from django.shortcuts import render
import django.contrib.auth.views as base_auth_views
from django.urls import reverse_lazy
from django.views.generic import CreateView

from accounts.forms import LECUserCreationForm
from accounts.models import LECUser


def profile(request):
    return render(request, "accounts/profile.html")

class Login(base_auth_views.LoginView):
    template_name = "accounts/login.html"
    success_url = ""

class CreateAccount(CreateView):
    model = LECUser
    form_class = LECUserCreationForm
    template_name = "accounts/create_account.html"
    success_url = reverse_lazy("accounts:account_created")


def account_created(request):
    return render(request, "accounts/account_created.html")
