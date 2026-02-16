from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .models import (
    Patient, Doctor, Department, StaffMember,
    Appointment, BillingRecord, InventoryItem, Report,
)


def home(request):
    """Dashboard home with quick counts and recent appointments."""
    ctx = {
        'patients': Patient.objects.count(),
        'doctors': Doctor.objects.count(),
        'appts': Appointment.objects.count(),
        'departments': Department.objects.count(),
        'staff': StaffMember.objects.count(),
        'bills': BillingRecord.objects.count(),
        'inv': InventoryItem.objects.count(),
        'reports': Report.objects.count(),
        'recent_appts': Appointment.objects.select_related('patient', 'doctor').order_by('-when')[:6],
    }
    return render(request, 'admin_dashboard/home.html', ctx)


# ---- Patients (short name: pt) ----
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


# ---- Doctors (short name: dr) ----
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


# ---- Appointments (short name: ap) ----
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


# ---- Simple lists for other sections (short names: dep, st, bill, inv, rep) ----
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
