from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing'),
    path('medicines/', views.medicine_list, name='medicine_list'),
    path('medicines/add/', views.add_medicine, name='add_medicine'),
    path('medicines/update/<int:pk>/', views.update_medicine, name='update_medicine'),
    path('medicines/delete/<int:pk>/', views.delete_medicine, name='delete_medicine'),
]
