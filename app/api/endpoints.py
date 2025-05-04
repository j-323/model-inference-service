# app/api/endpoints.py

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from fastapi.responses import Response
from app.core.config import DEFAULT_MODEL, SUPPORTED_MODELS
from app.services.inference_service import InferenceService

router = APIRouter()

class InferenceRequest(BaseModel):
    prompt: str = Field(..., description="Текстовый промпт для генерации изображения или видео")
    model: str = Field(DEFAULT_MODEL, description="Тип модели: image-gen или video-gen")
    # Параметры для image-gen
    num_inference_steps: int = Field(None, description="Количество шагов инференса (для image-gen)")
    guidance_scale: float = Field(None, description="Масштаб руководства (для image-gen)")
    width: int = Field(None, description="Ширина изображения (для image-gen)")
    height: int = Field(None, description="Высота изображения (для image-gen)")
    # Параметры для video-gen
    num_frames: int = Field(None, description="Количество кадров в видео (для video-gen)")
    frame_rate: int = Field(None, description="Частота кадров (для video-gen)")
    resolution: str = Field(None, description="Разрешение видео, например, '512x512' (для video-gen)")

@router.post("/infer")
def infer(request: InferenceRequest):
    if request.model not in SUPPORTED_MODELS:
        raise HTTPException(
            status_code=400,
            detail=f"Модель '{request.model}' не поддерживается. Допустимые: {SUPPORTED_MODELS}"
        )
    
    params = {}
    if request.model == "image-gen":
        params = {
            "num_inference_steps": request.num_inference_steps,
            "guidance_scale": request.guidance_scale,
            "width": request.width,
            "height": request.height
        }
    elif request.model == "video-gen":
        params = {
            "num_frames": request.num_frames,
            "frame_rate": request.frame_rate,
            "resolution": request.resolution
        }
    
    try:
        service = InferenceService(request.model)
        result = service.run_inference(request.prompt, **{k: v for k, v in params.items() if v is not None})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    # Ожидаем, что result — кортеж (content: bytes, media_type: str)
    if not isinstance(result, tuple) or len(result) != 2:
        raise HTTPException(status_code=500, detail="Некорректный формат вывода модели")
    
    content, media_type = result
    return Response(content=content, media_type=media_type)
