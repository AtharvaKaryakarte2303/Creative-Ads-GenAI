def validate_creative(img, boxes, pack_bbox, rules):
    violations = []

    # Safe zone validation
    for b in boxes:
        x, y, w, h = b["bbox"]
        if y < rules["rules"]["safe_zones"]["top"]:
            violations.append({
                "type": "safe_zone",
                "text": b["text"],
                "issue": "top_safe_zone"
            })

    # Packshot validation
    if pack_bbox is None:
        violations.append({
            "type": "packshot",
            "issue": "missing"
        })

    return violations
