from models import FitnessClass
from database import SessionLocal
from datetime import datetime, timedelta
import pytz

def seed_classes():
    db = SessionLocal()
    ist = pytz.timezone("Asia/Kolkata")
    now = datetime.now(ist)
    if db.query(FitnessClass).first():
        db.close()
        return
    classes = [
        FitnessClass(name="Yoga", instructor="San", time=now + timedelta(days=1), available_slots=5),
        FitnessClass(name="Zumba", instructor="Sou", time=now + timedelta(days=2), available_slots=8),
        FitnessClass(name="HIIT", instructor="Sandhya", time=now + timedelta(days=3), available_slots=10)
    ]
    db.add_all(classes)
    db.commit()
    db.close()
