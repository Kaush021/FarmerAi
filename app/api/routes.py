# app/api/routes.py
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def health_check():
    return {"status": "API working"}
