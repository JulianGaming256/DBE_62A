import os
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from dotenv import load_dotenv
import motor.motor_asyncio
import io
# Load environment variables from .env file
load_dotenv()
app = FastAPI()
# Connect to MongoDB Atlas
client = motor.motor_asyncio.AsyncIOMotorClient(os.getenv("MONGO_URI"))
db = client.event_management_db
# Data Models
class Event(BaseModel):
    name: str
    description: str
    date: str
    venue_id: str
    max_attendees: int
class Attendee(BaseModel):
    name: str
    email: str
    phone: Optional[str] = None
class Venue(BaseModel):
    name: str
    address: str
    capacity: int
class Booking(BaseModel):
    event_id: str
    attendee_id: str
    ticket_type: str
    quantity: int
# Event Endpoints
@app.post("/events")
async def create_event(event: Event):
    event_doc = event.dict()
    result = await db.events.insert_one(event_doc)
    return {"message": "Event created", "id": str(result.inserted_id)}
@app.get("/events")
async def get_events():
    events = await db.events.find().to_list(100)
    for event in events:
        event["_id"] = str(event["_id"])
    return events
# Venue Endpoints
@app.post("/venues")
async def create_venue(venue: Venue):
    venue_doc = venue.dict()
    result = await db.venues.insert_one(venue_doc)
    return {"message": "Venue created", "id": str(result.inserted_id)}
@app.get("/venues")
async def get_venues():
    venues = await db.venues.find().to_list(100)
    for venue in venues:
        venue["_id"] = str(venue["_id"])
    return venues
# Attendee Endpoints
@app.post("/attendees")
async def create_attendee(attendee: Attendee):
    attendee_doc = attendee.dict()
    result = await db.attendees.insert_one(attendee_doc)
    return {"message": "Attendee created", "id": str(result.inserted_id)}
@app.get("/attendees")
async def get_attendees():
    attendees = await db.attendees.find().to_list(100)
    for attendee in attendees:
        attendee["_id"] = str(attendee["_id"])
    return attendees
# Booking Endpoints
@app.post("/bookings")
async def create_booking(booking: Booking):
    booking_doc = booking.dict()
    result = await db.bookings.insert_one(booking_doc)
    return {"message": "Booking created", "id": str(result.inserted_id)}
@app.get("/bookings")
async def get_bookings():
    bookings = await db.bookings.find().to_list(100)
    for booking in bookings:
        booking["_id"] = str(booking["_id"])
    return bookings

# Upload Event Poster (Image)
@app.post("/upload_event_poster/{event_id}")
async def upload_event_poster(event_id: str, file: UploadFile = File(...)):
    content = await file.read()
    poster_doc = {
        "event_id": event_id,
        "filename": file.filename,
        "content_type": file.content_type,
        "content": content,
        "uploaded_at": datetime.utcnow()
    }
    result = await db.event_posters.insert_one(poster_doc)
    return {"message": "Event poster uploaded", "id": str(result.inserted_id)}

# Upload Venue Photo (Image)
@app.post("/upload_venue_photo/{venue_id}")
async def upload_venue_photo(venue_id: str, file: UploadFile = File(...)):
    content = await file.read()
    poster_doc = {
        "venue_id": venue_id,
        "filename": file.filename,
        "content_type": file.content_type,
        "content": content,
        "uploaded_at": datetime.utcnow()
    }
    result = await db.venue_photos.insert_one(poster_doc)
    return {"message": "Venue photo uploaded", "id": str(result.inserted_id)}

# Upload Promo Video (Video)
@app.post("/upload_promo_videos/{event_id}")
async def upload_promo_videos(event_id: str, file: UploadFile = File(...)):
    content = await file.read()
    poster_doc = {
        "event_id": event_id,
        "filename": file.filename,
        "content_type": file.content_type,
        "content": content,
        "uploaded_at": datetime.utcnow()
    }
    result = await db.promo_videos.insert_one(poster_doc)
    return {"message": "Promo video uploaded", "id": str(result.inserted_id)}