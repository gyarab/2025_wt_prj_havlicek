from django.shortcuts import render
from .models import Runner, Race, Result

def home(request):
    return render(request, 'app/home.html')

def about(request):
    return render(request, 'app/about.html')

def races(request):
    all_races = Race.objects.all()  # vybere všechny závody z DB
    return render(request, "app/races.html", {"races": all_races})

def runners(request):
    all_runners = Runner.objects.all()  # vybere všechny běžce
    return render(request, "app/runners.html", {"runners": all_runners})