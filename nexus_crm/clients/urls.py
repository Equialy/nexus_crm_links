from django.urls import path

from . import views

app_name = "clients"

urlpatterns = [
    path('add_client_ajax/', views.ClientAddView.as_view(), name='add_client_ajax'),
]