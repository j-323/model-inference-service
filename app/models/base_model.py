# app/models/base_model.py

from abc import ABC, abstractmethod

class BaseModel(ABC):
    @abstractmethod
    def infer(self, prompt: str, **kwargs) -> tuple:
        """
        Выполняет инференс модели по заданному текстовому промпту с дополнительными параметрами.
        Возвращает кортеж (content: bytes, content_type: str).
        """
        pass
