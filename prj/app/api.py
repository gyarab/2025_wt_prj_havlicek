from datetime import date
from typing import List, Optional

from django.shortcuts import get_object_or_404
from ninja import NinjaAPI, Schema

from .models import Runner


api = NinjaAPI()


class RunnerIn(Schema):
    first_name: str
    last_name: str
    birth_date: Optional[date] = None
    club: str = ""


class RunnerOut(RunnerIn):
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
