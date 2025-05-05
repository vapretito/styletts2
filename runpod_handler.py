import runpod

def setup():
    print("✅ Setup: StyleTTS2 listo (modo prueba)")
    return

def handler(event):
    text = event["input"].get("text", "Texto vacío")
    return {
        "message": f"Texto recibido correctamente: {text}"
    }

runpod.serverless.start({"handler": handler, "setup": setup})
