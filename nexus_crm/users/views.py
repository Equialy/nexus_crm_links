from django.contrib.auth import  login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordContextMixin
from django.views.generic import View, FormView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from django.views.generic import CreateView, UpdateView, TemplateView
from django.contrib import messages

from users.forms import SignUpForm, LoginUserForm, ProfileUserForm, UserPasswordChangeForm, PasswordResetConfirmForm, \
    PasswordResetRequestForm
from users.models import UserProfile
from users.tasks import send_welcome_email, send_password_reset_email


class IndexView(TemplateView):
    template_name = "base/base.html"
    extra_context = {'title': 'Главная страница'}


class SignUpUser(CreateView):
    model = UserProfile
    form_class = SignUpForm
    success_url = reverse_lazy('orders:dashboard')
    template_name = 'users/registration.html'
    extra_context = {'title': 'Регистрация'}
    success_message = "Регистрация прошла успешно!"

    def form_valid(self, form):
        user = form.save()
        self.object = user
        send_welcome_email.delay(user.email, user.username)
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
        return super().form_valid(form)

class ProfileUser(LoginRequiredMixin, UpdateView):
    model = UserProfile
    form_class = ProfileUserForm
    template_name = 'users/profile.html'

    extra_context = {
        'title': 'Профиль пользователя',
    }

    def get_success_url(self):
        return reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user

class PasswordResetInitiateView(LoginRequiredMixin, View):
    """
    По заходу на этот урл шлём письмо на email авторизованного пользователя
    и сразу даём фидбек через messages.
    """
    def get(self, request, *args, **kwargs):
        user = request.user

        # Ставим задачу отправки письма:
        send_password_reset_email.delay(user.email, user.pk)

        # Flash-сообщение:
        messages.success(
            request,
            "Письмо со ссылкой для сброса пароля отправлено на ваш email."
        )
        # Редиректим обратно в профиль (или куда хотите):
        return redirect('users:profile')



def password_reset_confirm(request, user_id, token):
    try:
        # uid = force_str(urlsafe_base64_decode(uidb64)) # Если в базе id user по uid
        user = UserProfile.objects.get(pk=user_id)
    except (TypeError, ValueError, OverflowError, UserProfile.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        if user is not None and default_token_generator.check_token(user, token):
            if request.method == 'POST':
                form = PasswordResetConfirmForm(request.POST, user=user)
                if form.is_valid():
                    form.save()  # установит новый пароль и сохранит user
                    messages.success(request, "Пароль успешно сброшен.")
                    return redirect('users:login')
            else:
                form = PasswordResetConfirmForm(user=user)

            return render(request, 'users/password_reset_confirm.html', {
                'form': form,
                'validlink': True
            })
    else:
        return render(request, 'users/password_reset_confirm.html', {'validlink': False})

class PasswordResetRequestView(FormView):
    """
    Форма «Забыли пароль?»: вводим email, при валидном email
    ставим задачу send_password_reset_email.delay(...)
    """
    template_name = 'users/password_reset_form.html'
    form_class = PasswordResetRequestForm
    success_url = reverse_lazy('users:password_reset_init')

    def form_valid(self, form):
        email = form.cleaned_data['email']
        try:
            user = UserProfile.objects.get(email=email)
        except UserProfile.DoesNotExist:
            messages.info(
                self.request,
                "Если такой email зарегистрирован — на него будет выслана ссылка."
            )
        else:
            # ставим таск
            send_password_reset_email.delay(email, user.pk)
            messages.success(
                self.request,
                "Если такой email зарегистрирован — ссылка для сброса пароля уже в пути."
            )
        return super().form_valid(form)