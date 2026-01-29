from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="Mock Calendly API for Medical Clinic")

app.include_router(router)
