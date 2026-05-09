from django import forms

from .models import Race, Result, Runner


class DateInput(forms.DateInput):
    input_type = "date"


class RaceForm(forms.ModelForm):
    class Meta:
        model = Race
        fields = ["name", "date", "location", "distance_m"]
        widgets = {
            "date": DateInput(),
        }
        labels = {
            "name": "Název běhu",
            "date": "Datum",
            "location": "Místo",
            "distance_m": "Délka trati (m)",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        apply_form_control_classes(self)


class RunnerForm(forms.ModelForm):
    class Meta:
        model = Runner
        fields = ["first_name", "last_name", "birth_date", "club"]
        widgets = {
            "birth_date": DateInput(),
        }
        labels = {
            "first_name": "Jméno",
            "last_name": "Příjmení",
            "birth_date": "Datum narození",
            "club": "Klub",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        apply_form_control_classes(self)


class ResultForm(forms.ModelForm):
    class Meta:
        model = Result
        fields = ["runner", "race", "time_seconds", "position"]
        labels = {
            "runner": "Běžec",
            "race": "Běh",
            "time_seconds": "Čas (sekundy)",
            "position": "Umístění",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        apply_form_control_classes(self)


def apply_form_control_classes(form):
    for field in form.fields.values():
        if isinstance(field.widget, forms.Select):
            field.widget.attrs["class"] = "form-select"
        else:
            field.widget.attrs["class"] = "form-control"
