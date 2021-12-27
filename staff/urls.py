from django.contrib import admin
from django.urls import re_path, path
from .views import *


app_name = 'staff'
urlpatterns = [
    path('post_list_by_department/', post_list_by_department, name='post_list_by_department'),
    path('post_employees/', post_employees, name='post_employees'),
    path('employees_detail/', employees_detail, name='employees_detail'),
    path('create_department/', create_department, name='create_department'),
    path('create_post/', create_post, name='create_post'),
    path('create_employees/', create_employees, name='create_employees'),
    path('edit_employees/', edit_employees, name='edit_employees'),
    path('edit_employees_detail/', edit_employees, name='edit_employees_detail'),
    path('delete_department/', delete_department, name='delete_department'),
    path('delete_post/', delete_post, name='delete_post'),
    path('delete_employees/', delete_employees, name='delete_employees'),
]