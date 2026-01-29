# Mock Calendly API for Medical Clinic

This project is a mock implementation of a Calendly-like scheduling system for a medical clinic using **FastAPI (Python 3.10+)**.  
It simulates backend scheduling logic such as appointment availability, slot booking, and appointment type handling without using any external scheduling service.

The goal of this project is to demonstrate:

- Backend API design
- Time slot generation logic
- Booked vs available slot detection
- Handling of “no availability” scenarios
- Clean and structured JSON responses

---

## Project Structure

```
calendly_mock/
│
├── app/
│   ├── main.py        # FastAPI application entry point
│   ├── models.py      # Pydantic schemas
│   ├── routes.py      # API endpoints
│   └── utils.py       # Core scheduling and booking logic
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup & Run

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

API will be available at:

```
http://127.0.0.1:8000
```

Swagger UI:

```
http://127.0.0.1:8000/docs
```

---

## 🏥 Appointment Types & Durations

| Appointment Type | Duration |
| ---------------- | -------- |
| Consultation     | 30 mins  |
| Follow-up        | 15 mins  |
| Dental Checkup   | 45 mins  |

Clinic working hours:

```
09:00 AM – 05:00 PM
```

Slots are automatically generated based on the appointment duration and clinic timing.

---

## 🔍 1. Check Availability

**Endpoint**

```
GET /api/calendly/availability
```

**Query Parameters**

```
date=YYYY-MM-DD
appointment_type=Consultation
```

**Example**

```
GET /api/calendly/availability?date=2026-01-30&appointment_type=Consultation
```

**Response**

```json
{
  "date": "2026-01-30",
  "appointment_type": "Consultation",
  "slots": [
    {
      "time": "09:00",
      "available": true
    },
    {
      "time": "09:30",
      "available": false
    },
    {
      "time": "10:00",
      "available": true
    }
  ]
}
```

### ⚠️ Important

If a time slot is **already booked**, then in the response:

```json
"available": false
```

If a time slot is **free**, then:

```json
"available": true
```

---

## 🚫 No Availability Scenario

If no slots are available for a selected date and appointment type:

```json
{
  "message": "No availability for selected date and appointment type",
  "slots": []
}
```

---

## 📝 2. Book an Appointment

**Endpoint**

```
POST /api/calendly/book
```

**Request Body**

```json
{
  "date": "2026-01-30",
  "time": "10:00",
  "appointment_type": "Consultation",
  "patient_name": "Khan Safiullah",
  "patient_email": "khansafiullah9821@gmail.com"
}
```

**Success Response**

```json
{
  "status": "success",
  "message": "Appointment booked successfully",
  "booking": {
    "date": "2026-01-30",
    "time": "10:00",
    "appointment_type": "Consultation",
    "patient_name": "Khan Safiullah",
    "patient_email": "khansafiullah9821@gmail.com"
  }
}
```

---

## 🧠 Core Logic Summary

- Slots are generated dynamically based on:
  - Appointment type
  - Duration
  - Clinic working hours
- All bookings are stored in-memory for simplicity.
- Slot availability is calculated as:

```python
available = not is_slot_booked(...)
```

So:

- Booked slot → `"available": false`
- Free slot → `"available": true`

---

## 🎯 Why This Project?

This project demonstrates:

- Clean API architecture
- Real-world scheduling logic
- Strong backend fundamentals
- Proper error handling
- Readable and production-style code structure

Perfect for technical assessments and backend-focused interviews.
