def fix_safe_zones(img_pil, boxes, rules):
    safe = rules["rules"]["safe_zones"]
    top_safe = safe["top"]
    bottom_safe = safe["bottom"]

    fixed = img_pil.copy()
    draw = ImageDraw.Draw(fixed)
    W, H = fixed.size
    bg = fixed.getpixel((10, 10))

    updated = []
    for b in boxes:
        x, y, w, h = b["bbox"]
        orig_y = y

        if y < top_safe:
            y = top_safe
        if y + h > H - bottom_safe:
            y = H - bottom_safe - h

        if y != orig_y:
            draw.rectangle([x, orig_y, x+w, orig_y+h], fill=bg)
            draw.text((x, y), b["text"], fill="white")

        b["bbox"] = [x, y, w, h]
        updated.append(b)

    return fixed, updated