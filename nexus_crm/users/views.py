from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from users.forms import SignUpForm, LoginUserForm, ProfileUserForm


class SignUpUser( CreateView):
    model = get_user_model()
    form_class = SignUpForm
    # success_url = reverse_lazy('filestorage:index')
    template_name = 'register.html'
    extra_context = {'title': 'Регистрация'}
    success_message = "Регистрация прошла успешно!"

class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'registration/login.html'
    # success_url = reverse_lazy("filestorage:index")
    extra_context = {'title': 'Авторизация'}

    def form_valid(self, form):
        print("Форма валидна! Пользователь аутентифицирован.")
        return super().form_valid(form)

class ProfileUser(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    form_class = ProfileUserForm
    template_name = 'profile.html'


    def get_success_url(self):
        return reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user