from django.shortcuts import*

from accounts.models import*
from django.conf import settings
from django.core.mail import send_mail

def pre_doctor(request):
    doctor_id = request.session.get('doctor_id')
    d = doctor.objects.get(id= doctor_id)
    return render(request,'doctors/pre_doctor.html',{'d':d})

def doctor_login(request):
    if request.method == 'POST':
        doctor_name = request.POST.get('doctor_name')
        doctor_password = request.POST.get('doctor_password')
        m = doctor.objects.filter(
            doctor_name = doctor_name,
            doctor_password = doctor_password

        ).first()
        if m:
            request.session['doctor_id'] = m.id
            return redirect('pre_doctor')
        
            
    return render(request, 'doctors/login_doctor.html')

def doctor_register(request):
    if request.method == 'POST':
        doctor_name = request.POST.get('doctor_name')
        doctor_speciality = request.POST.get('doctor_speciality')
        doctor_fee = request.POST.get('doctor_fee')
        doctor_slots = request.POST.get('doctor_slots')
        doctor_number = request.POST.get('doctor_number')
        doctor_email = request.POST.get('doctor_email')
        doctor_password = request.POST.get('doctor_password')

        doctor.objects.create(
            doctor_name=doctor_name,
            doctor_fee=doctor_fee,
            doctor_slots=doctor_slots,
            doctor_speciality=doctor_speciality,
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
        return render(request,'doctors/login_doctor.html')

    return render(request, 'doctors/register_doctor.html')

def doctor_dashboard(request):
    d = request.session.get('doctor_id')
    db = doctor.objects.get(id = d)
    a2 = appointments.objects.filter(doctor = db.doctor_name)
    a = appointments.objects.filter(
        doctor = db.doctor_name
        ).count()
    return render(request,'doctors/doctor_dashboard.html',{'c':a , 'c2':a2})