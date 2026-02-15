from django.urls import path
from . import views

urlpatterns = [
    path("reception-dashboard/", views.reception_dashboard, name="reception_dashboard"),
]
