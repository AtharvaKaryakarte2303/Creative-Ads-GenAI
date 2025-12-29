def detect_packshot(img_pil):
    img = img_pil.convert("RGB")
    W, H = img.size
    pix = img.load()

    found_pixels = []

    for y in range(H):
        for x in range(W):
            r, g, b = pix[x, y]

            # bright-ish object (packshot usually white/bright)
            if r > 180 and g > 180 and b > 180:
                found_pixels.append((x, y))

    if not found_pixels:
        return None

    xs = [p[0] for p in found_pixels]
    ys = [p[1] for p in found_pixels]

    min_x, max_x = min(xs), max(xs)
    min_y, max_y = min(ys), max(ys)

    w = max_x - min_x
    h = max_y - min_y

    return [min_x, min_y, w, h]
