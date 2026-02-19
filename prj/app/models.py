from django.db import models

class Runner(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField(null=True, blank=True)
    club = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Race(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    location = models.CharField(max_length=100)
    distance_m = models.PositiveIntegerField()  # vzdálenost v metrech

    def __str__(self):
        return f"{self.name} ({self.date})"

class Result(models.Model):
    runner = models.ForeignKey(Runner, on_delete=models.CASCADE)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    time_seconds = models.FloatField()  # čas v sekundách
    position = models.PositiveIntegerField(null=True, blank=True)  # pořadí

    def __str__(self):
        return f"{self.runner} – {self.race}: {self.time_seconds}s"
