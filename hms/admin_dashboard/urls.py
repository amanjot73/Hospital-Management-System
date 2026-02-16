from django.urls import path
from . import views

app_name = 'admin_dashboard'

urlpatterns = [
    path('', views.home, name='home'),

    # Patients (pt)
    path('pt/', views.PtList.as_view(), name='pt'),
    path('pt/add/', views.PtCreate.as_view(), name='pt_add'),
    path('pt/<int:pk>/edit/', views.PtUpdate.as_view(), name='pt_edit'),
    path('pt/<int:pk>/del/', views.PtDelete.as_view(), name='pt_del'),

    # Doctors (dr)
    path('dr/', views.DrList.as_view(), name='dr'),
    path('dr/add/', views.DrCreate.as_view(), name='dr_add'),
    path('dr/<int:pk>/edit/', views.DrUpdate.as_view(), name='dr_edit'),
    path('dr/<int:pk>/del/', views.DrDelete.as_view(), name='dr_del'),

    # Appointments (ap)
    path('ap/', views.ApptList.as_view(), name='ap'),
    path('ap/add/', views.ApptCreate.as_view(), name='ap_add'),
    path('ap/<int:pk>/edit/', views.ApptUpdate.as_view(), name='ap_edit'),
    path('ap/<int:pk>/del/', views.ApptDelete.as_view(), name='ap_del'),

    # Other short-named lists
    path('dep/', views.DepList.as_view(), name='dep'),
    path('st/', views.StfList.as_view(), name='st'),
    path('bill/', views.BillList.as_view(), name='bill'),
    path('inv/', views.InvList.as_view(), name='inv'),
    path('rep/', views.RepList.as_view(), name='rep'),
]
