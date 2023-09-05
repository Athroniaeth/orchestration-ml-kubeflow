import os
import sys
from pathlib import Path
from dotenv import load_dotenv
from fastapi import FastAPI

PROJECT_PATH = Path(__file__).parent.parent.absolute()
APP_PATH = PROJECT_PATH / 'app'
ENV_PATH = PROJECT_PATH / '.env'

sys.path.append(f"{PROJECT_PATH}")

load_dotenv(dotenv_path=ENV_PATH)

os.environ['PROJECT_PATH'] = f'{PROJECT_PATH}'
os.environ['APP_PATH'] = f'{APP_PATH}'

YOLO_MODEL_PATH = os.getenv('YOLO_MODEL_PATH')
os.environ['YOLO_MODEL_PATH'] = f'{PROJECT_PATH}/{YOLO_MODEL_PATH}'

# Récupère les routes (doit être importé après la création de la variable environment APP_PATH)
# noinspection PyPep8
from app.routers import router

app = FastAPI()
app.include_router(router)
