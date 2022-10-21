from django.http import HttpResponse
from django.urls import path
from org_admin import views

app_name = "org_admin"

urlpatterns = [
    path('', lambda request: HttpResponse("not implemented"), name="home"),
    path('programs/', views.programs, name="programs"),
    path('programs/add/', views.AddProgram.as_view(), name="add_program"),
    path('programs/<int:program_pk>/announcements/', views.view_announcements, name="view_announcements"),
    path('programs/<int:program_pk>/announcements/add/', views.MakeAnnouncement.as_view(), name="make_announcement"),
]
