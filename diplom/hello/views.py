from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from datetime import datetime


def index(request):
    return render(request, "index.html", context={"my_date": datetime.now()})


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")
