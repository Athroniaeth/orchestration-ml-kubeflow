import os
from io import BytesIO
from pathlib import Path

from PIL import Image
from fastapi.testclient import TestClient
from app.main import app

app = TestClient(app)
project_path = Path(os.getenv("PROJECT_PATH"))
image_path = project_path / 'tests' / 'data' / 'dog.jpeg'


def pillow_to_bytes(image: Image) -> BytesIO:
    image_bytes = BytesIO()
    image.save(image_bytes, format="JPEG")
    image_bytes.seek(0)
    return image_bytes


def test_valid_image():
    """Test si la route renvoie bien le bon modèle de prédiction quand l'utilisateur fournit une image."""
    valid_image = Image.open(image_path)
    valid_image = pillow_to_bytes(valid_image)

    response = app.post("/predict/", files={"file": valid_image})

    assert response.status_code == 200
    assert response.json() == {
        'results': [
            {
                'boxes': [0.0, 226.21920776367188, 664.9284057617188, 1278.9697265625],
                'confidence': 0.8,
                'label': 'dog'
            }
        ]}


def test_cropped_image():
    """Test si la route renvoie bien le bon modèle de prédiction quand l'utilisateur fournit une image."""
    valid_image = Image.open(image_path)
    cropped_image = valid_image.crop((20, 30, 50, 236))
    cropped_image = pillow_to_bytes(cropped_image)

    response = app.post("/predict/", files={"file": cropped_image})

    assert response.status_code == 200
    assert response.json() == {'results': []}


def test_empty_image():
    """Test si la route renvoie bien le bon modèle de prédiction quand l'utilisateur fournit une image."""
    empty_image = Image.new("RGB", (10, 10))  # Créer une image vide
    empty_image = pillow_to_bytes(empty_image)

    response = app.post("/predict/", files={"file": empty_image})

    assert response.status_code == 200
    assert response.json() == {'results': []}
