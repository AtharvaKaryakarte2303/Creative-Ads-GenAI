def validate_creative(img, boxes, pack_bbox, rules):
    violations = []

    img_w, img_h = img.size
    safe_zone = rules["rules"]["safe_zones"]

    # ---------------- SAFE ZONE ----------------
    if safe_zone["enabled"]:
        top_limit = safe_zone["top"]
        bottom_limit = img_h - safe_zone["bottom"]

        for b in boxes:
            x1, y1, x2, y2 = b["bbox"]

            if y1 < top_limit:
                violations.append({
                    "type": "safe_zone",
                    "issue": "top_safe_zone",
                    "text": b.get("text", ""),
                    "bbox": b["bbox"]
                })

            if y2 > bottom_limit:
                violations.append({
                    "type": "safe_zone",
                    "issue": "bottom_safe_zone",
                    "text": b.get("text", ""),
                    "bbox": b["bbox"]
                })

    # ---------------- PACKSHOT ----------------
    if pack_bbox is None:
        violations.append({
            "type": "packshot",
            "issue": "missing"
        })

    return violations

