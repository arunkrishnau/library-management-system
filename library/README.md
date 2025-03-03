Library Management System API

This is a Django REST Framework-based Library Management System where users can search and borrow books, and administrators can manage the system.

 Features
	•	Anonymous Users: Can browse books.
	•	Registered Users: Can search and borrow books.
	•	Administrators: Can add, edit, and delete books.
	•	JWT Authentication for secure access.
	•	Swagger UI Documentation for easy API testing.

Installation:

1. Clone the repository: 
2. Create virtual environment and activate it: python -m venv venv
   On windows: venv\Scripts\activate
   On Mac/Linux: source venv/bin/activate
3. Install dependencies: pip install -r requirements.txt
4. Apply database migrations: python manage.py migrate
5. Create a superuser(for admin access): python manage.py createsuperuser
#Follow the instructions to set a username, email, and a password.

Running the server
Start the Django server: python manage.py runserver

API Endpoints

Authentication
	•	POST /api/token/ → Get JWT access and refresh token.
	•	POST /api/token/refresh/ → Refresh access token.

 Books API
	•	GET /api/books/ → Get the list of available books.
	•	POST /api/books/ → Add a new book (Admin only).

Borrow API
	•	POST /api/borrow/ → Borrow a book (Authenticated users only).

API Documentation(Swagger)
once the server is running, open [Swagger UI](http://127.0.0.1:8000/swagger/)

Running Tests.
To run unit test: python manage.py test

Deployment (Optional)
To deploy the app on Heroku: heroku create library-api
                             git push heroku main
                             heroku run python manage.py migrate

Technologies Used
	•	Django (Backend Framework)
	•	Django REST Framework (API Development)
	•	PostgreSQL (Database)
	•	JWT (Authentication)
	•	Swagger (API Documentation)

Contact

For any questions, feel free to reach out:
📧 mailme.arunkrishna@gmail.com
🔗 GitHub: Your GitHub Username