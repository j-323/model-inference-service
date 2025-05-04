# app/main.py

from fastapi import FastAPI
from app.api.endpoints import router as api_router
from app.core.config import HOST, PORT

app = FastAPI(
    title="Сервис генерации изображений и видео",
    description="Микросервис для инференса моделей генерации изображений (image-gen) и видео (video-gen) с передачей бинарных данных по REST."
)

app.include_router(api_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=HOST, port=PORT)
