from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    # # path('', views.patient_login, name='patient_login'),
    # path('patient_login/',views.patient_login,name = 'patient_login'),
    # path('patient_register/',views.patient_register,name = 'patient_register'),
    # path('temp/',views.temp,name = 'temp'),
    path('pre_doctor/', views.pre_doctor, name='pre_doctor'), 
    path('login_doctor/', views.doctor_login, name='login_doctor'),      # Remove 'accounts/'
    path('register_doctor/', views.doctor_register, name='register_doctor'),  # Remove 'accounts/'
    

]