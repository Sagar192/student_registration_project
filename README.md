# student_registration_project
🏫 Student Registration, Admission & Fee Management System (Django)
A Django-based web application to manage student admissions, course details, and fee payment tracking for educational institutions.
🚀 Features
•	🧑🎓 Add & manage student details
•	📚 Handle student course admissions
•	💵 Record and track fee payments
•	📊 Generate student-wise fee reports
•	🔄 Update student and admission info
•	🗑️ Delete admission records
•	📄 Admin messages and validations
________________________________________
🏗️ Tech Stack
•	Backend: Django (Python)
•	Frontend: HTML (Django Templates), Bootstrap (optional)
•	Database: SQLite (default, can be switched to PostgreSQL, MySQL, etc.)
________________________________________
📂 Project Structure (Simplified)
student_project/
│
├── student_details/       # App folder
│   ├── models.py          # Models for Students, Admissions, FeePaid
│   ├── views.py           # Views for forms, reports, CRUD, etc.
│   ├── forms.py           # Django ModelForms
│   ├── templates/         # HTML templates
│   └── urls.py            # App-level routing
│
├── manage.py
├── db.sqlite3
└── requirements.txt
________________________________________
⚙️ Setup Instructions
1. Create and activate a virtual environment
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate

2. Create project
django-admin startproject studentregistration


3. Install dependencies
pip install -r requirements.txt
4. Run migrations
python manage.py makemigrations
python manage.py migrate
5. Create a superuser (optional for admin panel)
python manage.py createsuperuser
6. Run the server
python manage.py runserver
Now open your browser and go to: http://127.0.0.1:8000
________________________________________
🧾 Functionality Overview
Feature	URL	View
Home Page	/	home
Add Student	/students/new/	CreateNewStudent
Add Admission	/admissions/new/	CreateAdmission
Add Fee Payment	/students/<student_id>/add-fee/	FeePaidCreateView
View Admission List	/admissions/	AdmissionListView
View Student Details	/students/<pk>/	StudentDetailView
View Fee Report	/admissions/<pk>/report/	StudentPaymentDetailView
Update Student + Admission	/students/<pk>/update/	UpdateDetailsView
Delete Admission	/admissions/<pk>/delete/	AdmissionDeleteView
Note: You’ll need to configure your urls.py accordingly for these routes.
________________________________________
🧪 Testing & Development
To test features:
•	Use Django's built-in development server
•	Add test data through forms or Django admin
•	Check console/log for validation messages and success outputs
________________________________________
📌 Future Improvements
•	Add authentication & permissions
•	Export reports as PDF or Excel
•	Add pagination to admission list
•	Improve UI with Bootstrap or Tailwind
•	REST API using Django REST Framework
________________________________________________________________________________

