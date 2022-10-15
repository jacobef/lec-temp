from django.http import HttpResponse
from django.urls import path
from guardian import views

urlpatterns = [
    path('programs/', lambda request: HttpResponse("not implemented"))
]
