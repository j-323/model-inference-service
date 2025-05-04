# app/services/inference_service.py

from app.models.model_factory import ModelFactory
from app.services.decorators import log_inference

class InferenceService:
    def __init__(self, model_key: str):
        self.model = ModelFactory.create_model(model_key)

    @log_inference
    def run_inference(self, prompt: str, **params) -> tuple:
        """
        Возвращает результат инференса в виде кортежа (bytes, media_type)
        """
        return self.model.infer(prompt, **params)
