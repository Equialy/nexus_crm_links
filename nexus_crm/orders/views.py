from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView


# Create your views here.


class DashBoard(LoginRequiredMixin, TemplateView):
    template_name = "base/dashboard.html"
    extra_context = {'title': 'Главная страница'}


class DashBoardOrdersView(LoginRequiredMixin, View):
    pass


class DashBoardTasksView(LoginRequiredMixin, View):
    pass


class DashBoardAddOrderView(LoginRequiredMixin, View):
    pass
