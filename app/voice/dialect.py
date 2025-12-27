def detect_dialect(text):
    if "गढ़वाली" in text:
        return "Garhwali"
    if "कुमाऊँ" in text:
        return "Kumaoni"
    return "Hindi"
