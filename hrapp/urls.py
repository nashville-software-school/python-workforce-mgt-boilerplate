from django.urls import path

from hrapp import views
from . import views

app_name = 'hrapp'
urlpatterns = [
    path('', views.home, name='home'),
    path('employees/', views.employee_list, name='employee_list'),
]
