from django.shortcuts import render
from .models import Runner, Race, Result

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def races(request):
    all_races = Race.objects.all()  # vybere všechny závody z DB
    return render(request, "races.html", {"races": all_races})

def runners(request):
    all_runners = Runner.objects.all()  # vybere všechny běžce
    return render(request, "runners.html", {"runners": all_runners})