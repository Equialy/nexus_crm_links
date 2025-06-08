from django.contrib.auth.views import LogoutView
from django.urls import path

from . import views

app_name = "orders"

urlpatterns = [
    path('dashboard/', views.DashBoard.as_view(), name='dashboard' ),
    path('order/', views.DashBoardOrdersView.as_view(), name='order' ),
    path('tasks/', views.DashBoardTasksView.as_view(), name='tasks' ),
    path('new_order/', views.DashBoardAddOrderView.as_view(), name='new_order' ),

]
