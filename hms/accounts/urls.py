from django.contrib import admin
# from django.urls import path
# from .import views

from django.urls import path
from . import views

urlpatterns = [
    path('login_patient/', views.patient_login, name='login_patient'),      # Remove 'accounts/'
    path('register_patient/', views.patient_register, name='register_patient'),  # Remove 'accounts/'
    path('login_doctor/', views.doctor_login, name='login_doctor'),      # Remove 'accounts/'
    path('register_doctor/', views.doctor_register, name='register_doctor'),  # Remove 'accounts/'
    path('temp/', views.temp, name='temp'),  # Remove 'accounts/'
]