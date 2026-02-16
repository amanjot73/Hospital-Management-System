#!/usr/bin/env python
"""
Quick setup script to create superuser and sample data
Run with: python setup_admin.py
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hms.settings')
django.setup()

from django.contrib.auth.models import User
from admin_dashboard.models import Patient, Doctor, Department, StaffMember, Appointment, InventoryItem, BillingRecord
from datetime import datetime, timedelta

print("=" * 60)
print("HOSPITAL MANAGEMENT SYSTEM - SETUP")
print("=" * 60)

# Create Superuser
print("\n[1/3] Creating Superuser...")
username = 'admin'
email = 'admin@hospital.com'
password = 'Admin@12345'

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username, email, password)
    print(f"✓ Superuser created!")
    print(f"  Username: {username}")
    print(f"  Email: {email}")
    print(f"  Password: {password}")
else:
    print(f"✓ Superuser '{username}' already exists!")

# Create sample departments
print("\n[2/3] Creating sample data...")
departments_data = [
    ('Cardiology', 'CARD'),
    ('Neurology', 'NEUR'),
    ('Orthopedics', 'ORTH'),
    ('Pediatrics', 'PEDI'),
]

for name, code in departments_data:
    Department.objects.get_or_create(name=name, defaults={'code': code})

print(f"✓ Departments: {Department.objects.count()}")

# Create sample doctors
doctors_data = [
    ('Sarah', 'Smith', 'Cardiology'),
    ('John', 'Khan', 'Neurology'),
    ('Emily', 'Davis', 'Orthopedics'),
]

for first, last, specialty in doctors_data:
    dept = Department.objects.filter(name=specialty).first()
    Doctor.objects.get_or_create(
        first_name=first,
        last_name=last,
        defaults={'specialty': specialty, 'dept': dept}
    )

print(f"✓ Doctors: {Doctor.objects.count()}")

# Create sample staff
staff_data = [
    ('John Doe', 'Nurse'),
    ('Mary Johnson', 'Receptionist'),
    ('Michael Brown', 'Lab Technician'),
]

for name, role in staff_data:
    StaffMember.objects.get_or_create(name=name, defaults={'role': role})

print(f"✓ Staff: {StaffMember.objects.count()}")

# Create sample patients
patients_data = [
    ('John', 'Doe'),
    ('Mary', 'Johnson'),
    ('Michael', 'Brown'),
    ('Sarah', 'Williams'),
    ('James', 'Taylor'),
]

for first, last in patients_data:
    Patient.objects.get_or_create(first_name=first, last_name=last)

print(f"✓ Patients: {Patient.objects.count()}")

# Create sample inventory items
medicines_data = [
    ('Paracetamol', 500, 5.00),
    ('Ibuprofen', 350, 3.50),
    ('Amoxicillin', 200, 8.00),
    ('Aspirin', 400, 2.50),
    ('Antibiotics', 150, 12.00),
]

for name, qty, price in medicines_data:
    InventoryItem.objects.get_or_create(
        name=name,
        defaults={'qty': qty, 'unit_price': price}
    )

print(f"✓ Medicines: {InventoryItem.objects.count()}")

# Create sample appointments
patients = Patient.objects.all()
doctors_list = Doctor.objects.all()
now = datetime.now()

statuses = ['sch', 'done', 'cxl']
for i, patient in enumerate(patients[:3]):
    doctor = doctors_list[i % len(doctors_list)] if doctors_list else None
    Appointment.objects.get_or_create(
        patient=patient,
        when=now - timedelta(days=i),
        defaults={
            'doctor': doctor,
            'status': statuses[i % len(statuses)],
            'note': f'Appointment for {patient}'
        }
    )

print(f"✓ Appointments: {Appointment.objects.count()}")

# Create sample billing records
for patient in patients[:3]:
    BillingRecord.objects.get_or_create(
        patient=patient,
        defaults={'amount': 150.00 + (patient.id * 50), 'paid': False}
    )

print(f"✓ Billing Records: {BillingRecord.objects.count()}")

print("\n" + "=" * 60)
print("SETUP COMPLETE!")
print("=" * 60)
print("\nAdmin Panel Access:")
print(f"URL: http://localhost:8000/admin/")
print(f"Username: {username}")
print(f"Password: {password}")
print("\nDashboard:")
print("URL: http://localhost:8000/dashboard/")
print("=" * 60)
