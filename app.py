import gradio as gr
import json
from PIL import Image

from utils.run_ocr import run_ocr
from utils.detect_packshot import detect_packshot
from core.validation import validate_creative
from core.autofix import auto_fix_creative

def load_rules(path="rules/tesco.json"):
    with open(path, "r") as f:
        return json.load(f)

def process_image(img):
    tesco_rules = load_rules()
    boxes = run_ocr(img)
    pack_bbox = detect_packshot(img)

    violations = validate_creative(img, boxes, pack_bbox, tesco_rules)

    if violations:
        fixed = auto_fix_creative(img.copy(), boxes, tesco_rules)
        return fixed, violations

    return img, ["No violations 🎉"]


iface = gr.Interface(
    fn=process_image,
    inputs=gr.Image(type="pil", label="Upload Creative"),
    outputs=[
        gr.Image(label="Fixed Creative"),
        gr.JSON(label="Validation Report")
    ],
    title="Creative Ads GenAI – Tesco Rules Engine",
    description="Upload an ad creative. The system validates and auto-fixes it based on brand rules."
)

if __name__ == "__main__":
    iface.launch()
