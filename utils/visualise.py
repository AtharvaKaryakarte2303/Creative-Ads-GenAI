from PIL import ImageDraw, ImageFont

def draw_violations(img, violations, pack_bbox=None):
    draw = ImageDraw.Draw(img)

    # Draw packshot in GREEN
    if pack_bbox:
        draw.rectangle(pack_bbox, outline="green", width=4)
        draw.text(
            (pack_bbox[0], pack_bbox[1] - 15),
            "PACKSHOT",
            fill="green"
        )

    # Draw violations in RED
    for v in violations:
        bbox = v.get("bbox")
        label = v.get("type", "violation")

        if not bbox:
            continue

        draw.rectangle(bbox, outline="red", width=4)
        draw.text(
            (bbox[0], bbox[1] - 15),
            label.upper(),
            fill="red"
        )

    return img
