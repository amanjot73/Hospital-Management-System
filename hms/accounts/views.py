from django.shortcuts import render
from .models import *
from django.conf import settings
from django.core.mail import send_mail

def patient_login(request):
    if request.method == 'POST':
        patient_name = request.POST.get('patient_name')
        patient_password = request.POST.get('patient_password')
        m = patient.objects.filter(
            patient_name = patient_name,
            patient_password = patient_password

        )
        if m.exists():
            return render(request,'accounts/temp.html')
        
            
    return render(request, 'accounts/login_patient.html')

def patient_register(request):
    if request.method == 'POST':
        patient_name = request.POST.get('patient_name')
        patient_age = request.POST.get('patient_age')
        patient_number = request.POST.get('patient_number')
        patient_email = request.POST.get('patient_email')
        patient_password = request.POST.get('patient_password')

        patient.objects.create(
            patient_name=patient_name,
            patient_age=patient_age,
            patient_number=patient_number,
            patient_email=patient_email,
            patient_password=patient_password
        )

        send_mail(
            subject="Welcome to Hospital Management System",
            message=f'Hello {patient_name}, Thanks for registering with us',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[patient_email],
            fail_silently=False
        )
        return render(request,'accounts/temp.html')

    return render(request, 'accounts/register_patient.html')
def doctor_login(request):
    if request.method == 'POST':
        doctor_name = request.POST.get('doctor_name')
        doctor_password = request.POST.get('doctor_password')
        m = doctor.objects.filter(
            doctor_name = doctor_name,
            doctor_password = doctor_password

        )
        if m.exists():
            return render(request,'accounts/temp.html')
        
            
    return render(request, 'accounts/login_doctor.html')

def doctor_register(request):
    if request.method == 'POST':
        doctor_name = request.POST.get('doctor_name')
        doctor_age = request.POST.get('doctor_age')
        doctor_number = request.POST.get('doctor_number')
        doctor_email = request.POST.get('doctor_email')
        doctor_password = request.POST.get('doctor_password')

        doctor.objects.create(
            doctor_name=doctor_name,
            doctor_age=doctor_age,
            doctor_number=doctor_number,
            doctor_email=doctor_email,
            doctor_password=doctor_password
        )

        send_mail(
            subject="Welcome to Hospital Management System",
            message=f'Hello Dr. {doctor_name}, Thanks for registering with us',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[doctor_email],
            fail_silently=False
        )
        return render(request,'accounts/temp.html')

    return render(request, 'accounts/register_doctor.html')

def temp(request):
    return render(request,'accounts/temp.html')
