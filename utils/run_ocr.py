import pytesseract
from PIL import Image

def run_ocr(img):
    data = pytesseract.image_to_data(img, output_type=pytesseract.Output.DICT)

    boxes = []
    for i, text in enumerate(data["text"]):
        if text.strip():
            boxes.append({
                "text": text,
                "bbox": [
                    data["left"][i],
                    data["top"][i],
                    data["width"][i],
                    data["height"][i]
                ]
            })
    return boxes