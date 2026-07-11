JobQuest

A backend API for tracking job applications — built with FastAPI and secured with JWT authentication.

Features


🔐 User authentication with JWT (signup, login, protected routes)
📋 Create, view, update, and delete job applications
🗂️ Track application status (applied, interviewing, offered, rejected, etc.)
🛡️ Protected routes only authenticated users can access their own data


Tech Stack


Framework: FastAPI
Language: Python
Auth: JWT (JSON Web Tokens)
Database: SQLite


Project Structure

jobquest/
├── main.py         # App entry point, route registration
├── auth.py         # JWT authentication logic (login, signup, token handling)
├── database.py     # Database connection and CRUD operations
├── models.py       # Database models (tables/schema)
├── schemas.py      # Pydantic schemas for request/response validation
├── jobquest.db     # SQLite database file
└── .gitignore

Getting Started

Prerequisites


Python 3.9+
pip


Installation

bash# Clone the repo
git clone https://github.com/unnatissrivastava/jobquest.git
cd jobquest

# Create a virtual environment
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

# Install dependencies
pip install fastapi uvicorn pyjwt sqlalchemy


Note: Generate a requirements.txt for easier setup by future contributors:

bashpip freeze > requirements.txt

Then this step becomes pip install -r requirements.txt.



Run the app:

bashuvicorn main:app --reload

The API will be available at http://127.0.0.1:8000

Interactive API docs (Swagger UI): http://127.0.0.1:8000/docs

