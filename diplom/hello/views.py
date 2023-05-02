# from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("<h2>Главная страница</h2>")


def user(request):
    age = request.GET.get("age", 0)
    name = request.GET.get("name", "jopa")
    return HttpResponse(f"<h2>Имя: {name} Возраст: {age}</h2>")
