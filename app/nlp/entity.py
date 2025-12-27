import re

CROPS = ["wheat", "rice", "paddy", "maize"]
DISASTERS = ["flood", "drought", "barish"]

def extract_entities(text):
    text = text.lower()

    entities = {
        "crop": None,
        "disaster": None,
        "location": None,
        "aadhaar_requested": False
    }

    for crop in CROPS:
        if crop in text:
            entities["crop"] = crop

    for d in DISASTERS:
        if d in text:
            entities["disaster"] = d

    if "aadhaar" in text or "aadhar" in text:
        entities["aadhaar_requested"] = True

    loc = re.search(r"from\s([a-z ]+)", text)
    if loc:
        entities["location"] = loc.group(1)

    return entities
