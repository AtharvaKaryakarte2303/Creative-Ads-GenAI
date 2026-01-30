import gradio as gr
import json
from PIL import Image

from utils.run_ocr import run_ocr
from utils.detect_packshot import detect_packshot
from core.validation import validate_creative
from core.autofix import auto_fix_creative

def load_rules(path="rules/tesco.json"):
    with open(path, "r") as f:
        raw = json.load(f)

    # 🔥 sanitize booleans
    raw["rules"]["safe_zones"]["enabled"] = int(raw["rules"]["safe_zones"]["enabled"])
    return raw

def process_image(img):
    tesco_rules = load_rules()
    boxes = run_ocr(img)
    pack_bbox = detect_packshot(img)

    violations = validate_creative(img, boxes, pack_bbox, tesco_rules)

    if violations:
        fixed = auto_fix_creative(img.copy(), boxes, tesco_rules)
        return fixed, json.dumps(violations, indent=2)

    return img, "No violations 🎉"



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
