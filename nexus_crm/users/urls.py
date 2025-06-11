from django.contrib.auth.views import LogoutView
from django.urls import path

from . import views

app_name = "users"

urlpatterns = [
    path('registration/', views.SignUpUser.as_view(), name='registration' ),
    path('', views.IndexView.as_view(), name='index' ),
    path('login/', views.LoginUser.as_view(), name='login' ),
    path('profile/', views.ProfileUser.as_view(), name='profile'),
    path('logout/', LogoutView.as_view(next_page='users:index'), name='logout'),
    path('profile/', views.ProfileUser.as_view(), name='profile'),

    #  Инициация «одно-кликового» сброса пароля:
    path('password-reset-init/', views.PasswordResetInitiateView.as_view(), name='password_reset_init'),
    path('password-reset/<int:user_id>/<str:token>/', views.password_reset_confirm,name='password_reset_confirm'),

    # Сброс пароля на странице логина
    path('password-reset/',views.PasswordResetRequestView.as_view(),name='password_reset'),



]
