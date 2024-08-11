from django.shortcuts import redirect
from django.views.generic import CreateView, ListView, DeleteView, DetailView
from django.urls import reverse_lazy
from .models import Resume, Vacancy
from .forms import ResumeForm, VacancyForm


class SozdanieVakansii(CreateView):
    model = Vacancy
    form_class = VacancyForm
    template_name = 'vacancy_form.html'
    success_url = reverse_lazy('spisok_vakansii')

    def form_valid(self, form):
        form.instance.rabotodatel = self.request.user
        return super().form_valid(form)


class SpisokVakansii(ListView):
    model = Vacancy
    template_name = 'vacancy_list.html'
    context_object_name = 'vakansii'

    def get_queryset(self):
        return Vacancy.objects.filter(rabotodatel=self.request.user)


class DetailRezume(DetailView):
    model = Resume
    template_name = 'resume_detail.html'


class DetailVakansii(DetailView):
    model = Vacancy
    template_name = 'vacancy_detail.html'


class UdalenieVakansii(DeleteView):
    model = Vacancy
    template_name = 'vacancy_confirm_delete.html'
    success_url = reverse_lazy('spisok_vakansii')

    def get_object(self, queryset=None):
        obj = Vacancy.objects.get(pk=self.kwargs['pk'])
        if obj.rabotodatel != self.request.user:
            return redirect('spisok_vakansii')
        return obj


class SozdanieRezume(CreateView):
    model = Resume
    form_class = ResumeForm
    template_name = 'resume_form.html'
    success_url = reverse_lazy('spisok_rezume')

    def form_valid(self, form):
        form.instance.polzovatel = self.request.user
        return super().form_valid(form)


class SpisokRezume(ListView):
    model = Resume
    template_name = 'resume_list.html'
    context_object_name = 'rezume'

    def get_queryset(self):
        return Resume.objects.filter(polzovatel=self.request.user)


class UdalenieRezume(DeleteView):
    model = Resume
    template_name = 'resume_confirm_delete.html'
    success_url = reverse_lazy('spisok_rezume')

    def get_object(self, queryset=None):
        obj = Resume.objects.get(pk=self.kwargs['pk'])
        if obj.polzovatel != self.request.user:
            return redirect('spisok_rezume')
        return obj
