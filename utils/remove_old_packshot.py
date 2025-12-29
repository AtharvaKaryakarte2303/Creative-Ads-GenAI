def remove_old_packshot(img_pil, pack):
    if pack is None:
        return img_pil

    x, y, w, h = pack
    img = img_pil.copy()
    draw = ImageDraw.Draw(img)
    bg = img.getpixel((10, 10))
    draw.rectangle([x, y, x+w, y+h], fill=bg)
    return img