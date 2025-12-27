def extract_intent(text):
    text = text.lower()

    if "flood" in text or "barish" in text:
        return "DISASTER_RELIEF"
    if "crop" in text or "fasal" in text:
        return "CROP_INSURANCE"
    return "GENERAL_QUERY"

