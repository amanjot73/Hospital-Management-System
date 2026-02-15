from urllib import request
from django.shortcuts import *

# Create your views here.
def billing(request):
    return render(request,'billing/billing.html')

def billing_history(request):
    return render(request,'billing/billing_history.html')   


