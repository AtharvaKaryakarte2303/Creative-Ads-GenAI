import gradio as gr
import json
from PIL import Image

import pytesseract

pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)


from utils.run_ocr import run_ocr
from utils.detect_packshot import detect_packshot
from utils.visualise import draw_violations
from core.validation import validate_creative
from core.autofix import auto_fix_creative

def load_rules(path="rules/tesco.json"):
    with open(path, "r") as f:
        raw = json.load(f)

    rules = raw.get("rules", {})

    if "safe_zones" in rules and "enabled" in rules["safe_zones"]:
        rules["safe_zones"]["enabled"] = int(rules["safe_zones"]["enabled"])

    raw["rules"] = rules
    return raw

TESCO_RULES = load_rules()
def process_image(img):
    tesco_rules = load_rules()
    boxes = run_ocr(img)
    pack_bbox = detect_packshot(img)

    # FORCE a violation for testing
    violations = [{
        "type": "test_violation",
        "bbox": [50, 50, 300, 150]
    }]

    visual = draw_violations(img.copy(), violations, pack_bbox)

    return visual, json.dumps(violations, indent=2)


with gr.Blocks() as demo:
    gr.Markdown("## Creative Ads GenAI – Tesco Rules Engine")

    inp = gr.Image(type="pil", label="Upload Creative")
    out_img = gr.Image(label="Fixed Creative")
    out_txt = gr.Textbox(label="Validation Report")

    btn = gr.Button("Submit")

    btn.click(
        fn=process_image,
        inputs=inp,
        outputs=[out_img, out_txt]
    )

if __name__ == "__main__":
    demo.launch()
