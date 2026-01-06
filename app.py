import gradio as gr
from PIL import Image

from utils.run_ocr import run_ocr
from utils.detect_packshot import detect_packshot
from validation.validate_creative import validate_creative
from autofix.autofix_creative import auto_fix_creative
from rules.tesco_rules import tesco_rules

def process_image(img):
    boxes = run_ocr(img)
    pack_bbox = detect_packshot(img)

    violations = validate_creative(img, boxes, pack_bbox, tesco_rules)

    if violations:
        fixed = auto_fix_creative(img.copy(), boxes, tesco_rules)
        return fixed, violations
    else:
        return img, "Creative already compliant"

interface = gr.Interface(
    fn=process_image,
    inputs=gr.Image(type="pil", label="Upload Ad Creative"),
    outputs=[
        gr.Image(type="pil", label="Fixed Creative"),
        gr.JSON(label="Rule Violations")
    ],
    title="Creative Ads Gen AI",
    description="AI system that validates and auto-fixes ad creatives using brand rules"
)

interface.launch()
