# app/models/model_factory.py

from app.core.config import IMAGE_GEN_DEFAULTS, VIDEO_GEN_DEFAULTS
from app.models.image_generation_model import ImageGenerationModel
from app.models.video_generation_model import VideoGenerationModel

class ModelFactory:
    @staticmethod
    def create_model(model_key: str):
        if model_key == "image-gen":
            return ImageGenerationModel(**IMAGE_GEN_DEFAULTS)
        elif model_key == "video-gen":
            return VideoGenerationModel(**VIDEO_GEN_DEFAULTS)
        else:
            raise ValueError(f"Модель '{model_key}' не поддерживается.")
