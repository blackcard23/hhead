from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth import login, logout

from accounts.forms import RegisterForm


class UserLoginView(LoginView):
    template_name = 'auth/login.html'

    def get_success_url(self):
        return reverse_lazy('main')


class UserRegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'auth/register.html'

    def get_success_url(self):
        return reverse_lazy('main')

    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.save()
        login(self.request, user)
        return response


def user_logout(request):
    logout(request)
    return redirect('login')
