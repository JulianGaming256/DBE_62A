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

## Task 2

### Schema Design

The MongoDB database schema was designed using **MongoDB Atlas** and **MongoDB Compass**.

The database, named `event_management_db`, contains the following collections:

- **events** – Stores event details such as name, date, venue reference, and maximum attendees
- **venues** – Stores venue information including name, address, and capacity
- **attendees** – Stores attendee contact details
- **bookings** – Stores ticket bookings linked to events and attendees
- **event_posters** – Stores metadata and binary image data for event posters
- **promo_videos** – Stores metadata and binary video data for promotional videos
- **venue_photos** – Stores metadata and binary image data for venue photos

Each multimedia document includes fields such as `filename`, `content_type`, `content`, and `uploaded_at`.

Relationships between collections are maintained using referenced IDs (e.g. `event_id`, `venue_id`).

### Schema Deployment

The schema was deployed on **MongoDB Atlas** using a free-tier cluster.

A database named `event_management_db` was created, and all required collections were manually added.

Mock data was inserted into each collection to validate the schema design:

- Sample events linked to venues
- Sample attendees and bookings
- Example metadata entries for posters, promotional videos, and venue photos

The schema and data were visually verified using **MongoDB Atlas** and **MongoDB Compass**, with screenshots provided as evidence.

---

## Task 3

### Running the API Locally

Once the virtual environment and dependencies were installed, the API was started using:

```bash
uvicorn main:app --reload
```

The API is accessible at:

```
http://127.0.0.1:8000/docs
```

The **Swagger UI** was used to test and verify all endpoints.

### API Endpoints

#### Core Data Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/events` | Create a new event |
| GET | `/events` | Retrieve all events |
| POST | `/venues` | Create a venue |
| GET | `/venues` | Retrieve all venues |
| POST | `/attendees` | Create an attendee |
| GET | `/attendees` | Retrieve all attendees |
| POST | `/bookings` | Create a booking |
| GET | `/bookings` | Retrieve all bookings |

#### Multimedia Upload Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/upload_event_poster/{event_id}` | Upload an event poster image |
| POST | `/upload_promo_videos/{event_id}` | Upload a promotional video |
| POST | `/upload_venue_photo/{venue_id}` | Upload a venue photo |

All multimedia endpoints accept `multipart/form-data` and store files directly in MongoDB as binary data.

### Testing with Postman

- File uploads were tested using `form-data`
- JSON endpoints were tested using raw JSON
- - All endpoints returned confirmation messages and MongoDB document IDs
- Uploaded files were successfully stored and retrieved from MongoDB

### Running the API on Vercel

The FastAPI application was deployed to Vercel using a `vercel.json` configuration file.

Example hosted endpoints:

```
GET  https://<your-vercel-app>.vercel.app/events
POST https://<your-vercel-app>.vercel.app/upload_event_poster/{event_id}
```

