from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from database import Base

class FitnessClass(Base):
    __tablename__ = "fitness_classes"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    instructor = Column(String)
    time = Column(DateTime)
    available_slots = Column(Integer)

class Booking(Base):
    __tablename__ = "bookings"
    id = Column(Integer, primary_key=True, index=True)
    class_id = Column(Integer, ForeignKey("fitness_classes.id"))
    client_name = Column(String)
    client_email = Column(String, index=True)
