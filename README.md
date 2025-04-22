# Nexus LinkSaver
- A full-stack web application built with **Django** for saving and managing user links through CATEGORIES. 
It supports** User Authentication**, allowing users to create accounts, log in, and save links securely. 
The app is deployed on Render with a PostgreSQL database backend.

The app is **deployed on Render**. You can access it at:
https://nexus-linksaver.onrender.com/

---
- # Tech Stack

Backend: Django, Python

Frontend: HTML, CSS/Bootstrap, JavaScript

Database: PostgreSQL

Version Control: Git, GitHub

Deployment: Render (for cloud deployment)

---
- # Setup/Installation

Clone repo:
---
  git clone https://github.com/Bryxel/Nexus-LinkSaver.git

Create & activate a virtual env:
---
  python -m venv venv
  source venv/bin/activate  # On Windows use: venv\Scripts\activate

Install dependencies:
---
  pip install -r requirements.txt

Environment variables Create a .env file in the root:
---
  DATABASE_URL=your_postgres_url
  SECRET_KEY=your_secret_key
  DEBUG=True

Run migrations and Start the server:
---
  python manage.py migrate
  python manage.py runserver






