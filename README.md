# Event Management Multimedia Database API

This project is a **FastAPI-based RESTful API** for managing event data and multimedia assets, including events, venues, attendees, bookings, event posters, promotional videos, and venue photos, using a **MongoDB Atlas** database.

The project was developed as part of the **Database Essentials (ITMSD-506-2301)** unit at MCAST.

---

## Task 1

### Technologies Used

- **Python 3.11**
- **FastAPI** – High-performance REST API framework
- **Uvicorn** – ASGI server for running FastAPI
- **Motor** – Asynchronous MongoDB driver
- **Pydantic** – Data validation and schema enforcement
- **Python-Dotenv** – Secure environment variable management
- **Python-Multipart** – Handling file uploads via Postman
- **MongoDB Atlas** – Cloud-based NoSQL database
- **Postman** – API testing tool
- **VS Code** – Development environment
- **Git** – Version control system

### How I Set Up the Environment

This section outlines how the development environment was set up for this project.

#### 1. Created a Project Folder
A project folder was created to store all API source files and configuration files.

#### 2. Opened VS Code
The project folder was opened in Visual Studio Code, which was used as the main development environment.

#### 3. Created a Virtual Environment
The following command was executed in the VS Code terminal:

```bash
python -m venv .venv
```

#### 4. Activated the Virtual Environment

```bash
.venv\Scripts\activate
```

#### 5. Installed Required Dependencies

```bash
pip install fastapi uvicorn motor pydantic python-dotenv python-multipart requests
```

#### 6. Created requirements.txt

```bash
pip freeze > requirements.txt
```

#### 7. Created Main Application File

`main.py` – contains all FastAPI routes and MongoDB logic.

---

