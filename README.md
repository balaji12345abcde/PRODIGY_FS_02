👨‍💼 Employee Management System - Django
---------------------------------------

This project is developed as part of Prodigy Infotech Internship - Task 02.
The goal is to build a web-based Employee Management System that allows administrators to perform CRUD (Create, Read, Update, Delete) operations on employee records, with proper authentication and validation.

🚀 Features:
✅ Admin authentication & login/logout
✅ Add new employees (Create)
✅ View employee list/details (Read)
✅ Update employee information (Update)
✅ Delete employee records (Delete)
✅ Secure authentication using Django’s built-in system
✅ Form validation to ensure accurate data entry
✅ Access control (only authenticated users can manage employees)

🛠️ Tech Stack:

Backend: Python, Django

Frontend: HTML, CSS (Django Templates, Bootstrap optional)

Database: SQLite (default, can be changed to MySQL/PostgreSQL)

📂 Project Structure
EmployeeManagement/
│── employees/           # App for employee CRUD operations
│   ├── migrations/
│   ├── templates/       # HTML templates (list, add, edit, delete)
│   ├── views.py         # Employee CRUD logic
│   ├── urls.py          # Routes for employee management
│   └── models.py        # Employee model
│
│── accounts/            # App for authentication (login/logout/signup)
│   ├── templates/
│   ├── views.py
│   ├── urls.py
│   └── models.py
│
│── EmployeeManagement/  # Main project folder
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
└── manage.py

⚙️ Installation & Setup

Clone the Repository

git clone https://github.com/your-username/employee-management-django.git
cd employee-management-django


Create Virtual Environment

python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows


Install Dependencies

pip install -r requirements.txt


Run Migrations

python manage.py migrate


Create Superuser (Admin Panel)

python manage.py createsuperuser


Run Development Server

python manage.py runserver


Open in browser:
👉 http://127.0.0.1:8000/

🔐 Authentication Flow

Only authenticated users (Admin) can add, edit, delete, or view employees.

Employees data is securely stored in the database.

Admin credentials are managed via Django’s authentication system.

📸 Screenshots



📜 License

This project is for educational purposes as part of the Prodigy Infotech Internship.
