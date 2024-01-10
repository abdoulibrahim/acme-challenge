from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def index(request):
    return HttpResponse("ZRpqXSsdDCxM0MYGcdUkE2LX-8ChnPufpb2Ob26xHwM.GFomjbTeSiK3n7SwIGo55txIK6VABbji2n2kFcVhIgI")


urlpatterns = [
    path(".well-known/acme-challenge/ZRpqXSsdDCxM0MYGcdUkE2LX-8ChnPufpb2Ob26xHwM", index),
    path("admin/", admin.site.urls),
]
