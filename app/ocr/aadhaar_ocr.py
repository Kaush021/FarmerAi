import pytesseract
from PIL import Image
import re

def extract_aadhaar_details(image_path):
    text = pytesseract.image_to_string(Image.open(image_path), lang="eng+hin")

    aadhaar = re.search(r"\d{4}\s\d{4}\s\d{4}", text)
    name = re.search(r"Name[:\s]+([A-Za-z ]+)", text)

    return {
        "name": name.group(1).strip() if name else None,
        "aadhaar": aadhaar.group(0) if aadhaar else None
    }
