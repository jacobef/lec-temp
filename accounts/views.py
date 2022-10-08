from django.shortcuts import render
import django.contrib.auth.views as base_auth_views

# Create your views here.
class LoginView(base_auth_views.LoginView):
    template_name = "accounts/login.html"
