from django import forms
from .models import Resume, Vacancy


class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = [
            'nazvanie_vakansii', 'imya', 'familiya', 'otchestvo', 'data_rozhdeniya', 'email', 'navyki', 'opyt', 'obrazovanie'
        ]


class VacancyForm(forms.ModelForm):
    class Meta:
        model = Vacancy
        fields = [
            'nazvanie', 'nazvanie_kompanii', 'zarplata', 'trebovanie_navyki', 'obyazannosti', 'adres'
        ]

