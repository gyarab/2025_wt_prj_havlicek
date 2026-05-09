from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import RaceForm, ResultForm, RunnerForm
from .models import Race, Result, Runner


def home(request):
    context = {
        "race_count": Race.objects.count(),
        "runner_count": Runner.objects.count(),
        "result_count": Result.objects.count(),
        "latest_races": Race.objects.order_by("-date")[:3],
        "latest_results": Result.objects.select_related("runner", "race").order_by("-id")[:5],
    }
    return render(request, "app/home.html", context)


def about(request):
    return render(request, "app/about.html")


def races(request):
    if request.method == "POST":
        form = RaceForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Beh byl pridan.")
            return redirect("races")
    else:
        form = RaceForm()

    all_races = Race.objects.order_by("-date")
    return render(request, "app/races.html", {"races": all_races, "form": form})


def runners(request):
    if request.method == "POST":
        form = RunnerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Bezec byl pridan.")
            return redirect("runners")
    else:
        form = RunnerForm()

    all_runners = Runner.objects.order_by("last_name", "first_name")
    return render(request, "app/runners.html", {"runners": all_runners, "form": form})


def results(request):
    if request.method == "POST":
        form = ResultForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Vysledek byl pridan.")
            return redirect("results")
    else:
        form = ResultForm()

    all_results = Result.objects.select_related("runner", "race").order_by("race__date", "position")
    return render(request, "app/results.html", {"results": all_results, "form": form})
