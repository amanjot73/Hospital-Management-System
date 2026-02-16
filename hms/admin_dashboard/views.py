from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .models import (
    Patient, Doctor, Department, StaffMember,
    Appointment, BillingRecord, InventoryItem, Report,
)


def home(request):
    from django.db.models import Sum
    
    patients_count = Patient.objects.count()
    doctors_count = Doctor.objects.count()
    appts_count = Appointment.objects.count()
    departments_count = Department.objects.count()
    staff_count = StaffMember.objects.count()
    inventory_count = InventoryItem.objects.count()
    reports_count = Report.objects.count()
    
    # Calculate billing totals
    total_billing = BillingRecord.objects.aggregate(Sum('amount'))['amount__sum'] or 0
    
    # Get recent appointments with status
    recent_appts = Appointment.objects.select_related('patient', 'doctor').order_by('-when')[:6]
    
    # Get top medicines by quantity
    top_medicines = InventoryItem.objects.order_by('-qty')[:5]
    
    ctx = {
        'patients': patients_count,
        'doctors': doctors_count,
        'appts': appts_count,
        'departments': departments_count,
        'staff': staff_count,
        'bills': BillingRecord.objects.count(),
        'inv': inventory_count,
        'reports': reports_count,
        'total_billing': total_billing,
        'recent_appts': recent_appts,
        'top_medicines': top_medicines,
    }
    return render(request, 'admin_dashboard/home.html', ctx)


class PtList(ListView):
    model = Patient
    template_name = 'admin_dashboard/list.html'
    context_object_name = 'objs'

    def get_context_data(self, **kw):
        ctx = super().get_context_data(**kw)
        ctx.update({
            'title': 'Patients',
            'singular': 'Patient',
            'add_url': 'admin_dashboard:pt_add',
            'edit_name': 'admin_dashboard:pt_edit',
            'del_name': 'admin_dashboard:pt_del',
        })
        return ctx


class PtCreate(CreateView):
    model = Patient
    fields = ['first_name', 'last_name', 'dob', 'phone', 'email']
    template_name = 'admin_dashboard/form.html'
    success_url = reverse_lazy('admin_dashboard:pt')


class PtUpdate(UpdateView):
    model = Patient
    fields = ['first_name', 'last_name', 'dob', 'phone', 'email']
    template_name = 'admin_dashboard/form.html'
    success_url = reverse_lazy('admin_dashboard:pt')


class PtDelete(DeleteView):
    model = Patient
    template_name = 'admin_dashboard/confirm_delete.html'
    success_url = reverse_lazy('admin_dashboard:pt')

class DrList(ListView):
    model = Doctor
    template_name = 'admin_dashboard/list.html'
    context_object_name = 'objs'

    def get_context_data(self, **kw):
        ctx = super().get_context_data(**kw)
        ctx.update({
            'title': 'Doctors',
            'singular': 'Doctor',
            'add_url': 'admin_dashboard:dr_add',
            'edit_name': 'admin_dashboard:dr_edit',
            'del_name': 'admin_dashboard:dr_del',
        })
        return ctx


class DrCreate(CreateView):
    model = Doctor
    fields = ['first_name', 'last_name', 'specialty', 'dept', 'phone', 'email']
    template_name = 'admin_dashboard/form.html'
    success_url = reverse_lazy('admin_dashboard:dr')


class DrUpdate(UpdateView):
    model = Doctor
    fields = ['first_name', 'last_name', 'specialty', 'dept', 'phone', 'email']
    template_name = 'admin_dashboard/form.html'
    success_url = reverse_lazy('admin_dashboard:dr')


class DrDelete(DeleteView):
    model = Doctor
    template_name = 'admin_dashboard/confirm_delete.html'
    success_url = reverse_lazy('admin_dashboard:dr')

class ApptList(ListView):
    model = Appointment
    template_name = 'admin_dashboard/list.html'
    context_object_name = 'objs'

    def get_context_data(self, **kw):
        ctx = super().get_context_data(**kw)
        ctx.update({
            'title': 'Appointments',
            'singular': 'Appointment',
            'add_url': 'admin_dashboard:ap_add',
            'edit_name': 'admin_dashboard:ap_edit',
            'del_name': 'admin_dashboard:ap_del',
        })
        return ctx


class ApptCreate(CreateView):
    model = Appointment
    fields = ['patient', 'doctor', 'when', 'status', 'note']
    template_name = 'admin_dashboard/form.html'
    success_url = reverse_lazy('admin_dashboard:ap')


class ApptUpdate(UpdateView):
    model = Appointment
    fields = ['patient', 'doctor', 'when', 'status', 'note']
    template_name = 'admin_dashboard/form.html'
    success_url = reverse_lazy('admin_dashboard:ap')


class ApptDelete(DeleteView):
    model = Appointment
    template_name = 'admin_dashboard/confirm_delete.html'
    success_url = reverse_lazy('admin_dashboard:ap')

class DepList(ListView):
    model = Department
    template_name = 'admin_dashboard/list.html'
    context_object_name = 'objs'

    def get_context_data(self, **kw):
        ctx = super().get_context_data(**kw)
        ctx.update({'title': 'Departments', 'singular': 'Department'})
        return ctx


class StfList(ListView):
    model = StaffMember
    template_name = 'admin_dashboard/list.html'
    context_object_name = 'objs'

    def get_context_data(self, **kw):
        ctx = super().get_context_data(**kw)
        ctx.update({'title': 'Staff', 'singular': 'Staff member'})
        return ctx


class BillList(ListView):
    model = BillingRecord
    template_name = 'admin_dashboard/list.html'
    context_object_name = 'objs'

    def get_context_data(self, **kw):
        ctx = super().get_context_data(**kw)
        ctx.update({'title': 'Billing', 'singular': 'Billing record'})
        return ctx


class InvList(ListView):
    model = InventoryItem
    template_name = 'admin_dashboard/list.html'
    context_object_name = 'objs'

    def get_context_data(self, **kw):
        ctx = super().get_context_data(**kw)
        ctx.update({'title': 'Inventory', 'singular': 'Inventory item'})
        return ctx


class RepList(ListView):
    model = Report
    template_name = 'admin_dashboard/list.html'
    context_object_name = 'objs'

    def get_context_data(self, **kw):
        ctx = super().get_context_data(**kw)
        ctx.update({'title': 'Reports', 'singular': 'Report'})
        return ctx
