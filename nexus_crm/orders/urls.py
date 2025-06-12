
from django.urls import path

from . import views

app_name = "orders"

urlpatterns = [
    path('dashboard/', views.DashBoard.as_view(), name='dashboard' ),
    path('order/', views.DashBoardOrdersView.as_view(), name='order' ),
    path('tasks/', views.DashBoardTasksView.as_view(), name='tasks' ),
    path('new_order/', views.DashBoardAddOrderView.as_view(), name='new_order' ),
    path('delete/<int:pk>', views.DashboardDeleteView.as_view(), name='delete_order' ),
    path('add_service_ajax/', views.ServiceAddView.as_view(), name='add_service_ajax'),

    path('order_card/<int:pk>/', views.OrderDetailCartView.as_view(), name='order_card'),
    path('order/<int:pk>/update_costs/', views.UpdateOrderCostsView.as_view(), name='update_order_costs'),
    path('order/<int:pk>/files/', views.OrderFilesView.as_view(), name='order_files'),
    path('order/<int:pk>/edit/', views.EditOrderView.as_view(), name='edit_order'),
    path('edit_address/<int:pk>/', views.EditOrderAddressView.as_view(), name='edit_order_address'),

    path('order/<int:pk>/files/', views.OrderFilesView.as_view(), name='order_files'),
    path('order/<int:order_pk>/files/delete/<int:pk>/', views.OrderFileDeleteView.as_view(), name='order_file_delete'),

    path("service-request-detail/<int:service_request_id>/",views.ServiceRequestDetailView.as_view(),name="service_request_detail"),

]
