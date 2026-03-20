from django.contrib import admin
from .models import Runner, Race, Result

@admin.register(Runner)
class RunnerAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "birth_date", "club")
    search_fields = ("first_name", "last_name", "club")
    list_filter = ("club",)

@admin.register(Race)
class RaceAdmin(admin.ModelAdmin):
    list_display = ("name", "date", "location", "distance_m")
    search_fields = ("name", "location")
    list_filter = ("date",)

@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ("runner", "race", "time_seconds", "position")
    list_filter = ("race",)