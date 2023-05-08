from django.shortcuts import render
from .forms import UserForm
from django.http import HttpResponse, JsonResponse


def index(request):
    userform = UserForm()
    return render(request, "index.html", {"form": userform})


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")
