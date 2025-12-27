def recommend_scheme(intent):
    schemes = {
        "DISASTER_RELIEF": "PM Fasal Bima Yojana",
        "CROP_INSURANCE": "Crop Insurance Scheme",
        "GENERAL_QUERY": "Kisan Credit Card"
    }
    return schemes.get(intent, "Local Govt Scheme")

