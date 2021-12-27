from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import re_path, path
from .views import *

app_name = 'main'
urlpatterns = [
    path('', index, name='index'),
    path('accounts/login/', LoginView.as_view(template_name="auth/login_form.html", success_url='auth/user_profile.html'),  name='login'),
    path('accounts/profile/', profile, name="profile"),
    path('accounts/logout/', LogoutView.as_view(next_page='main:index'), name='logout'),
    path('accounts/register_done/', RegisterDoneView.as_view(), name='register_done'),
    path('accounts/register/', RegisterUserView.as_view(), name='register'),
]
