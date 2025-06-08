from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.views import View

from django.shortcuts import render

from clients.forms import ClientForm


# Create your views here.
class ClientAddView(LoginRequiredMixin, View):
    def post(self, request):
        form = ClientForm(request.POST)
        if form.is_valid():
            client = form.save(commit=False)
            client.manager = request.user
            client.save()
            return JsonResponse({"id": client.id, "name": client.name})
        return JsonResponse({"errors": form.errors}, status=400)
