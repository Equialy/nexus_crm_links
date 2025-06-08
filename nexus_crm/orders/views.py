from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse

from clients.forms import ClientForm
from orders.forms import OrderForm, ServiceForm, OrderFileForm, OrderAddressForm
from orders.models import Orders, OrderFile


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


class DashBoardAddOrderView(LoginRequiredMixin, View):
    # {% url 'tasks:my_tasks' %}\
    template_name = 'orders/order_blank.html'
    success_url = reverse_lazy('orders:dashboard')

    def get(self, request, *args, **kwargs):
        """Возвращает формы добавления клиента и сервиса для ajax запроса"""
        form = OrderForm()
        client_form = ClientForm()
        service_form = ServiceForm()

        return render(request, self.template_name,
                      {'form': form, "client_form": client_form, "service_form": service_form, 'title': 'Новая заявка'})

    def post(self, request, *args, **kwargs):
        # Предположим, что вы получаете эти поля из request.POST
        """Созраняет данные клиента и сервиса при отправке их через ajax"""
        form = OrderForm(request.POST)
        client_form = ClientForm(request.POST)
        service_form = ServiceForm(request.POST)

        if form.is_valid():
            order = form.save(commit=False)
            order.manager = request.user
            order.save()
            return redirect('orders:order_card',
                            pk=order.pk)  # При нажатии сохранить перенаправляет на следующую страницу сарточки заявки

        return render(request, self.template_name,
                      {'form': form, "client_form": client_form,
                       "service_form": service_form, "title": "Новая заявка"})


class DashboardDeleteView(LoginRequiredMixin, View):
    model = Orders
    success_url = reverse_lazy('orders:dashboard')

    def post(self, request, pk):
        order = get_object_or_404(Orders, pk=pk)
        # Удаление только своих заявок (если нужно)
        if order.manager == request.user:
            order.delete()

        return redirect('orders:dashboard')


class ServiceAddView(LoginRequiredMixin, View):
    """Добавляет сервис в таблицу service"""
    def post(self, request):
        form = ServiceForm(request.POST)
        if form.is_valid():
            service = form.save()
            return JsonResponse({"id": service.id, "title": service.title})
        return JsonResponse({"errors": form.errors}, status=400)


class OrderDetailCartView(LoginRequiredMixin, DetailView):
    model = Orders
    template_name = "orders/order_card.html"
    context_object_name = 'order'

    def get_context_data(self, **kwargs):
        """Возвращает форму изменения адреся на странице карточи заявки"""
        context = super().get_context_data(**kwargs)
        context['address_form'] = OrderAddressForm(instance=self.object)
        return context


class DashBoardOrdersView(TemplateView):
    pass


class DashBoardTasksView(TemplateView):
    pass


class UpdateOrderCostsView(LoginRequiredMixin, View):
    def post(self, request, pk):
        order = get_object_or_404(Orders, pk=pk)

        # Обновляем себестоимость
        cost_price = request.POST.get('cost_price')
        if cost_price:
            try:
                order.cost_price = float(cost_price)
            except (TypeError, ValueError):
                pass

        # Обновляем общую стоимость
        total_price = request.POST.get('total_price')
        if total_price:
            try:
                order.total_price = float(total_price)
            except (TypeError, ValueError):
                pass

        order.save()
        return redirect('orders:order_card', pk=order.pk)


class EditOrderView(LoginRequiredMixin, UpdateView):
    model = Orders
    form_class = OrderForm
    template_name = 'orders/edit_order.html'

    def get_success_url(self):
        return reverse('orders:order_card', kwargs={'pk': self.object.pk})


class OrderFilesView(LoginRequiredMixin, DetailView):
    model = Orders
    template_name = 'orders/order_files.html'
    context_object_name = 'order'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['file_form'] = OrderFileForm()
        ctx['files'] = self.object.files.all()
        return ctx

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = OrderFileForm(request.POST, request.FILES)
        if form.is_valid():
            file_obj = form.save(commit=False)
            file_obj.order = self.object
            file_obj.save()
        return redirect('orders:order_files', pk=self.object.pk)


class OrderFileDeleteView(LoginRequiredMixin, DeleteView):
    model = OrderFile
    http_method_names = ['post']

    def get_success_url(self):
        order_pk = self.object.order.pk
        return reverse('orders:order_files', kwargs={'pk': order_pk})


class EditOrderAddressView(LoginRequiredMixin, View):
    """Изменияет адрес в таблице orders при нажаитии в ajax запросе сохранить"""
    def post(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        order = get_object_or_404(Orders, pk=pk)
        form = OrderAddressForm(request.POST, instance=order)
        if form.is_valid():
            order = form.save()
            return redirect('orders:order_card', pk=order.pk)

