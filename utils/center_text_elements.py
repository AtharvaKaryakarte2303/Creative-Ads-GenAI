def center_text_elements(img_pil, boxes):
    fixed = img_pil.copy()
    draw = ImageDraw.Draw(fixed)
    W, H = fixed.size
    bg = fixed.getpixel((10, 10))

    # Pick largest text as headline
    if not boxes:
        return fixed

    headline = max(boxes, key=lambda b:b["bbox"][2] * b["bbox"][3])

    text = headline["text"]
    x, y, w, h = headline["bbox"]

    draw.rectangle([x, y, x+w, y+h], fill=bg)

    new_x = int((W - w) / 2)
    new_y = int(H * 0.10)

    draw.text((new_x, new_y), text, fill="white")
    headline["bbox"] = [new_x, new_y, w, h]

    return fixed