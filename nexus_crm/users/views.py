from django.contrib.auth import get_user_model, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, TemplateView

from users.forms import SignUpForm, LoginUserForm, ProfileUserForm
from users.models import UserProfile


class IndexView(TemplateView):
    template_name = "base/base.html"
    extra_context = {'title': 'Главная страница'}


class SignUpUser(CreateView):
    model = UserProfile
    form_class = SignUpForm
    success_url = reverse_lazy('users:index')
    template_name = 'users/registration.html'
    extra_context = {'title': 'Регистрация'}
    success_message = "Регистрация прошла успешно!"

    def form_valid(self, form):
        user = form.save()
        self.object = user
        login(self.request, user)  # Автоматический вход
        return redirect(self.get_success_url())


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'users/login.html'
    extra_context = {'title': 'Авторизация'}

    def get_success_url(self):
        url = self.get_redirect_url()
        if url:
            return url
        return reverse_lazy("orders:dashboard")

    def form_valid(self, form):
        print("Форма валидна! Пользователь аутентифицирован.")
        return super().form_valid(form)


class ProfileUser(LoginRequiredMixin, UpdateView):
    model = UserProfile
    form_class = ProfileUserForm
    template_name = 'profile.html'

    def get_success_url(self):
        return reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user
