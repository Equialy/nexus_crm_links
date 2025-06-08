from django.contrib.auth.views import LogoutView
from django.urls import path

from . import views

app_name = "orders"

urlpatterns = [
    path('dashboard/', views.DashBoard.as_view(), name='dashboard' ),
    path('order/', views.DashBoard.as_view(), name='dashboard' ),
    path('tasks/', views.DashBoard.as_view(), name='dashboard' ),
    path('new_order/', views.DashBoard.as_view(), name='dashboard' ),

]
