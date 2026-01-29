from pydantic import BaseModel
from typing import List

class AvailabilityRequest(BaseModel):
    date: str
    appointment_type: str

class BookingRequest(BaseModel):
    date: str
    time: str
    appointment_type: str
    patient_name: str
    patient_email: str

class Slot(BaseModel):
    time: str
    available: bool

class AvailabilityResponse(BaseModel):
    date: str
    appointment_type: str
    slots: List[Slot]
