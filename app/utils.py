from datetime import datetime, timedelta

# Appointment types with duration (minutes)
APPOINTMENT_TYPES = {
    "Consultation": 30,
    "Follow-up": 15,
    "Dental Checkup": 45
}

CLINIC_START = 9
CLINIC_END = 17

# In-memory booking storage
bookings = []

def generate_slots(date: str, appointment_type: str):
    duration = APPOINTMENT_TYPES[appointment_type]
    start_time = datetime.strptime(f"{date} {CLINIC_START}:00", "%Y-%m-%d %H:%M")
    end_time = datetime.strptime(f"{date} {CLINIC_END}:00", "%Y-%m-%d %H:%M")

    slots = []
    while start_time + timedelta(minutes=duration) <= end_time:
        slots.append(start_time.strftime("%H:%M"))
        start_time += timedelta(minutes=duration)

    return slots


def is_slot_booked(date, time, appointment_type):
    for booking in bookings:
        if (
            booking["date"] == date and
            booking["time"] == time and
            booking["appointment_type"] == appointment_type
        ):
            return True
    return False
