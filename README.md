# 🧘 Fitness Booking API

## Setup Instructions

1. Create virtual environment:
   ```bash
   python -m venv venv && source venv/bin/activate
   ```
2. Install dependencies:
   ```bash
   pip install fastapi uvicorn sqlalchemy pydantic pytz
   ```
3. Run the app:
   ```bash
   uvicorn main:app --reload
   ```

## Sample Requests

### View Classes
```bash
curl http://127.0.0.1:8000/classes?timezone=UTC
```

### Book Class
```bash
curl -X POST http://127.0.0.1:8000/book -H "Content-Type: application/json" -d '{"class_id": 1, "client_name": "Amit", "client_email": "amit@example.com"}'
```

### View Bookings
```bash
curl http://127.0.0.1:8000/bookings?email=amit@example.com
```
