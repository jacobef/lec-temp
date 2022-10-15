from django.http import HttpResponse
from django.urls import path
from guardian import views

app_name = "guardian"

urlpatterns = [
    path('home/', lambda request: HttpResponse("not implemented"), name="home"),
    path('programs/', views.programs, name="programs"),
    path('children/', views.children, name="children"),
    path('children/add/', views.AddChild.as_view(), name="add_child"),
    path('register/', views.RegisterForProgram.as_view(), name="register"),
]
