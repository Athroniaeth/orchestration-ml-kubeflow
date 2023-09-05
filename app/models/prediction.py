from typing import List

from pydantic import BaseModel


class Prediction(BaseModel):
    """Modèle Pydantic pour une prédiction d'un modèle YoloV8"""
    label: str
    confidence: float
    boxes: List[float]
