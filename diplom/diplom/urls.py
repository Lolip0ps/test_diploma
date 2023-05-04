from django.urls import path, include
from hello import views

urlpatterns = [
    path("set", views.set),
    path("get", views.get),
]
