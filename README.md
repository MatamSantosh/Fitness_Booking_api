#  Fitness Booking API

## Setup Instructions


1. Clone or Upload Project
   ```bash
   git clone https://github.com/MatamSantosh/Fitness_Booking_api.git
   cd Fitness_Booking_api
    ```
2. Create virtual environment:
   ```bash
   python -m venv venv && source venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install fastapi uvicorn sqlalchemy pydantic pytz
   ```
4. Run the app:
   ```bash
   uvicorn main:app --host 0.0.0.0 --port 8000
   ```
5. Your Api is now accessible via:
    ```bash
    http://localhost:8000
     ```
6. Navigate to Swagger UI
    ```bash
    http://localhost:8000/docs
    ```
   To see a list of available endpoints:
   - /classes
   - /book
   - /bookings

## Sample Requests

### View Classes
```bash
curl http://127.0.0.1:8000/classes?timezone=UTC
```

### Book Class
```bash
curl -X POST http://127.0.0.1:8000/book -H "Content-Type: application/json" -d '{"class_id": 1, "client_name": "san", "client_email": "san@example.com"}'
```

### View Bookings
```bash
curl http://127.0.0.1:8000/bookings?email=san@example.com
```
