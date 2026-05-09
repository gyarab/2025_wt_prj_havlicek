from datetime import date
from typing import List, Optional

from django.shortcuts import get_object_or_404
from ninja import NinjaAPI, Schema

from .models import Race, Result, Runner


api = NinjaAPI()


class RunnerIn(Schema):
    first_name: str
    last_name: str
    birth_date: Optional[date] = None
    club: str = ""


class RunnerOut(RunnerIn):
    id: int


class RaceIn(Schema):
    name: str
    date: date
    location: str
    distance_m: int


class RaceOut(RaceIn):
    id: int


class ResultIn(Schema):
    runner_id: int
    race_id: int
    time_seconds: float
    position: Optional[int] = None


class ResultOut(ResultIn):
    id: int


@api.get("/runner", response=List[RunnerOut])
def list_runners(request):
    return Runner.objects.all()


@api.get("/runner/{runner_id}", response=RunnerOut)
def get_runner(request, runner_id: int):
    return get_object_or_404(Runner, id=runner_id)


@api.post("/runner", response={201: RunnerOut})
def create_runner(request, payload: RunnerIn):
    runner = Runner.objects.create(**payload.model_dump())
    return 201, runner


@api.put("/runner/{runner_id}", response=RunnerOut)
def update_runner(request, runner_id: int, payload: RunnerIn):
    runner = get_object_or_404(Runner, id=runner_id)
    for attr, value in payload.model_dump().items():
        setattr(runner, attr, value)
    runner.save()
    return runner


@api.get("/race", response=List[RaceOut])
def list_races(request):
    return Race.objects.all()


@api.get("/race/{race_id}", response=RaceOut)
def get_race(request, race_id: int):
    return get_object_or_404(Race, id=race_id)


@api.post("/race", response={201: RaceOut})
def create_race(request, payload: RaceIn):
    race = Race.objects.create(**payload.model_dump())
    return 201, race


@api.put("/race/{race_id}", response=RaceOut)
def update_race(request, race_id: int, payload: RaceIn):
    race = get_object_or_404(Race, id=race_id)
    for attr, value in payload.model_dump().items():
        setattr(race, attr, value)
    race.save()
    return race


@api.get("/result", response=List[ResultOut])
def list_results(request):
    return Result.objects.all()


@api.get("/result/{result_id}", response=ResultOut)
def get_result(request, result_id: int):
    return get_object_or_404(Result, id=result_id)


@api.post("/result", response={201: ResultOut})
def create_result(request, payload: ResultIn):
    result = Result.objects.create(**payload.model_dump())
    return 201, result


@api.put("/result/{result_id}", response=ResultOut)
def update_result(request, result_id: int, payload: ResultIn):
    result = get_object_or_404(Result, id=result_id)
    for attr, value in payload.model_dump().items():
        setattr(result, attr, value)
    result.save()
    return result
