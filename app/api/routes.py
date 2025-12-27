# app/api/routes.py
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def health_check():
    return {"status": "API working"}

from fastapi import APIRouter, UploadFile
from app.voice.asr import speech_to_text
from app.nlp.intent import extract_intent
from app.nlp.entity import extract_entities
from app.schemes.recommender import recommend_scheme
from app.queue.producer import send_to_queue

router = APIRouter()

@router.post("/voice")
async def process_voice(audio: UploadFile):
    text = speech_to_text(audio.file)

    intent = extract_intent(text)
    entities = extract_entities(text)
    scheme = recommend_scheme(intent)

    send_to_queue("farmer_requests", {
        "text": text,
        "intent": intent,
        "entities": entities,
        "scheme": scheme
    })

    return {
        "text": text,
        "intent": intent,
        "entities": entities,
        "scheme": scheme
    }
