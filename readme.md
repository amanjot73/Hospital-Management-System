# 🏥 Hospital Management System (HMS)

A full-stack **Django-based Hospital Management System** built to streamline hospital workflows including patient management, appointments, prescriptions, billing, and administrative control.

This project demonstrates modular backend architecture, relational database handling, and real-world workflow implementation.

---

## 🚀 Features

### 👤 Patient Module

- Patient registration & login
- Book appointments
- View and download prescriptions
- Access medical history

### 👨‍⚕️ Doctor Module

- View scheduled appointments
- Add and manage prescriptions
- Track patient treatment records

### 🏢 Reception Module

- Monitor total patients and doctors
- View today's appointments
- Manage booking flow

### 💰 Billing & Payments

- Generate bills
- Track payment status
- Maintain transaction records

### 📊 Admin Dashboard

- Total patients count
- Total doctors count
- Total appointments count
- System overview monitoring

---

## 🛠️ Tech Stack

- **Backend:** Django 5.x  
- **Database:** SQLite (Development)  
- **Frontend:** HTML, CSS  
- **Authentication:** Django Authentication System  
- **Version Control:** Git & GitHub  

---

## 🏗️ Project Architecture

### Modular Django Apps

- `accounts`
- `patients`
- `doctors`
- `appointments`
- `billing`
- `Reception`

### Key Backend Concepts Implemented

- Model relationships (ForeignKey, One-to-Many)
- Date-based filtering using Django timezone
- Role-based dashboard separation
- File handling (prescription downloads)
- Clean QuerySet filtering
- Structured URL routing

---

## 📂 Project Structure

```bash
hms/
│
├── accounts/
├── patients/
├── doctors/
├── appointments/
├── billing/
├── Reception/
│
├── templates/
├── static/
├── media/
│
└── manage.py
```
⚙️ Installation
```bash
# Clone repository
git clone <your-repository-url>

# Navigate into project folder
cd hms

# Create virtual environment
python -m venv venv

# Activate virtual environment (Windows)
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Run development server
python manage.py runserver
```
## 👨‍💻 Author

Amanjot Singh
B.Tech CSE | Backend Developer
Passionate about building scalable backend systems and solving real-world logic problems.
## Show some love
⭐ If you found this project useful, consider giving it a star!

