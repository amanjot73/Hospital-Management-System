from django.shortcuts import*
from accounts.models import*
from django.conf import settings
from django.core.mail import send_mail
# Create your views here.
def reception_dashboard(request):
    return render(request, "Reception/reception_dashboard.html")
def pre_receptionist(request):
    receptionist_id = request.session.get('receptionist_id')
    r = receptionist.objects.get(id = receptionist_id)
    return render(request,'Reception/pre_receptionist.html',{'r':r})

def receptionist_login(request):
    if request.method == 'POST':
        receptionist_name = request.POST.get('receptionist_name')
        receptionist_password = request.POST.get('receptionist_password')
        m = receptionist.objects.filter(
            receptionist_name = receptionist_name,
            receptionist_password = receptionist_password

        ).first()
        if m:
            request.session['receptionist_id'] = m.id
            return redirect('pre_receptionist')
        
            
    return render(request, 'Reception/login_receptionist.html')

def receptionist_register(request):
    if request.method == 'POST':
        receptionist_name = request.POST.get('receptionist_name')
        receptionist_number = request.POST.get('receptionist_number')
        receptionist_email = request.POST.get('receptionist_email')
        receptionist_password = request.POST.get('receptionist_password')

        receptionist.objects.create(
            receptionist_name=receptionist_name,
            # receptionist_otp=receptionist_otp,
            receptionist_number=receptionist_number,
            receptionist_email=receptionist_email,
            receptionist_password=receptionist_password
        )

        send_mail(
            subject="Welcome to Hospital Management System",
            message=f'Hello {receptionist_name}, Thanks for registering with us',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[receptionist_email],
            fail_silently=False
        )
        return redirect('pre_receptionist')

    return render(request, 'Reception/register_receptionist.html')