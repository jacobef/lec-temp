from django.http import HttpResponse
from django.urls import path
from guardian import views

app_name = "guardian"

urlpatterns = [
    path('programs/', views.programs, name="programs"),
    path('children/', views.children, name="children"),
    path('register/', views.RegisterForProgram.as_view(), name="register"),
]
