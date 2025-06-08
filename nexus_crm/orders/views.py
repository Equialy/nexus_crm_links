from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView
from django.urls import reverse_lazy

from orders.models import Orders


# Create your views here.


class DashBoard(LoginRequiredMixin, TemplateView):
    template_name = "base/dashboard.html"
    extra_context = {'title': 'Главная страница'}

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        # все активные заявки:
        ctx['active_requests'] = Orders.objects.active()
        # только ваши:
        ctx['my_requests'] = Orders.objects.by_manager(self.request.user)
        return ctx


class DashBoardOrdersView(LoginRequiredMixin, View):
    pass


class DashBoardTasksView(LoginRequiredMixin, View):
    pass


class DashBoardAddOrderView(LoginRequiredMixin, View):
    # {% url 'tasks:my_tasks' %}\
    template_name = 'orders/order_blank.html'
    success_url = reverse_lazy('orders:dashboard')

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, { 'title': 'Новая заявка'})


    def post(self, request, *args, **kwargs):
        # Предположим, что вы получаете эти поля из request.POST
        description = request.POST['description']
        address = request.POST.get('address', '')
        cost_price = int(request.POST.get('cost_price', 0))
        total_price = int(request.POST.get('total_price', 0))

        # Создаём заявку через менеджер
        new_order = Orders.objects.create_order(
            manager=request.user,
            address=address,
            description=description,
            cost_price=cost_price,
            total_price=total_price
        )

        # После создания — редиректим на дашборд или детальную страницу
        return redirect('orders:dashboard')

