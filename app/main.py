# app/main.py
from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="Farmer AI Caseworker")
app.include_router(router)
