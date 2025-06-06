from fastapi import FastAPI, HTTPException, Depends, Query
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import Base, FitnessClass, Booking
from utils import convert_to_timezone
from seed_data import seed_classes
from datetime import datetime
from pydantic import BaseModel, EmailStr

app = FastAPI()
Base.metadata.create_all(bind=engine)
seed_classes()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class BookingRequest(BaseModel):
    class_id: int
    client_name: str
    client_email: EmailStr

@app.get("/classes")
def list_classes(timezone: str = "Asia/Kolkata", db: Session = Depends(get_db)):
    classes = db.query(FitnessClass).all()
    return [
        {
            "id": c.id,
            "name": c.name,
            "instructor": c.instructor,
            "time": convert_to_timezone(c.time, timezone),
            "available_slots": c.available_slots
        } for c in classes
    ]

@app.post("/book")
def book_class(data: BookingRequest, db: Session = Depends(get_db)):
    fitness_class = db.query(FitnessClass).filter(FitnessClass.id == data.class_id).first()
    if not fitness_class:
        raise HTTPException(status_code=404, detail="Class not found")
    if fitness_class.available_slots <= 0:
        raise HTTPException(status_code=400, detail="No slots available")

    booking = Booking(
        class_id=data.class_id,
        client_name=data.client_name,
        client_email=data.client_email
    )
    fitness_class.available_slots -= 1
    db.add(booking)
    db.commit()
    return {"message": "Booking successful"}

@app.get("/bookings")
def get_bookings(email: EmailStr = Query(...), db: Session = Depends(get_db)):
    bookings = db.query(Booking).filter(Booking.client_email == email).all()
    return [{
        "id": b.id,
        "class_id": b.class_id,
        "client_name": b.client_name,
        "client_email": b.client_email
    } for b in bookings]
