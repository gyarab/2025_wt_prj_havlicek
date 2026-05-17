from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("api-playground/", views.api_playground, name="api_playground"),
    path("races/", views.races, name="races"),
    path("runners/", views.runners, name="runners"),
    path("results/", views.results, name="results"),
]
