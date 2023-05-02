from django.urls import path, include
from hello import views

urlpatterns = [
    path("", views.index),
    path("user/", views.user),
]
