import gradio as gr

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
