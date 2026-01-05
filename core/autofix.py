from utils.normalizeText_ClearBox import normalize_text
from utils.normalizeText_ClearBox import clear_box

def auto_fix_creative(img, boxes, rules):
    draw = ImageDraw.Draw(img)
    bg_color = img.getpixel((5, 5))  # green background

    safe_top = rules["rules"]["safe_zones"]["top"]

    current_y = safe_top + 20
    line_gap = 30

    for b in boxes:
        raw_text = b["text"]
        text = normalize_text(raw_text)

        # 🚫 Ignore OCR garbage
        if len(text) < 4:
            continue

        # 🚫 Ignore forbidden copy
        if any(f.upper() in text for f in rules["rules"]["forbidden_copy"]):
            continue

        # ✅ Clear old text
        clear_box(img, b["bbox"], bg_color)

        x, _, w, h = b["bbox"]

        # ✅ Controlled vertical stacking (NO overlap)
        draw.text((x, current_y), text, fill="white")
        current_y += h + line_gap

    return img
