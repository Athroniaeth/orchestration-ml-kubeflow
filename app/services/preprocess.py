from typing import List, Dict

import numpy
from ultralytics.engine.results import Results

from app.models.prediction import Prediction


def predictions_to_json(results: Results) -> List[Prediction]:
    predictions: List[Prediction] = []

    for result in results:
        arrays: List[numpy.ndarray] = result.boxes.data.cpu().numpy()
        for array in arrays:
            array: List = array.tolist()

            boxes = array[:4]
            confidence = round(array[4], 2)
            label = result.names[array[5]]

            prediction = Prediction(label=label, boxes=boxes, confidence=confidence)

            predictions.append(prediction)

    return predictions
