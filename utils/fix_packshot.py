def fix_packshot(img_pil, rules):
    pack = detect_packshot(img_pil)
    if pack is None:
        return img_pil

    x, y, w, h = pack
    W, H = img_pil.size

    fixed = remove_old_packshot(img_pil, pack)
    draw = ImageDraw.Draw(fixed)

    # New size
    new_w = int(W * 0.28)
    new_h = int(H * 0.32)

    new_x = (W - new_w) // 2
    new_y = int(H * 0.55)

    # Draw placeholder box
    draw.rectangle([new_x, new_y, new_x+new_w, new_y+new_h],
                   outline="white", width=6)

    return fixed