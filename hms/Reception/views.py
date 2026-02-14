from django.shortcuts import render

# Create your views here.
def reception_dashboard(request):
    return render(request, "reception/reception_dashboard.html")
