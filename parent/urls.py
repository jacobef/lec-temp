from django.http import HttpResponse
from django.urls import path
from parent import views

urlpatterns = [
    path('programs/', lambda request: HttpResponse("not implemented"))
]
