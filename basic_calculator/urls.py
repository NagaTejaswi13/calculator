from django.urls import path
from . import views

urlpatterns  = [
    path("index/", views.index, name = "index"),
    path("basic_calci/", views.basic_calci, name = "basic_calci"),
    path("scientific_calci/", views.scientific_calci, name = "scientific_calci")
]   