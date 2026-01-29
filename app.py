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
    try:
        print("✅ Image received:", type(img))

        tesco_rules = load_rules()
        print("✅ Rules loaded")

        boxes = run_ocr(img)
        print("✅ OCR boxes:", boxes)

        pack_bbox = detect_packshot(img)
        print("✅ Packshot:", pack_bbox)

        violations = validate_creative(img, boxes, pack_bbox, tesco_rules)
        print("✅ Violations:", violations)

        if violations:
            fixed = auto_fix_creative(img.copy(), boxes, tesco_rules)
            return fixed, json.dumps(violations, indent=2)

        return img, json.dumps({"status": "No violations 🎉"}, indent=2)

    except Exception as e:
        print("🔥 ERROR:", str(e))
        return img, json.dumps({"error": str(e)}, indent=2)


iface = gr.Interface(
    fn=process_image,
    inputs=gr.Image(type="pil", label="Upload Creative"),
    outputs=[
        gr.Image(label="Fixed Creative"),
        gr.Textbox(label="Validation Report", lines=10)
    ],
    title="Creative Ads GenAI – Tesco Rules Engine",
    description="Upload an ad creative. The system validates and auto-fixes it based on brand rules.",
    allow_flagging="never"
)

if __name__ == "__main__":
    iface.launch(
        server_name="127.0.0.1",
        server_port=7860,
        share=False,
        show_api=False   # 🔥 THIS LINE KILLS THE ERROR
    )
