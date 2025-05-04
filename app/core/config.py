# app/core/config.py

HOST = "0.0.0.0"
PORT = 8003

DEFAULT_MODEL = "image-gen"
SUPPORTED_MODELS = ["image-gen", "video-gen"]

# Параметры по умолчанию для генерации изображений
IMAGE_GEN_DEFAULTS = {
    "num_inference_steps": 50,
    "guidance_scale": 7.5,
    "width": 512,
    "height": 512
}

# Параметры по умолчанию для генерации видео (демонстрационные)
VIDEO_GEN_DEFAULTS = {
    "num_frames": 16,
    "frame_rate": 8,
    "resolution": "512x512"
}
