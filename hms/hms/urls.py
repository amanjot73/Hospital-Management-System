"""
URL configuration for hms project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
<<<<<<< HEAD
from django.urls import path, include  # Make sure 'include' is imported

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),  # Use include()
    path('patients/', include('patients.urls')),  # Assuming you have this
    path('doctors/', include('doctors.urls')),    # Assuming you have this
=======
from django.urls import path,include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('appointments.urls')),
    path('',include('Reception.urls')),

>>>>>>> bc332647ca32a1334991bf0e1e0103ca0f1e0e2a
]
