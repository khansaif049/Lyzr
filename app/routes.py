from fastapi import APIRouter, HTTPException
from app.models import AvailabilityRequest, BookingRequest
from app.utils import generate_slots, is_slot_booked, bookings, APPOINTMENT_TYPES

router = APIRouter()

@router.get("/api/calendly/availability")
def get_availability(date: str, appointment_type: str):
    if appointment_type not in APPOINTMENT_TYPES:
        raise HTTPException(status_code=400, detail="Invalid appointment type")

    slots = generate_slots(date, appointment_type)
    response = []

    for slot in slots:
        available = not is_slot_booked(date, slot, appointment_type)
        response.append({
            "time": slot,
            "available": available
        })

    if not any(s["available"] for s in response):
        return {
            "message": "No availability for selected date and appointment type",
            "slots": []
        }

    return {
        "date": date,
        "appointment_type": appointment_type,
        "slots": response
    }


@router.post("/api/calendly/book")
def book_slot(booking: BookingRequest):
    if booking.appointment_type not in APPOINTMENT_TYPES:
        raise HTTPException(status_code=400, detail="Invalid appointment type")

    if is_slot_booked(booking.date, booking.time, booking.appointment_type):
        raise HTTPException(status_code=400, detail="Slot already booked")

    booking_data = booking.dict()
    bookings.append(booking_data)

    return {
        "status": "success",
        "message": "Appointment booked successfully",
        "booking": booking_data
    }
