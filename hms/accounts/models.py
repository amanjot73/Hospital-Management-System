from django.db import models

# Create your models here.
<<<<<<< HEAD
class patient(models.Model):
    patient_name = models.CharField(max_length=20)
    patient_age = models.CharField(max_length=5)
    patient_otp = models.CharField(max_length=10)
    patient_number = models.CharField(max_length=20)
    patient_email = models.EmailField(max_length=20)
    patient_password = models.CharField(max_length=20)
    patient_blood_group = models.CharField(max_length=20)
    patient_gender = models.CharField(max_length=10)
    def __str__(self):
        return self.patient_name
class doctor(models.Model):
    doctor_name = models.CharField(max_length=20)
    doctor_speciality = models.CharField(max_length=20)
    doctor_fee = models.IntegerField()
    doctor_slots = models.IntegerField()
    doctor_otp = models.CharField(max_length=10)
    doctor_number = models.CharField(max_length=20)
    doctor_email = models.EmailField(max_length=20)
    doctor_password = models.CharField(max_length=20)
    def __str__(self):
        return self.doctor_name

class receptionist(models.Model):
    receptionist_name = models.CharField(max_length=20)
    receptionist_number = models.CharField(max_length=20)
    receptionist_email = models.EmailField(max_length=20)
    receptionist_otp = models.CharField(max_length=10)
    receptionist_password = models.CharField(max_length=10)
    
    def __str__(self):
        return self.receptionist_name

=======
>>>>>>> bc332647ca32a1334991bf0e1e0103ca0f1e0e2a
