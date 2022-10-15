from django.http import HttpResponse
from django.urls import path
from org_admin import views

urlpatterns = [
    path('programs/', lambda request: HttpResponse("not implemented"))
]
