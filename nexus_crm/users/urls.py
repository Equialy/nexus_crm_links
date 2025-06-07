from django.contrib.auth.views import LogoutView
from django.urls import path

from . import views

app_name = "users"

urlpatterns = [
    path('registration/', views.SignUpUser.as_view(), name='registration' ),
    path('', views.LoginUser.as_view(), name='login' ),
    path('logout/', LogoutView.as_view(next_page='filestorage:index'), name='logout'),
    path('profile/', views.ProfileUser.as_view(), name='profile'),
]
