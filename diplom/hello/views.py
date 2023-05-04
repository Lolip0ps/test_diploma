# from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


def set(request):
    username = request.GET.get("username", "Undefined")
    response = HttpResponse(f"Hello {username}")
    response.set_cookie("username", username)
    return response


def get(request):
    username = request.COOKIES["username"]
    return HttpResponse(f"Hello {username}")


def get(request):
    return False
