from django.urls import path
from .views import*

urlpatterns = [
    path('dashboard/', user_dashboard, name='user_dashboard'),
    path('book-appointment/',book_appointment,name='book_appointment'),
]
