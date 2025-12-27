# app/ocr/aadhaar_ocr.py
import pytesseract
from PIL import Image
import re

def extract_aadhaar_details(image_path):
    text = pytesseract.image_to_string(Image.open(image_path), lang="eng+hin")

    aadhaar = re.findall(r"\d{4}\s\d{4}\s\d{4}", text)
    name = re.findall(r"Name[:\s]+([A-Za-z ]+)", text)

    return {
        "name": name[0] if name else None,
        "aadhaar": aadhaar[0] if aadhaar else None,
        "raw_text": text
    }
