from django.shortcuts import render
from appointments.models import Appointment
from django.utils.timezone import now

# Create your views here.
def user_dashboard(request):
    today = now().date()

    today_appointment = Appointment.objects.filter(
        patient=request.user,
        slot__date=today
    ).first()

    return render(request, 'appointment/dashboard.html', {
        'today_appointment': today_appointment
    })