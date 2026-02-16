from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .models import Medicine
from .forms import MedicineForm


# ===============================
# Landing Page
# ===============================

def landing_page(request):
    return render(request, 'pharmacy/landing_page.html')


# ===============================
# READ - View All Medicines
# ===============================

def medicine_list(request):
    medicines = Medicine.objects.all()
    return render(request, 'pharmacy/medicine_list.html', {'medicines': medicines})


# ===============================
# CREATE - Add Medicine
# ===============================

def add_medicine(request):
    if request.method == 'POST':
        form = MedicineForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('medicine_list')
    else:
        form = MedicineForm()

    return render(request, 'pharmacy/add_medicine.html', {'form': form})


# ===============================
# UPDATE - Edit Medicine
# ===============================

def update_medicine(request, pk):
    medicine = get_object_or_404(Medicine, pk=pk)

    if request.method == 'POST':
        form = MedicineForm(request.POST, instance=medicine)
        if form.is_valid():
            form.save()
            return redirect('medicine_list')
    else:
        form = MedicineForm(instance=medicine)

    return render(request, 'pharmacy/update_medicine.html', {'form': form})


# ===============================
# DELETE - Delete Medicine
# ===============================

def delete_medicine(request, pk):
    medicine = get_object_or_404(Medicine, pk=pk)

    if request.method == 'POST':
        medicine.delete()
        return redirect('medicine_list')

    return render(request, 'pharmacy/delete_medicine.html', {'medicine': medicine})

