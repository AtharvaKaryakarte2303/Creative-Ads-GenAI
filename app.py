violations = validate_creative(img, boxes, rules)

if violations:
    fixed_img = auto_fix_creative(img, boxes, rules)
else:
    fixed_img = img
