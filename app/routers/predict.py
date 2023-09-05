import os
from io import BytesIO
from typing import List

from PIL import Image
from fastapi import APIRouter, UploadFile, File
from ultralytics import YOLO

from app.models.prediction import Prediction
from app.services.preprocess import predictions_to_json

YOLO_MODEL_PATH = os.getenv('YOLO_MODEL_PATH')

router = APIRouter()

model = YOLO(f'{YOLO_MODEL_PATH}')


@router.post("/")
async def predict(file: UploadFile = File(...), response_model=List[Prediction]):
    # Charger l'image à partir du fichier
    image_stream = BytesIO(await file.read())
    image = Image.open(image_stream).convert("RGB")

    # Faire une prédiction
    results = model.predict(image, conf=0.25)

    predictions = predictions_to_json(results)

    return {'results': predictions}
