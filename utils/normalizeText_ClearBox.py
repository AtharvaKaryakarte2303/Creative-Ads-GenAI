import re
from PIL import ImageDraw

def normalize_text(text):
    text = text.lower()
    text = re.sub(r"[^a-z0-9 %]", "", text)
    return text.strip()


def clear_box(img, bbox, bg_color):
    draw = ImageDraw.Draw(img)
    x, y, w, h = bbox
    draw.rectangle([x, y, x + w, y + h], fill=bg_color)